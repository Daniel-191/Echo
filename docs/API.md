# Echo Bot Command Reference

Complete reference for all commands available in Echo bot.

**Default Prefix:** `.`

---

## 📋 Table of Contents

- [Economy Commands](#economy-commands)
- [Earning Commands](#earning-commands)
- [Gambling Commands](#gambling-commands)
- [Farming Commands](#farming-commands)
- [Crafting Commands](#crafting-commands)
- [Game Commands](#game-commands)
- [Fun Commands](#fun-commands)
- [Moderation Commands](#moderation-commands)
- [Help Commands](#help-commands)
- [Admin Commands](#admin-commands)

---

## Economy Commands

### Inventory & Shopping

#### `.inventory [user]`
**Aliases:** `.inv`

View your or another user's inventory.

**Parameters:**
- `user` (optional): User to view inventory for

**Examples:**
```
.inventory
.inv @Username
```

---

#### `.buy <item> [amount]`

Buy items from the shop.

**Parameters:**
- `item` (required): Item name to purchase
- `amount` (optional): Quantity to buy (default: 1)

**Examples:**
```
.buy shovel
.buy gold 5
```

**Available Items:**
| Item | Cost | Description |
|------|------|-------------|
| Silver | 1,000 | Safe investment |
| Gold | 10,000 | Store excess money |
| Shovel | 1,000 | Required for digging |
| Bow | 1,000 | Required for hunting |

---

#### `.sell <item> [amount]`

Sell items from your inventory.

**Parameters:**
- `item` (required): Item name to sell
- `amount` (optional): Quantity to sell (default: 1)

**Examples:**
```
.sell sword
.sell potato 10
```

---

#### `.trade <user> <item>`

Trade an item to another user.

**Parameters:**
- `user` (required): User to trade with
- `item` (required): Item to give

**Examples:**
```
.trade @Friend gun
```

**Note:** Trades are one-way. This gives the item to the target user.

---

### Money Management

#### `.balance [user]`
**Aliases:** `.bal`

View your or another user's balance.

**Parameters:**
- `user` (optional): User to check balance for

**Examples:**
```
.balance
.bal @Username
```

**Response:**
- On Hand: Credits in pocket
- Bank Balance: Credits in bank (max: 500,000)

---

#### `.networth [user]`
**Aliases:** `.character`, `.net`, `.worth`

View total net worth including inventory value.

**Parameters:**
- `user` (optional): User to check net worth for

**Examples:**
```
.networth
.character @Username
```

**Includes:**
- Pocket money
- Bank balance
- Inventory value

---

#### `.baltop`
**Aliases:** `.top`, `.balancetop`

View server's richest players leaderboard.

**Examples:**
```
.baltop
```

**Shows:**
- Top 10 richest players
- Your current rank

---

#### `.pay <user> <amount>`

Send credits to another user.

**Parameters:**
- `user` (required): User to pay
- `amount` (required): Amount to send

**Examples:**
```
.pay @Friend 1000
```

**Requirements:**
- Must have sufficient balance
- Cannot pay yourself

---

#### `.deposit <amount>`

Deposit credits into your bank.

**Parameters:**
- `amount` (required): Amount to deposit (or "all"/"max")

**Examples:**
```
.deposit 5000
.deposit all
.deposit max
```

**Bank Features:**
- Max capacity: 500,000 credits
- Earns 10% interest daily
- Protected from robberies

---

#### `.withdraw <amount>`

Withdraw credits from your bank.

**Parameters:**
- `amount` (required): Amount to withdraw (or "all"/"max")

**Examples:**
```
.withdraw 1000
.withdraw max
```

---

## Earning Commands

### `.dig`

Dig for items and credits (requires shovel).

**Cooldown:** 1 minute
**Requirements:** Shovel in inventory

**Rewards:**
- Random item (based on rarity)
- 1,000 - 1,600 credits

**Examples:**
```
.dig
```

---

### `.hunt`

Hunt animals for items and credits (requires bow).

**Cooldown:** 1 minute
**Requirements:** Bow in inventory

**Rewards:**
- Random item (based on rarity)
- 600 - 1,300 credits

**Examples:**
```
.hunt
```

---

### `.scrap`
**Aliases:** `.scavenge`, `.scav`

Scavenge for items and credits.

**Cooldown:** 1 minute
**Requirements:** None

**Rewards:**
- Random item (based on rarity)
- 400 - 800 credits

**Examples:**
```
.scrap
.scavenge
```

---

### `.beg`

Beg for credits.

**Cooldown:** 15 seconds
**Requirements:** None

**Rewards:**
- 100 - 200 credits

**Examples:**
```
.beg
```

---

### `.daily`

Claim your daily reward.

**Cooldown:** 24 hours
**Requirements:** None

**Rewards:**
- 15,000 credits

**Examples:**
```
.daily
```

---

## Gambling Commands

### `.gamble <amount>`
**Aliases:** `.g`

Gamble your credits (33% win chance).

**Parameters:**
- `amount` (required): Amount to gamble (or "max")

**Max Bet:** 500,000 credits
**Win Chance:** 33% (1/3)

**Examples:**
```
.gamble 1000
.g max
```

**Outcome:**
- Win: Double your bet
- Lose: Lose your bet

---

### `.rob <user>`

Attempt to rob another user.

**Parameters:**
- `user` (required): User to rob

**Cooldown:** 1 hour
**Success Rate:** 45%
**Amount:** 20% of target's balance

**Examples:**
```
.rob @Target
```

**Outcome:**
- Success: Steal 20% of their balance
- Failure: Lose 20% of your balance

**Requirements:**
- Target must have money
- You must have enough to cover potential loss

---

## Farming Commands

### `.plant <amount>`
**Aliases:** `.crop`, `.carrots`

Plant crops to harvest later.

**Parameters:**
- `amount` (required): Number of crops to plant

**Cost:** 100 credits per crop
**Max Plants:** 1,000
**Growth Time:** 12 hours

**Examples:**
```
.plant 100
.carrots 500
```

---

### `.harvest`
**Aliases:** `.har`

Harvest your grown crops.

**Examples:**
```
.harvest
```

**Rewards:**
- 125 credits per crop
- Profit: 25 credits per crop

**Status:**
- Shows growth percentage if not ready
- Harvests and pays if ready

---

## Crafting Commands

### `.recipes`

View all available crafting recipes.

**Examples:**
```
.recipes
```

**Shows:**
- All craftable items
- Required ingredients
- Sell prices
- 🎉 indicator if you have materials

---

### `.craft <item>`

Craft an item from a recipe.

**Parameters:**
- `item` (required): Item to craft

**Examples:**
```
.craft joint
.craft c4
```

**Available Recipes:**

| Item | Ingredients | Value |
|------|-------------|-------|
| Joint | 1x Roll, 1x Weed | 10,000 |
| C4 | 2x Sulphur, 1x Charcoal, 1x Clock, 5x Potato, 2x Electronics | 25,000 |
| Excalibur | 2x Gun, 1x Mythical Sword | 35,000 |
| M4A1 | 2x Gun, 1x Stick | 30,000 |
| 8 Incher | 1x Stick, 1x David's 4th Ball | 40,000 |
| Complete Gauntlet | 1x Infinity Gauntlet, 1x Legendary Sword, 1x David's 4th Ball | 60,000 |
| Poo | 3x Charcoal, 1x Sulphur | 2,000 |
| Glitch | 2x God | 50,000,000 |

---

## Game Commands

### `.blackjack [bet]`

Play blackjack against the dealer.

**Parameters:**
- `bet` (optional): Amount to bet

**Examples:**
```
.blackjack
.blackjack 1000
```

**Rules:**
- Try to get closer to 21 than dealer
- Aces count as 1 or 11
- Face cards count as 10
- Interactive buttons: Hit, Stand, Double Down

---

### `.slots [bet]`

Play the slot machine.

**Parameters:**
- `bet` (optional): Amount to bet

**Examples:**
```
.slots
.slots 500
```

**Features:**
- Animated GIF
- 25% win rate
- Various payout multipliers

---

### `.shoot [user]`

Shoot someone with a gun (for fun).

**Parameters:**
- `user` (optional): User to shoot

**Requirements:**
- Gun or M4A1 in inventory

**Examples:**
```
.shoot @Target
.shoot
```

**Note:** This is cosmetic only - no actual effects!

---

### `.bomb [user]`

Bomb someone with C4 (for fun).

**Parameters:**
- `user` (optional): User to bomb

**Requirements:**
- C4 in inventory

**Examples:**
```
.bomb @Target
```

**Note:** This is cosmetic only - no actual effects!

---

## Fun Commands

### `.ping`

Check bot latency.

**Examples:**
```
.ping
```

---

### `.invite`

Get bot invite link.

**Examples:**
```
.invite
```

---

### `.server_info`

View server information.

**Examples:**
```
.server_info
```

---

### `.user_info [user]`

View user information.

**Parameters:**
- `user` (optional): User to view info for

**Examples:**
```
.user_info
.user_info @Username
```

---

### `.avatar [user]`

Get user's avatar.

**Parameters:**
- `user` (optional): User to get avatar for

**Examples:**
```
.avatar
.avatar @Username
```

---

### `.coinflip`

Flip a coin.

**Examples:**
```
.coinflip
```

---

### `.dice [sides]`

Roll a dice.

**Parameters:**
- `sides` (optional): Number of sides (default: 6)

**Examples:**
```
.dice
.dice 20
```

---

### `.8ball <question>`

Ask the magic 8ball a question.

**Parameters:**
- `question` (required): Question to ask

**Examples:**
```
.8ball Will I be rich?
```

---

### `.qr <text>`

Generate a QR code.

**Parameters:**
- `text` (required): Text to encode

**Examples:**
```
.qr https://discord.com
```

---

### `.calculator <expression>`

Calculate a math expression.

**Parameters:**
- `expression` (required): Math expression

**Examples:**
```
.calculator 2 + 2
.calculator 5 * (3 + 2)
```

⚠️ **Security Note:** Currently uses `eval()` - DO NOT USE WITH UNTRUSTED INPUT

---

### `.joke`

Get a random joke.

**Examples:**
```
.joke
```

---

### `.say <message>`

Make the bot say something.

**Parameters:**
- `message` (required): Message to say

**Examples:**
```
.say Hello World!
```

---

### `.membercount`

Show server member count.

**Examples:**
```
.membercount
```

---

## Moderation Commands

### `.kick <user> [reason]`

Kick a user from the server.

**Parameters:**
- `user` (required): User to kick
- `reason` (optional): Reason for kick

**Permissions:** Kick Members

**Examples:**
```
.kick @BadUser
.kick @BadUser Spamming
```

---

### `.ban <user> [reason]`

Ban a user from the server.

**Parameters:**
- `user` (required): User to ban
- `reason` (optional): Reason for ban

**Permissions:** Ban Members

**Examples:**
```
.ban @BadUser
.ban @BadUser Breaking rules
```

---

### `.mute <user> [duration]`

Mute a user (timeout).

**Parameters:**
- `user` (required): User to mute
- `duration` (optional): Duration (e.g., "10m", "1h")

**Permissions:** Moderate Members

**Examples:**
```
.mute @User
.mute @User 10m
.mute @User 1h
```

---

### `.unmute <user>`

Unmute a user.

**Parameters:**
- `user` (required): User to unmute

**Permissions:** Moderate Members

**Examples:**
```
.unmute @User
```

---

### `.clear <amount>`

Clear messages from channel.

**Parameters:**
- `amount` (required): Number of messages to clear (max: 100)

**Permissions:** Manage Messages

**Examples:**
```
.clear 10
.clear 50
```

---

### `.lock_channel [channel]`

Lock a channel (prevent sending messages).

**Parameters:**
- `channel` (optional): Channel to lock (default: current)

**Permissions:** Manage Channels

**Examples:**
```
.lock_channel
.lock_channel #general
```

---

### `.unlock_channel [channel]`

Unlock a channel.

**Parameters:**
- `channel` (optional): Channel to unlock (default: current)

**Permissions:** Manage Channels

**Examples:**
```
.unlock_channel
.unlock_channel #general
```

---

### `.lock_server`

Lock entire server.

**Permissions:** Administrator

**Examples:**
```
.lock_server
```

---

### `.unlock_server`

Unlock entire server.

**Permissions:** Administrator

**Examples:**
```
.unlock_server
```

---

## Help Commands

### `.help [category]`

View bot help and command list.

**Parameters:**
- `category` (optional): Help category

**Examples:**
```
.help
.help economy
.help moderation
```

---

### `.tutorial`

View bot tutorial.

**Examples:**
```
.tutorial
```

---

## Admin Commands

⚠️ **Requires Admin ID** in config.json

### `.give <user> <amount>`

Give credits to a user.

**Parameters:**
- `user` (required): User to give credits to
- `amount` (required): Amount to give

**Examples:**
```
.give @User 10000
```

---

### `.add_item <user> <item> [amount]`

Add items to user's inventory.

**Parameters:**
- `user` (required): Target user
- `item` (required): Item to add
- `amount` (optional): Quantity (default: 1)

**Examples:**
```
.add_item @User gun
.add_item @User gold 5
```

---

### `.remove_item <user> <item> [amount]`

Remove items from user's inventory.

**Parameters:**
- `user` (required): Target user
- `item` (required): Item to remove
- `amount` (optional): Quantity (default: 1)

**Examples:**
```
.remove_item @User sword
.remove_item @User potato 10
```

---

### `.cool_bypass`

Clear all cooldowns.

**Examples:**
```
.cool_bypass
```

**Note:** Does not clear interest or farming cooldowns.

---

## Item Rarity & Drop Rates

### Common Items (High Drop Rate)
- Potato (65%)
- Charcoal (50%)
- Sulphur (40%)

### Uncommon Items
- Roll (33%)
- Clock (30%)
- Weed (30%)
- Electronics (25%)
- Shovel (23%)

### Rare Items
- Bow (20%)
- Gun (19%)
- Stick (15%)
- Rare Sword (25%)

### Legendary Items
- Legendary Sword (15%)
- David's 4th Ball (7%)
- Mythical Sword (5%)
- Infinity Gauntlet (5%)

### Mythical Items
- God (0.1%) - Rarest item!

---

## Cooldown Reference

| Command | Cooldown |
|---------|----------|
| `.dig` | 1 minute |
| `.hunt` | 1 minute |
| `.scrap` | 1 minute |
| `.beg` | 15 seconds |
| `.daily` | 24 hours |
| `.rob` | 1 hour |
| `.plant` | 12 hours (growth time) |

---

## Tips & Tricks

1. **Use the bank!** - Protects money from robberies
2. **Plant carrots** - Passive income while you wait
3. **Craft items** - Sell for higher profit
4. **Daily reward** - Don't forget to claim!
5. **Dig/Hunt** - Requires tools but better rewards
6. **Save rare items** - Use for crafting valuable items

---

**Last Updated:** 28-11-2025