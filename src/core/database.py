"""
Database management for Echo bot.
Handles all SQLite database operations for user data, balances, and inventories.
"""

import sqlite3
import json
from typing import List, Optional, Tuple
from pathlib import Path


class Database:
    """Manages database connections and operations for the bot."""

    def __init__(self, db_dir: str = 'src/databases'):
        """
        Initialize database connections.

        Args:
            db_dir: Directory where database files are stored
        """
        self.db_dir = Path(db_dir)
        self.data_db = str(self.db_dir / 'user_data.db')
        self.cooldown_db = str(self.db_dir / 'cooldowns.db')
        self.items_db = str(self.db_dir / 'items.db')

        self._initialize_databases()

    def _initialize_databases(self) -> None:
        """Create database tables if they don't exist."""
        # Initialize user data database
        with sqlite3.connect(self.data_db) as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS user_balances (
                    user_id TEXT PRIMARY KEY,
                    balance INTEGER DEFAULT 0,
                    inventory TEXT DEFAULT '[]'
                )
            ''')
            c.execute('''
                CREATE TABLE IF NOT EXISTS user_bank_balances (
                    user_id TEXT PRIMARY KEY,
                    balance INTEGER DEFAULT 0,
                    last_interest_update REAL DEFAULT 0
                )
            ''')
            c.execute('''
                CREATE TABLE IF NOT EXISTS user_carrot_plantations (
                    user_id TEXT PRIMARY KEY,
                    harvest_time REAL,
                    amount INTEGER
                )
            ''')
            conn.commit()

        # Initialize cooldowns database
        with sqlite3.connect(self.cooldown_db) as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS cooldowns (
                    user_id TEXT,
                    action TEXT,
                    last_action_time REAL,
                    PRIMARY KEY (user_id, action)
                )
            ''')
            conn.commit()

    # Balance Operations
    def get_user_balance(self, user_id: int) -> int:
        """Get user's pocket balance."""
        with sqlite3.connect(self.data_db) as conn:
            c = conn.cursor()
            c.execute('SELECT balance FROM user_balances WHERE user_id = ?', (str(user_id),))
            result = c.fetchone()
            if result is None:
                c.execute('INSERT INTO user_balances (user_id) VALUES (?)', (str(user_id),))
                conn.commit()
                return 0
            return result[0]

    def get_bank_balance(self, user_id: int) -> int:
        """Get user's bank balance."""
        with sqlite3.connect(self.data_db) as conn:
            c = conn.cursor()
            c.execute('SELECT balance FROM user_bank_balances WHERE user_id = ?', (str(user_id),))
            result = c.fetchone()
            if result is None:
                c.execute('INSERT INTO user_bank_balances (user_id) VALUES (?)', (str(user_id),))
                conn.commit()
                return 0
            return result[0]

    def update_user_balance(self, user_id: int, amount: int) -> None:
        """Update user's pocket balance by adding amount (can be negative)."""
        current_balance = self.get_user_balance(user_id)
        current_inventory = self.get_user_inventory(user_id)
        new_balance = current_balance + amount

        with sqlite3.connect(self.data_db) as conn:
            c = conn.cursor()
            c.execute('REPLACE INTO user_balances (user_id, balance, inventory) VALUES (?, ?, ?)',
                      (str(user_id), new_balance, json.dumps(current_inventory)))
            conn.commit()

    def update_bank_balance(self, user_id: int, amount: int) -> None:
        """Update user's bank balance by adding amount (can be negative)."""
        balance = self.get_bank_balance(user_id) + amount
        with sqlite3.connect(self.data_db) as conn:
            c = conn.cursor()
            c.execute('REPLACE INTO user_bank_balances (user_id, balance) VALUES (?, ?)',
                      (str(user_id), balance))
            conn.commit()

    # Inventory Operations
    def get_user_inventory(self, user_id: int) -> List[str]:
        """Get user's inventory as a list of item IDs."""
        with sqlite3.connect(self.data_db) as conn:
            c = conn.cursor()
            c.execute('SELECT inventory FROM user_balances WHERE user_id = ?', (str(user_id),))
            result = c.fetchone()
            if result is None or not result[0]:
                return []
            return json.loads(result[0])

    def add_item_to_inventory(self, user_id: int, item_id: str) -> None:
        """Add an item to user's inventory."""
        inventory = self.get_user_inventory(user_id)
        inventory.append(item_id)

        with sqlite3.connect(self.data_db) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM user_balances WHERE user_id = ?', (str(user_id),))
            existing = c.fetchone()

            if existing:
                c.execute('UPDATE user_balances SET inventory = ? WHERE user_id = ?',
                          (json.dumps(inventory), str(user_id)))
            else:
                c.execute('INSERT INTO user_balances (user_id, inventory) VALUES (?, ?)',
                          (str(user_id), json.dumps(inventory)))
            conn.commit()

    def remove_item_from_inventory(self, user_id: int, item_id: str) -> bool:
        """Remove an item from user's inventory. Returns True if successful."""
        inventory = self.get_user_inventory(user_id)

        if item_id in inventory:
            inventory.remove(item_id)
            with sqlite3.connect(self.data_db) as conn:
                c = conn.cursor()
                c.execute('UPDATE user_balances SET inventory = ? WHERE user_id = ?',
                          (json.dumps(inventory), str(user_id)))
                conn.commit()
            return True
        return False

    # Cooldown Operations
    def get_cooldown_remaining(self, user_id: int, action: str) -> float:
        """Get the time remaining for a cooldown."""
        with sqlite3.connect(self.cooldown_db) as conn:
            c = conn.cursor()
            c.execute('SELECT last_action_time FROM cooldowns WHERE user_id = ? AND action = ?',
                      (str(user_id), action))
            result = c.fetchone()
            return result[0] if result else 0

    def update_cooldown(self, user_id: int, action: str, timestamp: float) -> None:
        """Update the last action time for a cooldown."""
        with sqlite3.connect(self.cooldown_db) as conn:
            c = conn.cursor()
            c.execute('REPLACE INTO cooldowns (user_id, action, last_action_time) VALUES (?, ?, ?)',
                      (str(user_id), action, timestamp))
            conn.commit()

    def clear_cooldowns(self, exclude_actions: List[str] = None) -> None:
        """Clear all cooldowns except specified actions."""
        exclude_actions = exclude_actions or []
        with sqlite3.connect(self.cooldown_db) as conn:
            c = conn.cursor()
            if exclude_actions:
                placeholders = ','.join('?' * len(exclude_actions))
                c.execute(f"DELETE FROM cooldowns WHERE action NOT IN ({placeholders})", exclude_actions)
            else:
                c.execute("DELETE FROM cooldowns")
            conn.commit()
