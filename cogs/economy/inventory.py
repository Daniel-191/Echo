"""
Inventory management commands for the economy system.
Handles buying, selling, trading, and viewing inventories.
"""

from discord.ext import commands
import discord
from collections import Counter
from utils.utilities import *
from utils.eco_support import *
from utils.constants import COLOR_SUCCESS, COLOR_ERROR, FOOTER_HELP, DB_COOLDOWNS


class InventoryCommands(commands.Cog):
    """Commands for managing user inventories."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['inv'])
    async def inventory(self, ctx, user: commands.MemberConverter = None):
        """View a user's inventory."""
        try:
            if user is None:
                user_id = ctx.author.id
                inventory = get_user_inventory(user_id)
                item_counts = Counter(inventory)
                embed_title = f"{ctx.author.display_name}'s Inventory"
            else:
                user_id = user.id
                inventory = get_user_inventory(user_id)
                item_counts = Counter(inventory)
                embed_title = f"{user.display_name}'s Inventory"

            embed = discord.Embed(title=embed_title, color=COLOR_INFO)
            embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))

            for item, count in item_counts.items():
                embed.add_field(name=item, value=f"Count: {count}", inline=True)

            await ctx.send(embed=embed)

        except Exception as e:
            print(f"Error in inventory command: {e}")

    @commands.command()
    async def buy(self, ctx, item_name: str = None, amount: int = 1):
        """Buy items from the shop."""
        try:
            if item_name is None:
                embed = discord.Embed(
                    title="Incorrect Buy Usage",
                    description=f"{ctx.author.mention}, Please specify an item name. Usage: `{prefix}buy <item_name> <amount>`",
                    color=COLOR_ERROR
                )
                embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
                await ctx.send(embed=embed)
                return

            item_name = item_name.lower()

            if item_name not in shop_items:
                embed = discord.Embed(
                    title="Item Not Found",
                    description=f"{ctx.author.mention}, Item not found in the shop.",
                    color=COLOR_ERROR
                )
                embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
                await ctx.send(embed=embed)
                return

            user = ctx.author
            item_cost = shop_items[item_name]['cost']
            user_balance = get_user_balance(user.id)
            total = amount * item_cost

            if user_balance < total:
                embed = discord.Embed(
                    title="Insufficient Funds",
                    description=f"{ctx.author.mention}, You don't have enough credits to buy this item.",
                    color=COLOR_ERROR
                )
                embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
                await ctx.send(embed=embed)
                return

            update_user_balance(user.id, -total)

            for _ in range(amount):
                add_item_to_inventory(user.id, item_name)

            log_purchase(user.id, amount, user.name, item_name, item_cost)

            embed = discord.Embed(
                title="Purchase Successful",
                description=f"{ctx.author.mention}, You have successfully bought **{item_name}** for **{total} credits**.",
                color=COLOR_SUCCESS
            )
            embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
            await ctx.send(embed=embed)

        except Exception as e:
            print(f"An error occurred: {e}")
            embed = discord.Embed(
                title="Error",
                description=f"An error occurred while processing your request. Please try again later.",
                color=COLOR_ERROR
            )
            embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
            await ctx.send(embed=embed)

    @commands.command()
    async def sell(self, ctx, item_id: str=None, amount: int=1):
        """Sell items from your inventory."""
        user_id = ctx.author.id
        user_inventory = get_user_inventory(user_id)

        try:
            if item_id is None:
                embed = discord.Embed(
                    title="Incorrect Usage",
                    description=f"{ctx.author.mention}, Incorrect usage. Please use: `{prefix}sell <item> <amount>`",
                    color=embed_error
                )
                embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
                await ctx.send(embed=embed)
                return

            if item_id not in user_inventory:
                embed = discord.Embed(
                    title="Item Not Found",
                    description=f"{ctx.author.mention}, You don't have this in your inventory.",
                    color=embed_error
                )
                embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
                await ctx.send(embed=embed)
                return

            item_count = sum(item == item_id for item in user_inventory)
            if item_count < amount:
                embed = discord.Embed(
                    title=f"Insufficient {item_id}",
                    description=f"{ctx.author.mention}, You only have {item_count} {item_id}'s, which is less than the requested amount of {amount}.",
                    color=embed_error
                )
                await ctx.send(embed=embed)
                return

            item_id = item_id.lower()
            user = await self.bot.fetch_user(ctx.author.id)

            special_shop_items = ["gold", "silver"]

            if item_id in special_shop_items:
                item_info = shop_items[item_id]
                item_sell_price = item_info["cost"] * amount
            else:
                item_info = combined_items[item_id]
                item_sell_price = item_info["sell"] * amount

            if item_id not in combined_items and item_id not in shop_items:
                embed = discord.Embed(
                    title="Invalid Item ID",
                    description=f"{ctx.author.mention}, That Item ID is invalid/does not exist.",
                    color=embed_error
                )
                embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
                await ctx.send(embed=embed)
                return

            update_user_balance(user_id, item_sell_price)

            for i in range(0, amount):
                remove_item_from_inventory(user_id, item_id)

            log_purchase(user_id, 0, user.name, item_id, item_sell_price)

            embed = discord.Embed(
                title="Item Sold",
                description=f"{ctx.author.mention}, You sold **{amount} {item_id} for 💵 {item_sell_price} credits**. Your new balance is: 💵 **{get_user_balance(user_id)} credits**!",
                color=COLOR_SUCCESS
            )
            embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
            await ctx.send(embed=embed)
        except Exception as e:
            print(e)

    @commands.command()
    async def trade(self, ctx, user: commands.MemberConverter=None, item_name: str=None):
        """Trade an item to another user."""
        user_id = ctx.author.id

        if user is None:
            embed = discord.Embed(
                title="Incorrect usage",
                description=f"{ctx.author.mention}, Incorrect usage. Please use: `{prefix}trade <@user> <item2give>`",
                color=embed_error
            )
            embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
            await ctx.send(embed=embed)
            return

        if item_name is None:
            embed = discord.Embed(
                title="Incorrect usage",
                description=f"{ctx.author.mention}, Incorrect usage. Please use: `{prefix}trade <@user> <item2give>`",
                color=embed_error
            )
            embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
            await ctx.send(embed=embed)
            return

        user_inventory = get_user_inventory(user_id)

        if item_name not in user_inventory:
            embed = discord.Embed(
                title="Item not found",
                description=f"{ctx.author.mention}, You **dont have {item_name}** in your inventory!",
                color=embed_error
            )
            embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
            await ctx.send(embed=embed)
            return

        add_item_to_inventory(user.id, item_name)
        remove_item_from_inventory(user_id, item_name)

        embed = discord.Embed(
            title="Trade successfull",
            description=f"{ctx.author.mention}, You have **given {item_name} to {user}**!",
            color=COLOR_SUCCESS,
        )
        embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
        await ctx.send(embed=embed)

    # Admin Commands
    @commands.command()
    @commands.check(is_admin)
    async def give(self, ctx, user: commands.MemberConverter, amount: int):
        """[ADMIN] Give credits to a user."""
        update_user_balance(user.id, amount)
        embed = discord.Embed(
            title="Credits Given!",
            description=f"Admin {ctx.author.display_name} has given **{amount} credits** to {user.display_name}.",
            color=COLOR_SUCCESS
        )
        embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
        await ctx.send(embed=embed)

    @give.error
    async def give_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(
                title="Permission Denied",
                description=f"{ctx.author.mention}, You don't have permission to use this command.",
                color=embed_error
            )
            embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
            await ctx.send(embed=embed)

    @commands.command()
    @commands.check(is_admin)
    async def remove_item(self, ctx, user: commands.MemberConverter, item: str, amount=1):
        """[ADMIN] Remove items from a user's inventory."""
        embed = discord.Embed(
            title="Item Removal success",
            description=f"{ctx.author.mention}, I have successfully removed **{amount} {item}'s from {user.mention}'s** inventory.",
            color=COLOR_SUCCESS
        )
        embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
        await ctx.send(embed=embed)

        for i in range(0, amount):
            remove_item_from_inventory(user.id, item)

    @remove_item.error
    async def remove_item_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(
                title="Permission Denied",
                description=f"{ctx.author.mention}, You don't have permission to use this command.",
                color=embed_error
            )
            embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
            await ctx.send(embed=embed)

    @commands.command()
    @commands.check(is_admin)
    async def add_item(self, ctx, user: commands.MemberConverter, item: str, amount=1):
        """[ADMIN] Add items to a user's inventory."""
        embed = discord.Embed(
            title="Item Add success",
            description=f"{ctx.author.mention}, I have successfully Added **{amount} {item}'s to {user.mention}'s** inventory.",
            color=COLOR_SUCCESS
        )
        embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
        await ctx.send(embed=embed)

        for i in range(0, amount):
            add_item_to_inventory(user.id, item)

    @add_item.error
    async def add_item_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(
                title="Permission Denied",
                description=f"{ctx.author.mention}, You don't have permission to use this command.",
                color=embed_error
            )
            embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
            await ctx.send(embed=embed)

    @commands.command()
    @commands.check(is_admin)
    async def cool_bypass(self, ctx):
        """[ADMIN] Clear all cooldowns."""
        conn = sqlite3.connect(DB_COOLDOWNS)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cooldowns WHERE type != 'interest' AND type != 'farming'")
        conn.commit()
        conn.close()

        embed = discord.Embed(
            title="Cooldowns Wiped",
            description=f"Admin {ctx.author.display_name} has just wiped all cooldowns! (except for interest on banks and farming)",
            color=COLOR_SUCCESS
        )
        embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
        await ctx.send(embed=embed)

    @cool_bypass.error
    async def cool_bypass_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(
                title="Permission Denied",
                description=f"{ctx.author.mention}, You don't have permission to use this command.",
                color=embed_error
            )
            embed.set_footer(text=FOOTER_HELP.format(prefix=prefix))
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(InventoryCommands(bot))
