"""
User data models for the Echo bot economy system.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class UserBalance:
    """Represents a user's balance information."""
    user_id: int
    pocket: int
    bank: int

    @property
    def total(self) -> int:
        """Calculate total balance (pocket + bank)."""
        return self.pocket + self.bank


@dataclass
class UserInventory:
    """Represents a user's inventory."""
    user_id: int
    items: List[str]

    def count_item(self, item_id: str) -> int:
        """Count occurrences of an item in inventory."""
        return self.items.count(item_id)

    def has_item(self, item_id: str) -> bool:
        """Check if user has an item."""
        return item_id in self.items

    def add_item(self, item_id: str) -> None:
        """Add an item to inventory."""
        self.items.append(item_id)

    def remove_item(self, item_id: str) -> bool:
        """Remove an item from inventory. Returns True if successful."""
        if item_id in self.items:
            self.items.remove(item_id)
            return True
        return False


@dataclass
class UserPlantation:
    """Represents a user's crop plantation."""
    user_id: int
    harvest_time: float
    amount: int
