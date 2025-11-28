"""
Earning and gambling game commands for the economy system.
Handles money-earning activities and gambling games.
"""

from discord.ext import commands
import discord
import random
from utilities import *
from eco_support import *


class GameCommands(commands.Cog):
    """Commands for earning money and gambling."""

    def __init__(self, bot):
        self.bot = bot

    # Earning Commands
    @commands.command()
    async def dig(self, ctx):
        """Dig for items and credits (requires shovel)."""
        user_id = ctx.author.id

        user_inventory = get_user_inventory(user_id)
        if 'shovel' not in user_inventory:
            embed = discord.Embed(
                title="You need a shovel...",
                description=f"{ctx.author.mention}, digging with your hands? We arn't animals, **go buy or find a shovel**.",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        if not can_dig(user_id):
            embed = discord.Embed(
                title="Cooldown Active",
                description=f"{ctx.author.mention}, You're on a **1min break** buddy 🤫 don't chat to me.",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        chosen_item = random.choices(list(cosmetics_items.keys()), weights=[item["chance"] for item in cosmetics_items.values()], k=1)[0]
        won_item = cosmetics_items[chosen_item]
        add_item_to_inventory(user_id, chosen_item)

        embed = discord.Embed(
            title=f"{ctx.author.display_name}, Item Found",
            description=f"🎉 You found: **{won_item['name']}**! 🎉 Check your inventory with `{prefix}inventory`.",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
        await ctx.send(embed=embed)

        amount = random.randint(1000, 1600)
        update_user_balance(ctx.author.id, amount)

        embed = discord.Embed(
            title=f"{ctx.author.display_name}, Credits Found",
            description=f"💵 You found: **{amount} credits**! Your new balance is: **{get_user_balance(ctx.author.id)} credits**.",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
        await ctx.send(embed=embed)

        update_last_action_time(user_id, "dig")

    @commands.command()
    async def hunt(self, ctx):
        """Hunt for items and credits (requires bow)."""
        user_id = ctx.author.id

        user_inventory = get_user_inventory(user_id)
        if 'bow' not in user_inventory:
            embed = discord.Embed(
                title="Find a bow first lol",
                description=f"{ctx.author.mention}, You need a **bow** too shoot arrows... **Go buy or find one.**",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        if not can_hunt(user_id):
            embed = discord.Embed(
                title="Cooldown Active",
                description=f"{ctx.author.mention}, You're on a **1min break. Go away**.",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        chosen_item = random.choices(list(cosmetics_items.keys()), weights=[item["chance"] for item in cosmetics_items.values()], k=1)[0]
        won_item = cosmetics_items[chosen_item]
        add_item_to_inventory(user_id, chosen_item)

        embed = discord.Embed(
            title=f"{ctx.author.display_name}, Item Found",
            description=f"🎉 You found: **{won_item['name']}**! 🎉 Check your inventory with `{prefix}inventory`",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
        await ctx.send(embed=embed)

        amount = random.randint(600, 1300)
        update_user_balance(ctx.author.id, amount)

        embed = discord.Embed(
            title=f"{ctx.author.display_name}, Credits Found",
            description=f"💵 You found: **{amount} credits**! Your new balance is: **{get_user_balance(ctx.author.id)} credits**.",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
        await ctx.send(embed=embed)

        update_last_action_time(user_id, "hunt")

    @commands.command(aliases=['scavenge', 'scarp', 'scav', 'scap', 'srcap'])
    async def scrap(self, ctx):
        """Scavenge for items and credits."""
        try:
            user_id = ctx.author.id

            if not can_scavenge(user_id):
                embed = discord.Embed(
                    title="Cooldown Active",
                    description=f"{ctx.author.mention}, **1min cooldown** lmao.",
                    color=embed_error
                )
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

            chosen_item = random.choices(list(cosmetics_items.keys()), weights=[item["chance"] for item in cosmetics_items.values()], k=1)[0]
            add_item_to_inventory(ctx.author.id, chosen_item)
            won_item = cosmetics_items[chosen_item]

            embed = discord.Embed(
                title=f"{ctx.author.display_name}, Item Found",
                description=f"🎉 You found: **{won_item['name']}**. 🎉 Check your inventory with `{prefix}inventory`",
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)

            amount = random.randint(400, 800)
            update_user_balance(ctx.author.id, amount)

            embed = discord.Embed(
                title=f"{ctx.author.display_name}, Credits Found",
                description=f"💵 You found: **{amount} Credits**! Your new balance is: **{get_user_balance(ctx.author.id)} credits**.",
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)

            update_last_action_time(user_id, "scavenge")
        except Exception as e:
            print(e)

    @commands.command()
    async def beg(self, ctx):
        """Beg for credits."""
        user_id = ctx.author.id

        if not can_beg(user_id):
            embed = discord.Embed(
                title="Cooldown Active",
                description=f"{ctx.author.mention}, You begged in the past **15s. Wait the cooldown**.",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        amount = random.randint(100, 200)
        update_user_balance(user_id, amount)

        embed = discord.Embed(
            title=f"{ctx.author.display_name} is begging",
            description=f'💵 A kind man gave you **{amount} credits**.',
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
        await ctx.send(embed=embed)

        update_last_action_time(user_id, "beg")

    @commands.command()
    async def daily(self, ctx):
        """Claim your daily reward."""
        user_id = ctx.author.id

        try:
            if not can_claim_daily(user_id):
                embed = discord.Embed(
                    title="Daily Reward Already Claimed",
                    description=f"{ctx.author.mention}, Nah its called **'daily' for a reason**. What are you tryna do.",
                    color=embed_error
                )
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

            update_user_balance(user_id, int(daily_reward))

            embed = discord.Embed(
                title="Daily Reward Claimed",
                description=f'{ctx.author.mention}, You have claimed your daily reward of 💵 **{daily_reward} credits**!',
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)

            set_last_claim_time(user_id)
        except Exception as e:
            print(e)

    # Gambling Commands
    @commands.command(aliases=['g'])
    async def gamble(self, ctx, amount: str = None):
        """Gamble your credits (1/3 chance to double)."""
        if amount is None:
            embed = discord.Embed(
                title="Gamble Command",
                description=f"{ctx.author.mention}, Please specify an amount to gamble. Usage: `{prefix}gamble <amount>`",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        if amount.lower() == "max":
            amount = min(get_user_balance(ctx.author.id), max_bet)
        else:
            try:
                amount = int(amount)
            except ValueError:
                embed = discord.Embed(
                    title="Invalid Input",
                    description=f"{ctx.author.mention}, Please enter a valid amount or 'max'.",
                    color=embed_error
                )
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

        if amount <= 0 or amount > get_user_balance(ctx.author.id) or amount > max_bet:
            embed = discord.Embed(
                title="Invalid Bet Amount",
                description=f"{ctx.author.mention}, Invalid bet amount. You can bet up to {max_bet} Credits.",
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        if random.choice([True, False, False]):
            update_user_balance(ctx.author.id, amount)
            result_description = f"{ctx.author.mention}, You won 💵 **{amount} credits**!"
            result_color = discord.Color.green()
        else:
            update_user_balance(ctx.author.id, -amount)
            result_description = f"{ctx.author.mention}, You lost 💵 **{amount} credits! Big L**."
            result_color = embed_error

        result_embed = discord.Embed(
            title="Gamble Result",
            description=result_description,
            color=result_color
        )
        await ctx.send(embed=result_embed)

    @commands.command()
    async def rob(self, ctx, user: commands.MemberConverter = None):
        """Rob another user (45% success rate)."""
        user_id = ctx.author.id
        target_id = user.id

        if not can_rob(user_id):
            embed = discord.Embed(
                title="Cooldown Active",
                description=f"{ctx.author.mention}, Police are on the streets right now. **Wait 1h**.",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        try:
            if user is None:
                embed = discord.Embed(
                    title="Incorrect Usage",
                    description=f"{ctx.author.mention}, Please specify the user to rob: `{prefix}rob <@user>`",
                    color=embed_error
                )
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

            if user == ctx.author:
                embed = discord.Embed(
                    title="You can't rob yourself!",
                    description=f"{ctx.author.mention}, You can't rob yourself!",
                    color=embed_error
                )
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

            user_balance = get_user_balance(user_id)
            target_balance = get_user_balance(target_id)

            amount_to_rob = int(0.2 * target_balance)

            if user_balance < amount_to_rob:
                embed = discord.Embed(
                    title="Insufficient Balance",
                    description=f"{ctx.author.mention}, You don't have enough balance to rob.",
                    color=embed_error
                )
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

            if target_balance <= 0:
                embed = discord.Embed(
                    title=f"Your target has no money!",
                    description=f"{ctx.author.mention}, Why rob a poor person! Instead, rob the rich and give to the poor.",
                    color=embed_error
                )
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

            success_chance = random.random()

            if success_chance <= 0.45:
                update_user_balance(user_id, amount_to_rob)
                update_user_balance(target_id, -amount_to_rob)

                embed = discord.Embed(
                    title="Robbery Successful",
                    description=f"You successfully robbed {amount_to_rob} from {user.mention}!",
                    color=discord.Color.green()
                )
            else:
                loss_amount = int(0.2 * user_balance)
                update_user_balance(user_id, -loss_amount)

                embed = discord.Embed(
                    title="Robbery Failed",
                    description=f"You failed to rob {user.mention} and lost {loss_amount}!",
                    color=embed_error
                )

            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)

            update_last_action_time(user_id, "rob")

        except Exception as e:
            print(e)

    # Fun Interaction Commands
    @commands.command()
    async def shoot(self, ctx, user: commands.MemberConverter=None):
        """Shoot someone (requires gun or m4a1)."""
        user_id = ctx.author.id

        user_inventory = get_user_inventory(user_id)
        if 'gun' in user_inventory:
            pass
        elif 'm4a1' in user_inventory:
            pass
        else:
            embed = discord.Embed(
                title="Unable to shoot",
                description=f"{ctx.author.mention}, You need to find a gun or craft an m4a1 to shoot people! Find a gun using `{prefix}scrap` or craft an m4a1 using `{prefix}craft m4a1` view recipes using `{prefix}recipes`!",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        if user is None:
            embed = discord.Embed(
                title="Suicide",
                description=f"{ctx.author.mention} has just shot themself!",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(
            title="Shots Fired",
            description=f"{ctx.author.mention}, Has just **shot and killed {user.mention}** in cold blood.",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
        await ctx.send(embed=embed)

    @commands.command()
    async def bomb(self, ctx, user: commands.MemberConverter=None):
        """Bomb someone (requires c4)."""
        user_id = ctx.author.id

        user_inventory = get_user_inventory(user_id)
        if 'c4' not in user_inventory:
            embed = discord.Embed(
                title="Unable to bomb",
                description=f"{ctx.author.mention}, You need C4 to blow someone up! Craft one using `{prefix}craft c4` view recipes using `{prefix}recipes`",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        if user is None:
            embed = discord.Embed(
                title="Suicide",
                description=f"{ctx.author.mention}, has just **blown up!**",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(
            title="Bombing",
            description=f"{ctx.author.mention}, has just **bombed and killed {user.mention}** with c4!",
            color=discord.Color.green(),
        )
        embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(GameCommands(bot))
