"""
Transaction and balance management commands for the economy system.
Handles payments, deposits, withdrawals, and balance viewing.
"""

from discord.ext import commands
import discord
from utilities import *
from eco_support import *


class TransactionCommands(commands.Cog):
    """Commands for managing money and viewing balances."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pay(self, ctx, user: commands.MemberConverter=None, amount: int=None):
        """Pay credits to another user."""
        if amount is None or amount <= 0:
            embed = discord.Embed(
                title="Invalid Amount",
                description=f"{ctx.author.mention}, Please specify an amount to pay. Usage: `{prefix}pay <@user> <amount>`",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        if user is None:
            embed = discord.Embed(
                title="Not a user",
                description=f"{ctx.author.mention}, Please specify a user. Usage: `{prefix}pay <@user> <amount>`",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        payer_id = str(ctx.author.id)
        user_id = str(user.id)

        if payer_id == user_id:
            embed = discord.Embed(
                title="Payment Error",
                description=f"{ctx.author.mention}, Yeah nah you cant pay yourself.",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        if amount > get_user_balance(payer_id):
            embed = discord.Embed(
                title="Broke asf :sob:",
                description=f"{ctx.author.mention}, go get some money you're way too poor buddy.",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        update_user_balance(payer_id, -amount)
        update_user_balance(user_id, amount)

        embed = discord.Embed(
            title="Payment Successful",
            description=f"{ctx.author.mention}, 💵 You just paid {user.display_name} **{amount} credits**!",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
        await ctx.send(embed=embed)

    @commands.command()
    async def deposit(self, ctx, amount=None):
        """Deposit credits into your bank."""
        if amount == 'all' or amount == 'max':
            amount = get_user_balance(ctx.author.id)
        elif amount is None:
            embed = discord.Embed(
                title="Incorrect deposit usage!",
                description=f"{ctx.author.mention}, Incorrect deposit usage, please use: `{prefix}deposit <amount>`",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return
        else:
            try:
                amount = int(amount)
            except ValueError:
                embed = discord.Embed(
                    title="Invalid deposit amount",
                    description=f"{ctx.author.mention}, Please enter a valid amount.",
                    color=embed_error
                )
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

        if amount <= 0 or amount > get_user_balance(ctx.author.id):
            embed = discord.Embed(
                title="Invalid deposit amount",
                description=f"{ctx.author.mention}, Please enter a valid amount.",
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        remaining_space = max_bank_size - get_user_bank_balance(ctx.author.id)
        amount_to_deposit = min(amount, remaining_space)

        update_user_balance(ctx.author.id, -amount_to_deposit)
        update_bank_balance(ctx.author.id, amount_to_deposit)

        embed = discord.Embed(
            title="Deposit Successful",
            description=f'{ctx.author.mention}, 💵 **{amount_to_deposit} credits** has been deposited to your sussy account.',
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
        await ctx.send(embed=embed)

    @commands.command()
    async def withdraw(self, ctx, amount=None):
        """Withdraw credits from your bank."""
        if amount is None:
            embed = discord.Embed(
                title="Incorrect withdraw usage!",
                description=f'{ctx.author.mention}, Incorrect withdraw usage. Please use: `{prefix}withdraw <amount>`',
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        if amount == 'max' or amount == 'all':
            amount = get_user_bank_balance(ctx.author.id)
        else:
            try:
                amount = int(amount)
            except ValueError:
                embed = discord.Embed(
                    title="Invalid Withdraw amount",
                    description=f"{ctx.author.mention}, Please enter a valid amount.",
                    color=embed_error
                )
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

        if amount <= 0 or amount > get_user_bank_balance(ctx.author.id):
            embed = discord.Embed(
                title="Invalid withdraw amount",
                description=f'{ctx.author.mention}, Invalid withdraw amount. Please try again.',
                color=embed_error
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
            return

        update_bank_balance(ctx.author.id, -amount)
        update_user_balance(ctx.author.id, amount)

        embed = discord.Embed(
            title="Withdraw Successful",
            description=f'{ctx.author.mention}, 💵 **{amount} credits** have been withdrawn from your sussy account.',
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
        await ctx.send(embed=embed)

    @commands.command(aliases=['bal'])
    async def balance(self, ctx, user: commands.MemberConverter=None):
        """View your or another user's balance."""
        try:
            user = user or ctx.author
            user_id = user.id

            pocket_money = get_user_balance(user_id)
            bank_balance = get_user_bank_balance(user_id)

            embed = discord.Embed(
                title=f"**{user.display_name}'s** Balance",
                description=f'On Hand: **{pocket_money} credits**\nBank Balance: **{bank_balance}/{max_bank_size} credits**',
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
            print(e)

    @commands.command(aliases=['networth', 'net', 'worth', 'netowrth', 'netwoth'])
    async def character(self, ctx, user: commands.MemberConverter=None):
        """View total networth including inventory value."""
        try:
            user = user or ctx.author

            pocket_money = get_user_balance(user.id)
            bank_balance = get_user_bank_balance(user.id)
            user_inventory = get_user_inventory(user.id)

            total_inventory_value = sum(combined_items[item_id]["sell"] if item_id in combined_items else shop_items[item_id]["cost"] for item_id in user_inventory)

            total_balance = pocket_money + bank_balance + total_inventory_value

            embed = discord.Embed(
                title=f"💰 {user.display_name}'s Balance 💰",
                description=f'💼 Wallet: **{pocket_money} credits**💼\n🏦 Bank Account: **{bank_balance}/{max_bank_size} credits**🏦\n\n🛍️ Assets: **{total_inventory_value}** credits🛍️',
                color=discord.Color.green()
            )

            embed.set_thumbnail(url=user.avatar.url if user.avatar else user.default_avatar_url)

            embed.add_field(name="💰 NETWORTH 💰", value=f"**{total_balance}** credits", inline=False)

            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(e)
            print(e)

    @commands.command(aliases=['top', 'balancetop', 'balance_top'])
    async def baltop(self, ctx):
        """View the server's richest players."""
        try:
            user_balances = []

            for member in ctx.guild.members:
                if member.bot:
                    continue

                pocket_money = get_user_balance(member.id)
                bank_balance = get_user_bank_balance(member.id)
                user_inventory = get_user_inventory(member.id)

                total_inventory_value = sum(combined_items[item_id]["sell"] if item_id in combined_items and item_id != 'meth' else shop_items[item_id]["cost"] for item_id in user_inventory if item_id != 'meth')

                total_balance = pocket_money + bank_balance + total_inventory_value

                user_balances.append((member.id, total_balance))

            user_balances.sort(key=lambda x: x[1], reverse=True)

            user_id = ctx.author.id
            user_rank = next((rank + 1 for rank, (member_id, _) in enumerate(user_balances) if member_id == user_id), None)

            embed = discord.Embed(
                title="💰 Highest Networths 💰",
                color=discord.Color.green()
            )

            for rank, (member_id, balance) in enumerate(user_balances[:10], start=1):
                member = ctx.guild.get_member(member_id)
                if member:
                    embed.add_field(name=f"**#{rank}** - {member.display_name}", value=f"💰 **{balance} credits**", inline=False)

            embed.add_field(name="\u200b", value="\u200b", inline=False)

            if user_rank is not None:
                embed.add_field(name="Your Rank", value=f"Your net worth rank is **#{user_rank}**", inline=False)
            else:
                embed.add_field(name="Your Rank", value="**You are not ranked in the top net worths.**", inline=False)

            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(e)
            print(e)


def setup(bot):
    bot.add_cog(TransactionCommands(bot))
