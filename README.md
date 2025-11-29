<div align="center">
  <img src="https://github.com/Daniel-191/Echo/blob/main/images/bot_icon.png" alt="Echo Bot Image" width="400">
</div>

<h1 align="center">
  <br>
  Echo Bot v6 - DEPRECATED - NO LONGER MAINTAINED
  <br>
</h1>

<p align="center">Admin, AutoMod, Economy, Fun, Invite, Information, Moderation, Owner, Social, Suggestion, Tickets, verify, Utility and More...</p>

<br>

<p align="center">
  <a href="#-features">Features</a>
  •
  <a href="#-prerequisites">Prerequisites</a>
  •
  <a href="#-installation">Installation</a>
  •
  <a href="#-commands">Commands</a>
</p>

<br>

## ✨ Features

- 💰 **Advanced Economy System** - Earn, trade, and manage virtual currency
- 🎮 **Interactive Games** - Blackjack, Slots, and more
- 🌾 **Farming System** - Plant and harvest crops for profit
- 🔨 **Crafting System** - Combine items to create valuable goods
- 🛡️ **Moderation Tools** - Kick, ban, mute, and channel management
- 🎲 **Fun Commands** - Jokes, quotes, QR codes, and utilities
- 📊 **Leaderboards** - Track top players by net worth
- 🏦 **Banking System** - Deposit money to earn daily interest

## 📦 Prerequisites

