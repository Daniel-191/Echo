"""
Farming system for the economy.
Allows users to plant and harvest crops.
"""

from discord.ext import commands
import discord
from colorama import Fore
import time
from utils.utilities import *
from utils.eco_support import *
from utils.constants import COLOR_SUCCESS, COLOR_ERROR, COLOR_WARNING


class Farming(commands.Cog):
    """Farming commands for planting and harvesting crops."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(aliases=['crop', 'carrots'])
    async def plant(self, ctx, amount: int=None):
        """Plant crops (costs credits, takes time to grow)."""
        user_id = ctx.author.id
        user_balance = get_user_balance(user_id)

        try:
            if amount is None:
                embed = discord.Embed(color=embed_error)
                embed.title = "Incorrect usage"
                embed.description = f"{ctx.author.mention}, Please enter the amount of crops you want to plant. Usage: `{prefix}plant <amount>`"
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

            total_cost = amount * cost_per_carrot

            embed = discord.Embed(color=COLOR_SUCCESS)

            if user_has_plants(user_id):
                embed.title = "Wait a Little Longer"
                embed.description = f"{ctx.author.mention}, Your crops take {config.get('carrot_growth_duration')} hours to grow. Try harvesting them using: `{prefix}harvest`."
                embed.color = embed_error
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

            if amount > max_carrot_planted:
                embed.title = "Too Many crops"
                embed.description = f"{ctx.author.mention}, You cannot plant more than {max_carrot_planted} crops."
                embed.color = embed_error
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

            if user_balance < total_cost:
                embed.title = "Not Enough Balance"
                embed.description = f"{ctx.author.mention}, You need {total_cost} credits to plant {amount} crops"
                embed.color = embed_error
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

            plant_carrots(user_id, amount)

            embed.title = "Crops Planted"
            embed.description = f"{ctx.author.mention}, You have planted {amount} crops."
            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
            await ctx.send(embed=embed)

            update_last_action_time(user_id, "plant")
        except Exception as e:
            print(e)

    @commands.command(aliases=['har'])
    async def harvest(self, ctx):
        """Harvest your crops when they're ready."""
        user_id = str(ctx.author.id)
        user_plantations = load_user_plants()

        try:
            if user_id in user_plantations:
                time_planted, amount_planted = user_plantations[user_id]
                current_time = time.time()
                time_left_seconds = max(0, time_planted + growth_duration - current_time)
                growth_percentage = min(100, ((growth_duration - time_left_seconds) / growth_duration) * 100)

                if time_left_seconds <= 0:
                    harvested_amount = amount_planted
                    total_profit = harvested_amount * carrot_sell
                    update_user_balance(user_id, total_profit)
                    del user_plantations[user_id]

                    embed = discord.Embed(
                        title="Success",
                        description=f"{ctx.author.mention}, You have successfully harvested {harvested_amount} crops and earned ${total_profit}.",
                        color=COLOR_SUCCESS
                    )
                    embed.set_footer(text=f"Need some help? Do {ctx.prefix}tutorial")
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                        title="Crop Info",
                        description=f"{ctx.author.mention}, Your crops are not ready yet. They are {int(growth_percentage)}% grown.",
                        color=COLOR_WARNING
                    )
                    embed.set_footer(text=f"Need some help? Do {ctx.prefix}tutorial")
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="Error",
                    description=f"{ctx.author.mention}, You don't have any crops planted.",
                    color=embed_error
                )
                embed.set_footer(text=f"Need some help? Do {ctx.prefix}tutorial")
                await ctx.send(embed=embed)

            save_user_plants(user_plantations)

        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_ready(self):
        t = time.strftime("%H:%M:%S", time.localtime())
        print(f'{Fore.LIGHTGREEN_EX}{t}{Fore.LIGHTGREEN_EX} | Farming Cog Loaded! {Fore.RESET}')
        global user_carrot_plantations
        user_carrot_plantations = load_user_plants()


def setup(bot):
    bot.add_cog(Farming(bot))
