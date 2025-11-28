# Echo Bot Architecture

This document provides a comprehensive overview of Echo's system architecture, design patterns, and implementation details.

## 📋 Table of Contents

- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Core Components](#core-components)
- [Data Flow](#data-flow)
- [Database Schema](#database-schema)
- [Design Patterns](#design-patterns)
- [Security Considerations](#security-considerations)
- [Performance & Scalability](#performance--scalability)

---

## Overview

Echo is a Discord bot built with discord.py that provides economy, gaming, and moderation features. The architecture follows a modular, cog-based design for maintainability and extensibility.

### Technology Stack

- **Language**: Python 3.12+
- **Framework**: discord.py 2.3.2
- **Database**: SQLite 3
- **Image Processing**: Pillow (PIL)
- **Async**: asyncio

### Design Philosophy

1. **Modularity** - Features organized into independent cogs
2. **Separation of Concerns** - Clear boundaries between layers
3. **Maintainability** - Clean code with documentation
4. **Extensibility** - Easy to add new features

---

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Discord API                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                     main.py (Entry Point)                   │
│  - Bot initialization                                       │
│  - Cog loading                                             │
│  - Event handling                                          │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│    Cogs     │  │    Core     │  │   Models    │
│             │  │             │  │             │
│ - Economy   │  │ - Database  │  │ - User      │
│ - Games     │  │ - Config    │  │ - Inventory │
│ - Moderation│  │             │  │             │
│ - Fun       │  │             │  │             │
└──────┬──────┘  └──────┬──────┘  └─────────────┘
       │                │
       │                ▼
       │         ┌─────────────┐
       │         │  SQLite DB  │
       │         │             │
       │         │ - user_data │
       │         │ - cooldowns │
       │         │ - items     │
       │         └─────────────┘
       │
       ▼
┌─────────────┐
│   Utils     │
│             │
│ - Utilities │
│ - Constants │
│ - Eco       │
└─────────────┘
```

---

## Core Components

### 1. Entry Point (`main.py`)

**Responsibilities:**
- Initialize Discord bot client
- Load all cogs
- Handle global events (`on_ready`, `on_message`)
- Start bot and maintain connection

**Key Functions:**
```python
async def setup_bot()      # Load all cogs
async def on_ready()       # Bot startup event
async def on_message()     # Message filtering
async def run_bot()        # Start the bot
```

### 2. Cogs Layer

Cogs are modular command groups that encapsulate related functionality.

#### Economy System (`cogs/economy/`)

Modular economy system split into:

**`inventory.py`** - Inventory Management
- Commands: `inventory`, `buy`, `sell`, `trade`
- Admin commands: `give`, `add_item`, `remove_item`
- Handles item transactions and inventory operations

**`transactions.py`** - Money Management
- Commands: `pay`, `deposit`, `withdraw`, `balance`, `baltop`, `networth`
- Manages pocket money and bank accounts
- Calculates user net worth

**`games.py`** - Earning & Gambling
- Earning: `dig`, `hunt`, `scrap`, `beg`, `daily`
- Gambling: `gamble`, `rob`
- Fun: `shoot`, `bomb`

**`__init__.py`** - Main Economy Cog
- Combines all economy sub-cogs
- Initializes economy system

#### Game Cogs

**`blackjack.py`**
- Interactive blackjack game
- Card rendering with PIL
- Image composition for hands

**`slots.py`**
- Animated slot machine
- GIF generation
- Weighted probability system

#### Extension Cogs

**`farming.py`**
- Plant and harvest crops
- Time-based growth system
- Profit calculation

**`crafting.py`**
- Recipe-based crafting
- Item combination system
- Ingredient validation

**`jobs.py`**
- Job selection system
- Salary collection
- Interactive buttons

#### Utility Cogs

**`fun.py`**
- General utility commands
- QR code generation
- Server/user info

**`help.py`**
- Dynamic help system
- Pagination
- Tutorial system

**`moderation.py`**
- User moderation (kick, ban, mute)
- Channel management (lock, clear)
- Server management

### 3. Core Layer (`core/`)

**`database.py`** - Database Management

Encapsulates all database operations:

```python
class Database:
    def __init__(self, db_dir: str = 'data')

    # Balance operations
    def get_user_balance(user_id: int) -> int
    def get_bank_balance(user_id: int) -> int
    def update_user_balance(user_id: int, amount: int)
    def update_bank_balance(user_id: int, amount: int)

    # Inventory operations
    def get_user_inventory(user_id: int) -> List[str]
    def add_item_to_inventory(user_id: int, item_id: str)
    def remove_item_from_inventory(user_id: int, item_id: str) -> bool

    # Cooldown operations
    def get_cooldown_remaining(user_id: int, action: str) -> float
    def update_cooldown(user_id: int, action: str, timestamp: float)
    def clear_cooldowns(exclude_actions: List[str] = None)
```

### 4. Models Layer (`models/`)

**`user.py`** - Data Models

Data classes representing entities:

```python
@dataclass
class UserBalance:
    user_id: int
    pocket: int
    bank: int

    @property
    def total(self) -> int:
        return self.pocket + self.bank

@dataclass
class UserInventory:
    user_id: int
    items: List[str]

    def count_item(self, item_id: str) -> int
    def has_item(self, item_id: str) -> bool
    def add_item(self, item_id: str) -> None
    def remove_item(self, item_id: str) -> bool

@dataclass
class UserPlantation:
    user_id: int
    harvest_time: float
    amount: int
```

### 5. Utils Layer (`utils/`)

**`constants.py`** - Constants & Configuration
- Color constants
- Cooldown durations
- Economy settings
- Message templates
- File paths

**`utilities.py`** - Helper Functions
- Embed creation
- Channel locking
- Admin checks
- Time conversion
- QR code generation

**`eco_support.py`** - Economy Support
- Item definitions (cosmetics, craftables, shop)
- Crafting recipes
- Database initialization
- Cooldown functions
- Farming functions

---

## Data Flow

### Command Execution Flow

```
User sends message
        │
        ▼
Discord API receives message
        │
        ▼
Bot on_message event
        │
        ├─> Link filter check
        │
        ▼
Command dispatcher
        │
        ▼
Cog command handler
        │
        ├─> Check permissions
        ├─> Check cooldowns
        ├─> Validate input
        │
        ▼
Execute command logic
        │
        ├─> Database operations
        ├─> Calculations
        ├─> State updates
        │
        ▼
Create response embed
        │
        ▼
Send to Discord API
        │
        ▼
User sees response
```

### Database Operation Flow

```
Command needs data
        │
        ▼
Call eco_support function
        │
        ▼
Open SQLite connection
        │
        ▼
Execute SQL query
        │
        ├─> SELECT (read)
        ├─> INSERT (create)
        ├─> UPDATE (modify)
        └─> DELETE (remove)
        │
        ▼
Process results
        │
        ▼
Close connection
        │
        ▼
Return data to command
```

---

## Database Schema

### `user_data.db`

**Table: `user_balances`**
```sql
CREATE TABLE user_balances (
    user_id TEXT PRIMARY KEY,
    balance INTEGER DEFAULT 0,
    inventory TEXT DEFAULT '[]'  -- JSON array
)
```

**Table: `user_bank_balances`**
```sql
CREATE TABLE user_bank_balances (
    user_id TEXT PRIMARY KEY,
    balance INTEGER DEFAULT 0,
    last_interest_update REAL DEFAULT 0
)
```

**Table: `user_carrot_plantations`**
```sql
CREATE TABLE user_carrot_plantations (
    user_id TEXT PRIMARY KEY,
    harvest_time REAL,
    amount INTEGER
)
```

### `cooldowns.db`

**Table: `cooldowns`**
```sql
CREATE TABLE cooldowns (
    user_id TEXT,
    action TEXT,
    last_action_time REAL,
    PRIMARY KEY (user_id, action)
)
```

### `items.db`

**Table: `items`**
```sql
CREATE TABLE items (
    item_name TEXT PRIMARY KEY,
    desc TEXT,
    cost INTEGER
)
```

---

## Design Patterns

### 1. Cog Pattern (Command Pattern)

Discord.py's Cog system implements the Command pattern:

```python
class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx):
        # Command logic
        pass
```

**Benefits:**
- Encapsulation of related commands
- Easy to load/unload features
- Clear separation of concerns

### 2. Repository Pattern (Database Access)

The `Database` class acts as a repository:

```python
class Database:
    def get_user_balance(self, user_id: int) -> int:
        # Encapsulates database access
        pass
```

**Benefits:**
- Centralized data access
- Easy to swap database implementations
- Testable with mocks

### 3. Singleton Pattern (Configuration)

Configuration is loaded once and shared:

```python
# In utilities.py
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
```

### 4. Factory Pattern (Embed Creation)

Helper function creates consistent embeds:

```python
def make_embed(title: str, description: str, color: discord.Color) -> discord.Embed:
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_footer(text="Footer text")
    return embed
```

### 5. Strategy Pattern (Item Drop System)

Weighted random selection for item drops:

```python
chosen_item = random.choices(
    list(cosmetics_items.keys()),
    weights=[item["chance"] for item in cosmetics_items.values()],
    k=1
)[0]
```

---

## Security Considerations

### Current Security Measures

1. **Admin Authorization**
   ```python
   def is_admin(ctx):
       return ctx.author.id == config.get("ADMIN_ID")
   ```

2. **Link Filtering**
   ```python
   if any(link in message.content for link in BANNED_LINKS):
       await message.delete()
   ```

3. **Input Validation**
   - Amount checks for transactions
   - User existence validation
   - Item ownership verification

### Security Concerns

⚠️ **Known Vulnerabilities:**

1. **Eval() Usage** (CRITICAL)
   - Location: `utils/utilities.py:217`
   - Risk: Arbitrary code execution
   - Fix: Use `ast.literal_eval()` or safe math parser

2. **Plain Text Token Storage**
   - Location: `config.json`
   - Risk: Token exposure if committed
   - Fix: Use environment variables

3. **SQL Injection** (LOW RISK)
   - Using parameterized queries (✅ Protected)
   - But should migrate to ORM

### Recommended Security Improvements

1. Move secrets to `.env` file
2. Remove `eval()` usage
3. Add rate limiting
4. Implement permission checks
5. Add input sanitization
6. Use prepared statements everywhere

---

## Performance & Scalability

### Current Performance Characteristics

**Database:**
- SQLite (file-based)
- Synchronous operations
- No connection pooling

**Limitations:**
- Single server only (no sharding)
- Blocking I/O for database
- In-memory data structures

### Bottlenecks

1. **Database Reads**
   - Every command hits database
   - No caching layer
   - Synchronous SQLite

2. **Image Generation**
   - Blackjack card rendering
   - Slots GIF generation
   - CPU-intensive

3. **Message Processing**
   - Link filtering on every message
   - No rate limiting

### Scalability Improvements

**For Small to Medium Servers (< 10k users):**
- Current architecture is fine
- SQLite handles load well

**For Large Servers (> 10k users):**

1. **Add Caching**
   ```python
   from functools import lru_cache

   @lru_cache(maxsize=1000)
   def get_user_balance(user_id: int) -> int:
       # Cache frequently accessed data
       pass
   ```

2. **Migrate to PostgreSQL**
   - Better concurrency
   - ACID transactions
   - Connection pooling

3. **Add Redis for Caching**
   - Cache balances
   - Cache cooldowns
   - Session management

4. **Implement Sharding**
   - Discord.py sharding support
   - Horizontal scaling

5. **Add Rate Limiting**
   ```python
   @commands.cooldown(1, 60, commands.BucketType.user)
   async def command(self, ctx):
       pass
   ```

---

## Module Dependency Graph

```
main.py
  │
  ├─> cogs/
  │     ├─> economy/
  │     │     ├─> inventory.py  ──┐
  │     │     ├─> transactions.py ┼──> utils.eco_support
  │     │     └─> games.py       ─┘
  │     ├─> farming.py ────────────> utils.eco_support
  │     ├─> crafting.py ───────────> utils.eco_support
  │     └─> ...
  │
  ├─> core/
  │     └─> database.py
  │
  ├─> models/
  │     └─> user.py
  │
  └─> utils/
        ├─> constants.py
        ├─> utilities.py ──> config.json
        └─> eco_support.py
```

---

## Future Architecture Improvements

### Short Term
1. Replace direct SQLite calls with `Database` class
2. Add comprehensive logging
3. Split `eco_support.py` into modules
4. Add type hints throughout

### Medium Term
1. Implement caching layer
2. Add proper error handling
3. Create test suite
4. Add monitoring/metrics

### Long Term
1. Migrate to PostgreSQL
2. Add Redis for caching
3. Implement microservices architecture
4. Add API for external integrations

---

## References

- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)

---

**Last Updated**: 28-11-2025