- [Python 3.12+](https://www.python.org/downloads/release/python-3120/)
- [Git](https://git-scm.com/downloads)
- A Discord Bot Token ([Create one here](https://discord.com/developers/applications))

## 🚀 Installation

### Windows

1. Open Command Prompt and clone the repository:
```bash
git clone https://github.com/Daniel-191/Echo
cd Echo
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the bot:
   - Open `config.json` in a text editor
   - Add your **Bot Token** (required)
   - Add your **User ID** as admin (optional)
   - Add your **Bot Invite Link** (optional)

5. Run the bot:
```bash
python main.py
```

### Linux / macOS

1. Open Terminal and clone the repository:
```bash
git clone https://github.com/Daniel-191/Echo
cd Echo
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the bot:
```bash
nano config.json
```
   - Add your **Bot Token** (required)
   - Add your **User ID** as admin (optional)
   - Add your **Bot Invite Link** (optional)

5. Run the bot:
```bash
python3 main.py
```

## 📝 Configuration

Edit `config.json` with your settings:

```json
{
  "token": "YOUR_BOT_TOKEN_HERE",
  "prefix": "!",
  "ADMIN_ID": 123456789012345678,
  "invite_link": "https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID",
  "link_ban": "false",
  "daily_reward": 15000,
  "carrot_plant_cost": 100,
  "carrot_sell": 125,
  "max_carrots": 1000,
  "growth_duration": 12
}
```

## 💬 Commands

> Default prefix: `!`

### General Commands

| Command | Description |
|---------|-------------|
| `help` | Display all available commands |
| `ping` | Check bot latency |
| `avatar [@user]` | Display user's avatar |
| `serverinfo` | Display server information |
| `userinfo [@user]` | Display user information |
| `membercount` | Show server member count |
| `quote` | Get an inspiring quote |
| `joke` | Get a random joke |
| `8ball <question>` | Ask the magic 8-ball |
| `coinflip <heads/tails>` | Flip a coin |
| `dice` | Roll a dice |
| `qr <text/link>` | Generate a QR code |
| `calculator <expression>` | Perform calculations |

### 💰 Economy Commands

| Command | Description |
|---------|-------------|
| `balance [@user]` | Check wallet and bank balance |
| `networth [@user]` | Check total net worth (including items) |
| `baltop` | View the richest players leaderboard |
| `daily` | Claim daily reward (15,000 credits) |
| `pay <@user> <amount>` | Send money to another user |
| `deposit <amount/max>` | Deposit money into bank (earns 10% daily interest) |
| `withdraw <amount/max>` | Withdraw money from bank |

### 🎯 Earning Commands

| Command | Description |
|---------|-------------|
| `beg` | Beg for money (100-200 credits) |
| `dig` | Dig for treasure (requires shovel, 1,000-1,600 credits) |
| `hunt` | Hunt for items (requires bow, 600-1,300 credits) |
| `scrap` | Scavenge for items (400-800 credits) |

### 🎲 Gambling Commands

| Command | Description |
|---------|-------------|
| `gamble <amount>` | Gamble credits with 33% win chance |
| `rob <@user>` | Attempt to rob another player (45% success) |
| `blackjack <amount>` | Play blackjack with interactive cards |
| `slots <amount>` | Play the slot machine |

### 🛒 Shop & Inventory

| Command | Description |
|---------|-------------|
| `shop` | View items available for purchase |
| `buy <item>` | Purchase an item from the shop |
| `sell <item>` | Sell an item from your inventory |
| `inventory [@user]` | View your or another user's inventory |
| `trade <@user> <item>` | Trade an item with another player |
| `cosmetics` | View all findable cosmetic items |

### 🌾 Farming Commands

| Command | Description |
|---------|-------------|
| `plant <amount/max>` | Plant carrots (100 credits each, 25% profit) |
| `harvest` | Harvest grown crops after 12 hours |

### 🔨 Crafting Commands

| Command | Description |
|---------|-------------|
| `recipes` | View all craftable items and recipes |
| `craft <item>` | Craft an item using materials |

### 🎮 Action Commands

| Command | Description |
|---------|-------------|
| `shoot <@user>` | Shoot someone (requires Gun or M4A1) |
| `bomb <@user>` | Bomb someone (requires C4) |

### 🛡️ Moderation Commands

> Admin/Moderator only

| Command | Description |
|---------|-------------|
| `kick <@user> [reason]` | Kick a member from the server |
| `ban <@user> [reason]` | Ban a member from the server |
| `mute <@user> [reason]` | Mute a member |
| `unmute <@user>` | Unmute a member |
| `clear <amount>` | Delete messages in bulk (1-100) |
| `lockchannel [duration]` | Lock a channel temporarily |
| `unlockchannel` | Unlock a locked channel |
| `lockserver [duration]` | Lock the entire server |
| `unlockserver` | Unlock the entire server |

### ⚙️ Admin Commands

> Bot owner only

| Command | Description |
|---------|-------------|
| `give <@user> <amount>` | Give credits to a user |
| `additem <@user> <item>` | Add an item to user's inventory |
| `removeitem <@user> <item>` | Remove an item from user's inventory |
| `config_view` | View current bot configuration |
| `config_edit <key> <value>` | Edit bot configuration |

## 🛒 Shop Items

| Item | Description | Cost |
|------|-------------|------|
| Silver | Safe investment when bank is full | 1,000 |
| Gold | High-value safe investment | 10,000 |
| Shovel | Required for digging | 1,000 |
| Bow | Required for hunting | 1,000 |

## 🔨 Craftable Items

| Item | Ingredients | Sell Value |
|------|-------------|------------|
| Joint | 1x Roll + 1x Weed | 10,000 |
| Poo | 3x Charcoal + 1x Sulphur | 2,000 |
| C4 | 2x Sulphur + 1x Charcoal + 1x Clock + 5x Potato + 2x Electronics | 25,000 |
| Excalibur | 2x Gun + 1x Mythical Sword | 35,000 |
| M4A1 | 2x Gun + 1x Stick | 30,000 |
| 8 Incher | 1x Stick + 1x David's 4th Ball | 40,000 |
| Complete Gauntlet | 1x Infinity Gauntlet + 1x Legendary Sword + 1x David's 4th Ball | 60,000 |
| Glitch | 2x God | 50,000,000 |

## 💎 Findable Items (Cosmetics)

Found through `dig`, `hunt`, and `scrap` commands.

| Item | Sell Value | Drop Chance |
|------|------------|-------------|
| God | 15,000,000 | 0.1% |
| Mythical Sword | 12,500 | 5% |
| Infinity Gauntlet | 30,000 | 5% |
| David's 4th Ball | 25,000 | 7% |
| Stick | 15,000 | 15% |
| Legendary Sword | 5,000 | 15% |
| Glock-18 | 8,000 | 19% |
| Bow | 1,000 | 20% |
| Shovel | 1,000 | 23% |
| Rare Sword | 2,500 | 25% |
| Weed | 5,000 | 30% |
| Alarm Clock | 700 | 30% |
| Roll | 1,500 | 33% |
| Sulphur | 500 | 40% |
| Charcoal | 300 | 50% |
| Potato | 100 | 65% |

## 📁 Project Structure

```
Echo/
├── cogs/                  # Command modules (Cogs)
│   ├── economy/          # Economy system
│   ├── blackjack.py      # Blackjack game
│   ├── slots.py          # Slot machine
│   ├── farming.py        # Farming system
│   ├── crafting.py       # Crafting system
│   ├── moderation.py     # Moderation commands
│   ├── fun.py            # Fun commands
│   └── help.py           # Help system
├── utils/                # Utility modules
│   ├── constants.py      # Configuration constants
│   ├── utilities.py      # Helper functions
│   └── eco_support.py    # Economy support functions
├── data/                 # SQLite databases
├── assets/              # Card images and assets
├── docs/                # Documentation
├── config.json          # Bot configuration
├── main.py             # Entry point
└── requirements.txt    # Python dependencies

```

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## 📚 Documentation

- [Architecture Guide](docs/ARCHITECTURE.md) - System design and implementation details
- [API Reference](docs/API.md) - Complete command reference

## ⚠️ Security Note

- **Never commit `config.json` with your bot token!**
- Keep your bot token secret
- Use environment variables in production
- The `config.json` file is gitignored by default

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [discord.py](https://github.com/Rapptz/discord.py)
- Card images for Blackjack game
- Community contributors

---

<div align="center">
  Made with ❤️ by mal023
</div>
