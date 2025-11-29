# 💬 Echo Bot Commands

Complete command reference for Echo Bot.

**Default Prefix:** `.`

---

## 🎮 General Commands

**Get help and information**

- `.help` - Display all available commands
- `.ping` - Check bot latency and response time
- `.avatar [@user]` - Display a user's avatar image
- `.serverinfo` - Show detailed server information
- `.userinfo [@user]` - Display user profile information
- `.membercount` - Show total server member count

**Fun & Utilities**

- `.quote` - Get an inspiring daily quote
- `.joke` - Get a random joke
- `.8ball <question>` - Ask the magic 8-ball a question
- `.coinflip <heads/tails>` - Flip a coin
- `.dice` - Roll a six-sided dice
- `.qr <text/link>` - Generate a QR code from text or URL
- `.calculator <expression>` - Perform mathematical calculations

---

## 💰 Economy Commands

**Balance & Wealth**

- `.balance [@user]` - Check wallet and bank balance
- `.networth [@user]` - View total net worth including items
- `.baltop` - View the richest players leaderboard

**Money Management**

- `.daily` - Claim daily reward (15,000 credits)
- `.pay <@user> <amount>` - Transfer money to another user
- `.deposit <amount/max>` - Deposit money into bank (earns 10% daily interest)
- `.withdraw <amount/max>` - Withdraw money from bank

---

## 🎯 Earning Commands

**Make money through activities**

- `.beg` - Beg for money
  - Cooldown: 15 seconds
  - Earnings: 100-200 credits

- `.dig` - Dig for treasure and items
  - Requires: Shovel (buy from shop)
  - Cooldown: 1 minute
  - Earnings: 1,000-1,600 credits + random items

- `.hunt` - Hunt animals for items
  - Requires: Bow (buy from shop)
  - Cooldown: 1 minute
  - Earnings: 600-1,300 credits + random items

- `.scrap` - Scavenge for items
  - Cooldown: 1 minute
  - Earnings: 400-800 credits + random items

---

## 🎲 Gambling Commands

**Risk your money for big rewards**

- `.gamble <amount>` - Gamble your credits
  - Win Chance: 33%
  - Win: 2x your bet
  - Lose: Lose your bet

- `.rob <@user>` - Attempt to rob another player
  - Success Rate: 45%
  - Success: Steal 20% of their balance
  - Fail: Lose credits as penalty
  - Cooldown: 5 minutes

- `.blackjack <amount>` - Play blackjack with interactive cards
  - Beat the dealer to win 2x your bet
  - Interactive UI with hit/stand buttons

- `.slots <amount>` - Play the slot machine
  - Win Chance: 25%
  - Various multipliers based on matches
  - Cooldown: 3 seconds

---

## 🛒 Shop & Inventory

**Manage your items**

- `.shop` - View all items available for purchase
- `.buy <item>` - Purchase an item from the shop
- `.sell <item>` - Sell an item from your inventory
- `.inventory [@user]` - View inventory contents
- `.trade <@user> <item>` - Give an item to another player
- `.cosmetics` - View all findable cosmetic items and their values

---

## 🌾 Farming Commands

**Plant and harvest crops**

- `.plant <amount/max>` - Plant carrots
  - Cost: 100 credits per carrot
  - Sell Price: 125 credits per carrot
  - Profit: 25% after 12 hours
  - Growth Time: 12 hours
  - Max: 1,000 carrots at once

- `.harvest` - Harvest grown crops
  - Automatically sells harvested carrots
  - Receive 125 credits per carrot

---

## 🔨 Crafting Commands

**Combine items to create valuable goods**

- `.recipes` - View all craftable items and required materials
- `.craft <item>` - Craft an item using materials from your inventory

See [ITEMS.md](ITEMS.md#craftable-items) for the complete list of craftable items.

---

## 🎮 Action Commands

**Use items on other players**

- `.shoot <@user>` - Shoot someone
  - Requires: Gun or M4A1 in inventory
  - Fun command with no real effect

- `.bomb <@user>` - Bomb someone
  - Requires: C4 in inventory
  - Fun command with no real effect

---

## 🛡️ Moderation Commands

> **Permission Required:** Administrator or Moderator role

**User Management**

- `.kick <@user> [reason]` - Kick a member from the server
- `.ban <@user> [reason]` - Ban a member from the server
- `.mute <@user> [reason]` - Mute a member (prevents them from speaking)
- `.unmute <@user>` - Unmute a previously muted member

**Channel Management**

- `.clear <amount>` - Delete multiple messages in bulk (1-100)
- `.lockchannel [duration]` - Lock a channel temporarily
  - Optional: Specify duration (e.g., "1h", "30m")
  - Prevents non-moderators from sending messages
- `.unlockchannel` - Unlock a previously locked channel

**Server Management**

- `.lockserver [duration]` - Lock the entire server
  - Locks all channels at once
  - Optional: Specify duration
- `.unlockserver` - Unlock the entire server

---

## ⚙️ Admin Commands

> **Permission Required:** Bot owner only (requires ADMIN_ID in config.json)

**Economy Management**

- `.give <@user> <amount>` - Give credits to a user
- `.additem <@user> <item>` - Add an item to user's inventory
- `.removeitem <@user> <item>` - Remove an item from user's inventory

**Bot Configuration**

- `.config_view` - View current bot configuration from Discord
- `.config_edit <key> <value>` - Edit bot configuration from Discord
  - Modifies config.json directly
  - Changes take effect immediately

---

## 📊 Cooldowns Reference

| Command | Cooldown |
|---------|----------|
| `.beg` | 15 seconds |
| `.dig` | 1 minute |
| `.hunt` | 1 minute |
| `.scrap` | 1 minute |
| `.rob` | 5 minutes |
| `.slots` | 3 seconds |
| `.daily` | 24 hours |

---

## 💡 Tips

- Use `.help` in Discord to see all available commands
- Commands are case-insensitive (`.help` = `.HELP` = `.Help`)
- You can use command aliases when available
- Type `.help <command>` for detailed help on a specific command

---

[← Back to README](../README.md) | [View Items & Economy →](ITEMS.md)
