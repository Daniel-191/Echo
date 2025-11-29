"""
This file contains anything economy game related
e.g functions to load databases, access databases
"""

from utilities import *


# List of all cosmetics
cosmetics_items = {
    # Swords
    "r.sword": {"name": "Rare Sword", "sell": 2500, "chance": 25},
    "leg.sword": {"name": "Legendary Sword", "sell": 5000, "chance": 15},
    "mythical_sword": {"name": "Mythical sword", "sell": 12500, "chance": 5},

    # Tools
    "shovel": {"name": "Shovel used for digging", "sell": 1000, "chance": 23},
    "bow": {"name": "Bow used for hunting", "sell": 1000, "chance": 20},

    # Other items (High to low chance)
    "god": {"name": "An item that only the gods can hold.", "sell": 15000000, "chance": 0.1},
    "infinity": {"name": "Infinity Gauntlet", "sell": 30000, "chance": 5},
    "david4": {"name": "David's 4th ball", "sell": 25000, "chance": 7},
    "stick": {"name": "Stick", "sell": 15000, "chance": 15},
    "gun": {"name": "Glock-18", "sell": 8000, "chance": 19},
    "tech": {"name": "Electronics", "sell": 1000, "chance": 25},
    "weed": {"name": "Weed", "sell": 5000, "chance": 30},
    "sulphur": {"name": "Sulphur", "sell": 500, "chance": 40},
    "charcoal": {"name": "Charcoal", "sell": 300, "chance": 50},
    "clock": {"name": "Alarm Clock", "sell": 700, "chance": 30},
    "roll": {"name": "Roll", "sell": 1500, "chance": 33},
    "potato": {"name": "Potato", "sell": 100, "chance": 65},
}


# List of all items you can craft
craftables = {
    "joint": {"name": "Weed rolled in paper", "sell": 10000},
    "poo": {"name": "Its poo made by the gods", "sell": 2000},
    "c4": {"name": "C4 BOMB", "sell": 25000},
    "excalibur": {"name": "The Excalibur", "sell": 35000},
    "m4a1": {"name": "Assault Rifle", "sell": 30000},
    "excalibur": {"name": "Excalibur", "sell": 30000},
    "8_incher": {"name": "Long hard Stick", "sell": 40000},
    "complete_gauntlet": {"name": "Infinity  Gauntlet", "sell": 60000},
    "glitch": {"name": "A glitch in the matrix", "sell": 50000000}
}


"""
If you are adding items to the shop do the following:

- Add your custom items
- Turn off bot
- delete items.db in the databases directory
- Start bot
- New items will be created along with the database
Enjoy!
"""
shop_items = {
    "silver": {"desc": "Bank full? Cant afford any gold? Buy some silver", "cost": 1000},
    "gold": {"desc": "Too rich? Banks full? Invest some money into gold. No interest, but its safe.", "cost": 10000},
    "shovel": {"desc": "Dig up treasure, find items and make money!", "cost": 1000},
    "bow": {"desc": "You can now hunt animals! Sell what you find and make money while doing it.", "cost": 1000},
    #"example": {"desc": "This is the item description!!", "cost": 1234},
}

combined_items = {**cosmetics_items, **craftables}

# crafting recipes
crafting_recipes = {
    "excalibur": {
        "gun": 2,
        "mythical_sword": 1,
        "result": "excalibur"  # A powerful sword that only the one can handle
    },
    "m4a1": {
        "gun": 2,
        "stick": 1,
        "result": "m4a1"  # Shoot down your enemies
    },
    "8_incher": {
        "stick": 1,
        "david4": 1,
        "result": "8_incher"  # A unique and 8 inch weapon
    },
    "complete_gauntlet": {
        "infinity": 1,
        "leg.sword": 1,
        "david4": 1,
        "result": "complete_gauntlet"  # The most powerful item in the game
    },
    "c4": {
        "sulphur": 2,
        "charcoal": 1,
        "clock": 1,
        "potato": 5,  # Because why not?
        "tech": 2,
        "result": "c4" # C4 Bomb for bombing kids
    },
    "poo": {
        "charcoal": 3,
        "sulphur": 1,
        "result": "poo"
    },
    "joint": {
        "roll": 1,
        "weed": 1,
        "result": "joint" # Get high asf 
    },
    "glitch": {
        "god": 2,
        "result": "glitch" # rarest item in the game, if you have this your legit a god
    }
}

