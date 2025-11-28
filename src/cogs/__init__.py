"""
Cogs (command groups) for the Echo Discord bot.
"""

# Economy system (split into modules)
from .economy import Economy

# Game cogs
from .blackjack import Blackjack
from .slots import Slots

# Feature cogs
from .moderation import Moderation
from .fun import Fun
from .help import Help

# Extension cogs
from .farming import Farming
from .crafting import Crafting
from .jobs import Jobs

__all__ = [
    'Economy',
    'Blackjack',
    'Slots',
    'Moderation',
    'Fun',
    'Help',
    'Farming',
    'Crafting',
    'Jobs',
]
