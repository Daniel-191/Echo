"""
Constants and configuration values for Echo bot.
Centralized location for all magic numbers and hardcoded values.
"""

import discord

# ============================================================================
# COLORS
# ============================================================================

# Embed Colors
COLOR_SUCCESS = discord.Color.green()
COLOR_ERROR = discord.Color.red()
COLOR_INFO = discord.Color.blue()
COLOR_WARNING = discord.Color.orange()
COLOR_CYAN = discord.Color.from_rgb(0, 255, 255)  # Default embed color

# Alternative color definitions (for hex values)
HEX_SUCCESS = 0x00FF00
HEX_ERROR = 0xFF0000
HEX_INFO = 0x0099FF
HEX_WARNING = 0xFFA500


# ============================================================================
# COOLDOWNS (in seconds)
# ============================================================================

# Action Cooldowns
COOLDOWN_ROB = 3600         # 1 hour
COOLDOWN_DAILY = 86400      # 24 hours
COOLDOWN_DIG = 60           # 1 minute
COOLDOWN_HUNT = 60          # 1 minute
COOLDOWN_SCAVENGE = 60      # 1 minute
COOLDOWN_BEG = 15           # 15 seconds
COOLDOWN_SLOTS = 3          # 3 seconds
COOLDOWN_INTEREST = 86400   # 24 hours (bank interest)


# ============================================================================
# ECONOMY SETTINGS
# ============================================================================

# Default Values
DEFAULT_BALANCE = 0
DEFAULT_BANK_BALANCE = 0

# Limits
MAX_BANK_SIZE = 500000           # Default max bank capacity (overridden by config)
MAX_GAMBLE_AMOUNT = 500000       # Default max gamble bet (overridden by config)
MAX_INVENTORY_SIZE = 1000        # Maximum items in inventory

# Daily Reward
DEFAULT_DAILY_REWARD = 15000     # Default daily claim amount (overridden by config)

# Interest Rate
BANK_INTEREST_RATE = 0.10        # 10% daily interest on bank balance

# Gambling Odds
GAMBLE_WIN_CHANCE = 0.33         # 1/3 chance to win (33%)
ROB_SUCCESS_CHANCE = 0.45        # 45% success rate
ROB_PERCENTAGE = 0.20            # Rob 20% of target's balance


# ============================================================================
# EARNING RANGES (min, max credits)
# ============================================================================

# Digging Rewards
DIG_CREDITS_MIN = 1000
DIG_CREDITS_MAX = 1600

# Hunting Rewards
HUNT_CREDITS_MIN = 600
HUNT_CREDITS_MAX = 1300

# Scavenging Rewards
SCAVENGE_CREDITS_MIN = 400
SCAVENGE_CREDITS_MAX = 800

# Begging Rewards
BEG_CREDITS_MIN = 100
BEG_CREDITS_MAX = 200


# ============================================================================
# FARMING SETTINGS
# ============================================================================

# Carrot Farming
DEFAULT_CARROT_PLANT_COST = 100      # Cost per carrot to plant (overridden by config)
DEFAULT_CARROT_SELL_PRICE = 125      # Sell price per carrot (overridden by config)
DEFAULT_MAX_CARROTS = 1000           # Max carrots plantable at once (overridden by config)
DEFAULT_CARROT_GROWTH_HOURS = 12     # Hours to grow (overridden by config)
CARROT_GROWTH_SECONDS = 3600 * DEFAULT_CARROT_GROWTH_HOURS  # Converted to seconds


# ============================================================================
# JOB SETTINGS
# ============================================================================

# Job Salary Ranges (min, max)
JOB_FREELANCER_SALARY = (50, 100)
JOB_GAMER_SALARY = (20, 80)
JOB_CHEF_SALARY = (30, 70)


# ============================================================================
# GAME SETTINGS
# ============================================================================

# Slots
SLOTS_WIN_CHANCE = 0.25          # 25% win rate
SLOTS_REEL_ITEM_HEIGHT = 180     # Height of each item on slot reel
SLOTS_SPIN_SPEED = 6             # Animation speed multiplier

# Blackjack
BLACKJACK_STARTING_BALANCE = 100  # Starting chips for demo

# Card Values
CARD_VALUE_ACE_HIGH = 11
CARD_VALUE_ACE_LOW = 1
CARD_VALUE_FACE = 10             # Jack, Queen, King


# ============================================================================
# DATABASE PATHS
# ============================================================================

DB_DIR = 'data'
DB_USER_DATA = 'data/user_data.db'
DB_COOLDOWNS = 'data/cooldowns.db'
DB_ITEMS = 'data/items.db'

# Data Files
FILE_LOCKED_CHANNELS = 'data/locked_channels.json'
FILE_LOGS = 'data/logs.txt'


# ============================================================================
# ASSET PATHS
# ============================================================================

PATH_CARDS = 'assets/cards'
PATH_IMAGES = 'assets/images'
PATH_TABLE_IMAGE = 'assets/images/table.png'


# ============================================================================
# MESSAGES & TEMPLATES
# ============================================================================

# Error Messages
MSG_NO_PERMISSION = "You don't have permission to use this command."
MSG_INSUFFICIENT_FUNDS = "You don't have enough credits."
MSG_INVALID_AMOUNT = "Please enter a valid amount."
MSG_COOLDOWN_ACTIVE = "You're on cooldown. Please wait before using this command again."

# Success Messages
MSG_PURCHASE_SUCCESS = "Purchase successful!"
MSG_SALE_SUCCESS = "Item sold successfully!"

# Footer Text
FOOTER_HELP = "Need some help? Do {prefix}tutorial"
FOOTER_CREDITS = "Made by mal023"


# ============================================================================
# LIMITS & CONSTRAINTS
# ============================================================================

# Command Limits
MAX_BALTOP_DISPLAY = 10          # Number of top users to show in baltop
MAX_TRADE_AMOUNT = 100           # Max items per trade

# Timeout Settings
BUTTON_TIMEOUT = 60              # Seconds before buttons timeout
VIEW_TIMEOUT = 180               # Seconds before views timeout

# Pagination
ITEMS_PER_PAGE = 10              # Items per page in paginated lists
ITEMS_PER_PAGE_ECONOMY = 15      # Items per page in economy/cosmetics lists


# ============================================================================
# SPECIAL VALUES
# ============================================================================

# Admin
ADMIN_BYPASS_COOLDOWNS = True    # Whether admins bypass cooldowns

# Logging
LOG_PURCHASE_MODE_BUY = 1
LOG_PURCHASE_MODE_SELL = 0


# ============================================================================
# ITEM RARITY WEIGHTS
# ============================================================================

# These are default weights - actual values are in eco_support.py
RARITY_COMMON = 50
RARITY_UNCOMMON = 30
RARITY_RARE = 15
RARITY_LEGENDARY = 5
RARITY_MYTHICAL = 1


# ============================================================================
# DISCORD LIMITS (from Discord API)
# ============================================================================

DISCORD_EMBED_TITLE_LIMIT = 256
DISCORD_EMBED_DESCRIPTION_LIMIT = 4096
DISCORD_EMBED_FIELD_LIMIT = 25
DISCORD_EMBED_FIELD_NAME_LIMIT = 256
DISCORD_EMBED_FIELD_VALUE_LIMIT = 1024
DISCORD_MESSAGE_LIMIT = 2000
