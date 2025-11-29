<div align="center">
  <img src="https://github.com/Daniel-191/Echo/blob/main/images/bot_icon.png" alt="Echo Bot Image" width="400">
</div>

<h1 align="center">
  <br>
  Echo Bot v6
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

<h2 align="center">
  <br>
  DEPRECATED - NO LONGER MAINTAINED
  <br>
</h2>

<br>

## 📦 Prerequisites

- [Python 3.12+](https://www.python.org/downloads/release/python-3120/)
- [Git](https://git-scm.com/downloads)
- A Discord Bot Token ([Create one here](https://discord.com/developers/applications))

## 🚀 Installation

### Quick Start

```bash
# Clone the repository
git clone https://github.com/Daniel-191/Echo
cd Echo

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Configure config.json with your bot token, then run
python main.py
```

---

### Detailed Setup Guide

<details>
<summary><b>Step 1: Clone Repository</b></summary>

<br>

```bash
git clone https://github.com/Daniel-191/Echo
cd Echo
```
</details>

<details>
<summary><b>Step 2: Create Virtual Environment</b></summary>

<br>

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```
</details>

<details>
<summary><b>Step 3: Install Dependencies</b></summary>

<br>

```bash
pip install -r requirements.txt
```
</details>

<details>
<summary><b>Step 4: Configure Bot</b></summary>

<br>

Edit `config.json` with your settings:

**Required:**
- `TOKEN` - Your Discord bot token

**Optional:**
- `ADMIN_ID` - Your Discord user ID (for admin commands)
- `bot_invite_link` - Bot invite URL

**Get Bot Token:**
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create/select application → Bot section
3. Click "Reset Token" → Copy token

**Get User ID:**
1. Enable Developer Mode (Discord Settings → Advanced)
2. Right-click your username → Copy User ID
</details>

<details>
<summary><b>Step 5: Run the Bot</b></summary>

<br>

```bash
python main.py
```

</details>

## 💬 Commands & Economy

> **Default Prefix:** `.`

Echo Bot has tons of commands across economy, games, moderation, and fun categories.

### 📖 Full Documentation

For complete command details, cooldowns, and usage examples:

**→ [View All Commands](docs/COMMANDS.md)**

### 💎 Items & Economy

For shop items, craftable recipes, and findable items:

**→ [View Items & Economy Guide](docs/ITEMS.md)**

<details>
<summary><b>Quick Economy Overview</b></summary>

<br>

**Shop Items:**
- Shovel (1,000) - Required for `.dig`
- Bow (1,000) - Required for `.hunt`
- Silver (1,000) / Gold (10,000) - Safe investments

**Top Craftable Items:**
- Glitch - 50,000,000 credits (2x God)
- Complete Gauntlet - 60,000 credits
- Excalibur - 35,000 credits
- M4A1 - 30,000 credits

**Best Earning Methods:**
1. `.dig` - 1,000-1,600 credits/min (requires shovel)
2. `.hunt` - 600-1,300 credits/min (requires bow)
3. `.scrap` - 400-800 credits/min
4. `.daily` - 15,000 credits/day

</details>

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## 📚 Documentation

- **[Commands Reference](docs/COMMANDS.md)** - Complete list of all bot commands
- **[Items & Economy Guide](docs/ITEMS.md)** - Shop items, crafting recipes, and findable items
- **[Architecture Guide](docs/ARCHITECTURE.md)** - System design and implementation details
- **[API Reference](docs/API.md)** - Technical API documentation

---

<div align="center">
  Made with ❤️ by mal023
</div>