# Import database paths and cooldowns from constants
from utils.constants import (
    DB_USER_DATA as DATA_DB,
    DB_COOLDOWNS as COOLDOWN_DB,
    DB_ITEMS as ITEMS_DB,
    DB_LOCKED_CHANNELS as LOCKED_CHANNELS_DB,
    COOLDOWN_ROB,
    COOLDOWN_DAILY,
    COOLDOWN_DIG,
    COOLDOWN_HUNT,
    COOLDOWN_SCAVENGE,
    COOLDOWN_BEG,
    COOLDOWN_INTEREST,
    BANK_INTEREST_RATE
)

# Create the databases and tables if they don't exist
def initialize_databases():
    try:
        # Initialize user data database
        with sqlite3.connect(DATA_DB) as conn:
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
            # No need for explicit commit/close - with statement handles it

        # Initialize cooldowns database
        with sqlite3.connect(COOLDOWN_DB) as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS cooldowns (
                    user_id TEXT,
                    action TEXT,
                    last_action_time REAL,
                    PRIMARY KEY (user_id, action)
                )
            ''')

        # Initialize locked channels database
        with sqlite3.connect(LOCKED_CHANNELS_DB) as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS locked_channels (
                    channel_id TEXT PRIMARY KEY,
                    unlock_time TEXT
                )
            ''')

        with sqlite3.connect(ITEMS_DB) as conn:
            c = conn.cursor()
            # Create items table if not exists
            c.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    item_name TEXT PRIMARY KEY,
                    desc TEXT,
                    cost INTEGER
                )
            ''')

            # Insert data into items table
            for item_name, item_data in shop_items.items():
                c.execute('''
                    INSERT OR IGNORE INTO items (item_name, desc, cost) VALUES (?, ?, ?)
                ''', (item_name, item_data['desc'], item_data['cost']))
    except Exception as e:
        print(f"CRITICAL ERROR initializing databases: {e}")
        raise  # Re-raise since this is critical

initialize_databases()


def load_cooldowns():
    try:
        with sqlite3.connect(COOLDOWN_DB) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM cooldowns')
            cooldowns = {f"{row[0]}_{row[1]}": row[2] for row in c.fetchall()}
        return cooldowns
    except Exception as e:
        print(f"Error loading cooldowns: {e}")
        return {}  # Return empty dict on error


def load_user_plants():
    try:
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM user_carrot_plantations')
            user_plantations = {}
            for row in c.fetchall():
                user_id, harvest_time, amount_planted = row
                try:
                    harvest_time = float(harvest_time)
                    amount_planted = int(amount_planted)
                    user_plantations[user_id] = (harvest_time, amount_planted)
                except ValueError as e:
                    continue  # Skip this row if conversion fails
        return user_plantations
    except Exception as e:
        print(f"Error loading user plantations: {e}")
        return {}  # Return an empty dictionary or handle the error as appropriate


def save_cooldowns(cooldowns):
    try:
        with sqlite3.connect(COOLDOWN_DB) as conn:
            c = conn.cursor()
            for key, value in cooldowns.items():
                user_id, action = key.split('_')
                c.execute('REPLACE INTO cooldowns (user_id, action, last_action_time) VALUES (?, ?, ?)', (user_id, action, value))
    except Exception as e:
        print(f"Error saving cooldowns: {e}")


def save_user_plants(user_plantations):
    try:
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()

            # Use REPLACE INTO for efficient upsert (handles both INSERT and UPDATE)
            for user_id, (harvest_time, amount_planted) in user_plantations.items():
                c.execute('REPLACE INTO user_carrot_plantations (user_id, harvest_time, amount) VALUES (?, ?, ?)',
                          (user_id, harvest_time, amount_planted))

            # Delete plantations for users not in the current user_plantations dict
            if user_plantations:
                placeholders = ','.join('?' * len(user_plantations))
                c.execute(f'DELETE FROM user_carrot_plantations WHERE user_id NOT IN ({placeholders})',
                          list(user_plantations.keys()))
            else:
                # If no plantations exist, clear the table
                c.execute('DELETE FROM user_carrot_plantations')
    except Exception as e:
        print(f"Error saving user plantations: {e}")
  

def user_has_plants(user_id):
    """Check if a user has planted carrots - optimized single query."""
    try:
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()
            c.execute('SELECT 1 FROM user_carrot_plantations WHERE user_id = ? LIMIT 1', (str(user_id),))
            return c.fetchone() is not None
    except Exception as e:
        print(f"Error checking user plants: {e}")
        return False


def update_plants():
    try:
        global user_carrot_plantations
        user_carrot_plantations = load_user_plants()
        
        if user_carrot_plantations is None:
            print("No user carrot plantations loaded.")  # Debug statement
            return  # Handle the case where data loading failed or returned None

        current_time = datetime.now().timestamp()
        
        for user_id, (harvest_time, amount) in user_carrot_plantations.items():
            time_left_seconds = max(0, harvest_time - current_time)
            if time_left_seconds <= 0:
                # Harvest the crops if the growth time has passed
                total_profit = amount * carrot_sell
                update_user_balance(user_id, total_profit)
                del user_carrot_plantations[user_id]  # Removing the plantation record
            else:
                # Update the time left in the percentage
                growth_percentage = min(100, ((growth_duration - time_left_seconds) / growth_duration) * 100)
                user_carrot_plantations[user_id] = (harvest_time, amount)  # Ensure consistency

        # Save the updated data
        save_user_plants(user_carrot_plantations)

    except Exception as e:
        print(f"Error updating plants: {e}")
        

def plant_carrots(user_id, amount):
    total_cost = amount * cost_per_carrot

    try:
        # Update balance
        update_user_balance(user_id, -total_cost)  # Deducting the cost for planting

        # Directly insert/update user's plantation - no need to load all plantations
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()
            c.execute('REPLACE INTO user_carrot_plantations (user_id, harvest_time, amount) VALUES (?, ?, ?)',
                     (str(user_id), get_current_time(), amount))
    except Exception as e:
        print(e)


def update_bank_interest(user_id, max_bank_size):
    try:
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()

            # Get both balance and last interest update in single query
            c.execute('SELECT balance, last_interest_update FROM user_bank_balances WHERE user_id = ?', (user_id,))
            result = c.fetchone()

            if result is None:
                # User doesn't exist yet
                return

            bank_balance = result[0] if result[0] is not None else 0
            last_interest_update = result[1] if result[1] else 0

            time_difference = time.time() - last_interest_update

            if time_difference >= COOLDOWN_INTEREST:
                interest_amount = int(bank_balance * BANK_INTEREST_RATE)
                interest_amount = min(interest_amount, max_bank_size - bank_balance)

                new_balance = bank_balance + interest_amount

                # Update both balance and last_interest_update in same transaction
                c.execute('UPDATE user_bank_balances SET balance = ?, last_interest_update = ? WHERE user_id = ?',
                         (new_balance, time.time(), user_id))
    except Exception as e:
        print(f"Error updating bank interest: {e}")


# Function to retrieve user inventory from the database
def get_user_inventory(user_id):
    try:
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()
            c.execute('SELECT inventory FROM user_balances WHERE user_id = ?', (user_id,))
            inventory = c.fetchone()
        return json.loads(inventory[0]) if inventory and inventory[0] else []
    except Exception as e:
        print(f"Error in get_user_inventory: {e}")
        return []


def add_item_to_inventory(user_id, item_name):
    try:
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()

            # Get current inventory in same connection
            c.execute('SELECT inventory FROM user_balances WHERE user_id = ?', (user_id,))
            result = c.fetchone()

            # Load existing inventory or create new
            if result and result[0]:
                inventory = json.loads(result[0])
            else:
                inventory = []

            # Add item and save
            inventory.append(item_name)
            inventory_json = json.dumps(inventory)

            if result:
                # Update existing entry
                c.execute('UPDATE user_balances SET inventory = ? WHERE user_id = ?', (inventory_json, user_id))
            else:
                # Insert new entry
                c.execute('INSERT INTO user_balances (user_id, inventory) VALUES (?, ?)', (user_id, inventory_json))

    except Exception as e:
        print(f"Error in add_item_to_inventory: {e}")


def remove_item_from_inventory(user_id, item_name):
    try:
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()

            # Get current inventory in same connection
            c.execute('SELECT inventory FROM user_balances WHERE user_id = ?', (user_id,))
            result = c.fetchone()

            if result and result[0]:
                inventory = json.loads(result[0])

                if item_name in inventory:
                    inventory.remove(item_name)
                    inventory_json = json.dumps(inventory)

                    # Update only the inventory field using UPDATE statement
                    c.execute('UPDATE user_balances SET inventory = ? WHERE user_id = ?', (inventory_json, user_id))

    except Exception as e:
        print(f"Error removing item from inventory: {e}")


def get_user_balance(user_id):
    try:
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()
            c.execute('SELECT balance FROM user_balances WHERE user_id = ?', (user_id,))
            result = c.fetchone()
            if result is None:
                c.execute('INSERT INTO user_balances (user_id) VALUES (?)', (user_id,))
                result = (0,)
            return result[0]
    except Exception as e:
        print(f"Error getting user balance: {e}")
        return 0  # Return 0 on error


def get_user_bank_balance(user_id):
    try:
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()
            c.execute('SELECT balance FROM user_bank_balances WHERE user_id = ?', (user_id,))
            result = c.fetchone()
            if result is None:
                c.execute('INSERT INTO user_bank_balances (user_id) VALUES (?)', (user_id,))
                result = (0,)
            return result[0]
    except Exception as e:
        print(f"Error getting user bank balance: {e}")
        return 0  # Return 0 on error


def update_user_balance(user_id, amount):
    try:
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()

            # Get current balance and inventory in single connection
            c.execute('SELECT balance, inventory FROM user_balances WHERE user_id = ?', (user_id,))
            result = c.fetchone()

            if result is None:
                # User doesn't exist, create with initial values
                current_balance = 0
                current_inventory = []
            else:
                current_balance = result[0] if result[0] is not None else 0
                current_inventory = json.loads(result[1]) if result[1] else []

            # Calculate the new balance
            new_balance = current_balance + amount

            # Update in same connection
            c.execute('REPLACE INTO user_balances (user_id, balance, inventory) VALUES (?, ?, ?)',
                      (user_id, new_balance, json.dumps(current_inventory)))
    except Exception as e:
        print(f"Error updating user balance: {e}")


def update_bank_balance(user_id, amount):
    try:
        with sqlite3.connect(DATA_DB) as conn:
            c = conn.cursor()

            # Get current bank balance in same connection
            c.execute('SELECT balance FROM user_bank_balances WHERE user_id = ?', (user_id,))
            result = c.fetchone()

            if result is None:
                # User doesn't exist, create with initial balance
                current_balance = 0
            else:
                current_balance = result[0] if result[0] is not None else 0

            # Calculate new balance and update
            new_balance = current_balance + amount
            c.execute('REPLACE INTO user_bank_balances (user_id, balance) VALUES (?, ?)', (user_id, new_balance))
    except Exception as e:
        print(f"Error updating bank balance: {e}")


# COOLDOWN FUNCTIONS


def get_current_time():
    return time.time()


def get_cooldown_remaining(user_id, action, cooldowns, cooldown_duration):
    last_action_time = cooldowns.get(f"{user_id}_{action}", 0)
    current_time = get_current_time()
    return current_time - last_action_time


def can_perform_action(user_id, action, cooldown_duration):
    cooldowns = load_cooldowns()
    cooldown_remaining = get_cooldown_remaining(user_id, action, cooldowns, cooldown_duration)
    return cooldown_remaining >= cooldown_duration


def update_last_action_time(user_id, action):
    cooldowns = load_cooldowns()
    cooldowns[f"{user_id}_{action}"] = get_current_time()
    save_cooldowns(cooldowns)

def can_rob(user_id):
    return can_perform_action(user_id, "rob", COOLDOWN_ROB)


def can_claim_daily(user_id):
    return can_perform_action(user_id, "claim", COOLDOWN_DAILY)


def can_dig(user_id):
    return can_perform_action(user_id, "dig", COOLDOWN_DIG)


def can_hunt(user_id):
    return can_perform_action(user_id, "hunt", COOLDOWN_HUNT)


def can_scavenge(user_id):
    return can_perform_action(user_id, "scavenge", COOLDOWN_SCAVENGE)


def can_beg(user_id):
    return can_perform_action(user_id, "beg", COOLDOWN_BEG)


def can_plant(user_id):
    return can_perform_action(user_id, "plant", growth_duration * 3600)  # 12 hours in seconds


# ============================================================================
# LOCKED CHANNELS DATABASE FUNCTIONS
# ============================================================================

def save_locked_channel(channel_id, unlock_time):
    """Save a locked channel to the database."""
    try:
        with sqlite3.connect(LOCKED_CHANNELS_DB) as conn:
            c = conn.cursor()
            c.execute('INSERT OR REPLACE INTO locked_channels (channel_id, unlock_time) VALUES (?, ?)',
                      (str(channel_id), unlock_time))
    except Exception as e:
        print(f"Error saving locked channel: {e}")


def remove_locked_channel(channel_id):
    """Remove a locked channel from the database."""
    try:
        with sqlite3.connect(LOCKED_CHANNELS_DB) as conn:
            c = conn.cursor()
            c.execute('DELETE FROM locked_channels WHERE channel_id = ?', (str(channel_id),))
    except Exception as e:
        print(f"Error removing locked channel: {e}")


def get_locked_channels():
    """Get all locked channels from the database as a dictionary."""
    try:
        with sqlite3.connect(LOCKED_CHANNELS_DB) as conn:
            c = conn.cursor()
            c.execute('SELECT channel_id, unlock_time FROM locked_channels')
            rows = c.fetchall()

        locked_channels = {}
        for channel_id, unlock_time in rows:
            locked_channels[channel_id] = {"unlock_time": unlock_time}
        return locked_channels
    except Exception as e:
        print(f"Error getting locked channels: {e}")
        return {}  # Return empty dict on error


def is_channel_locked(channel_id):
    """Check if a channel is locked."""
    try:
        with sqlite3.connect(LOCKED_CHANNELS_DB) as conn:
            c = conn.cursor()
            c.execute('SELECT 1 FROM locked_channels WHERE channel_id = ?', (str(channel_id),))
            result = c.fetchone()
            return result is not None
    except Exception as e:
        print(f"Error checking if channel is locked: {e}")
        return False  # Return False on error


def set_last_claim_time(user_id):
    update_last_action_time(user_id, "claim")


def log_purchase(user_id, mode ,username , item_name, item_cost):
    if mode == 1:
        with open("data/logs.txt", "a") as log_file:
            log_file.write(f"User {user_id} | {username} bought {item_name} for {item_cost} Credits.\n")
    elif mode == 0:
        with open("data/logs.txt", "a") as log_file:
            log_file.write(f"User {user_id} | {username} sold {item_name} for {item_cost} Credits.\n")
