"""
Crafting system for the economy.
Allows users to craft items from recipes.
"""

from discord.ext import commands
import discord
from colorama import Fore
import time
from utils.utilities import *
from utils.eco_support import *
from utils.constants import COLOR_SUCCESS, COLOR_ERROR


class Crafting(commands.Cog):
    """Crafting commands for combining items."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def recipes(self, ctx):
        """Display all crafting recipes."""
        try:
            embed = discord.Embed(title="Crafting Recipes", description="The 🎉 emoji means you have the materials to craft that item!", color=discord.Colour.green())

            user_id = ctx.author.id
            user_inventory = get_user_inventory(user_id)

            for recipe_id, recipe_details in crafting_recipes.items():
                missing_items = {}
                for ingredient, count in recipe_details.items():
                    if ingredient != 'result' and (user_inventory.count(ingredient) < count):
                        missing_items[ingredient] = count - user_inventory.count(ingredient)

                if not missing_items:
                    result_sell_price = craftables.get(recipe_id, {}).get('sell', 'unknown price')
                    recipe_text = ', '.join([f"{count}x {combined_items[item]['name']}" for item, count in recipe_details.items() if item != 'result'])
                    embed.add_field(name=f"{recipe_id} 🎉", value=f"**Sell price: {result_sell_price}**\n{recipe_text}", inline=False)
                else:
                    recipe_text = ', '.join([f"{count}x {combined_items[item]['name']}" for item, count in recipe_details.items() if item != 'result'])
                    embed.add_field(name=f"{recipe_id}", value=f"**Sell price: {craftables.get(recipe_id, {}).get('sell', 'unknown price')}**\n{recipe_text}", inline=False)

            embed.set_footer(text=f"Need some help? Do {prefix}tutorial")

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(e)
            print(e)

    @commands.command()
    async def craft(self, ctx, item_name: str=None):
        """Craft an item from a recipe."""
        user_id = ctx.author.id

        try:
            if item_name is None:
                embed = discord.Embed(title="Incorrect Usage", description=f"Correct usage: `{ctx.prefix}craft <item>`", color=embed_error)
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
                return

            item_name = item_name.lower()

            if item_name in crafting_recipes:
                recipe = crafting_recipes[item_name]
                inventory = get_user_inventory(user_id)
                missing_items = {}

                for ingredient, count in recipe.items():
                    if ingredient != 'result' and (inventory.count(ingredient) < count):
                        missing_items[ingredient] = count - inventory.count(ingredient)

                if missing_items:
                    missing_items_text = ', '.join([f"{count}x {item}" for item, count in missing_items.items()])
                    embed = discord.Embed(title="Missing Items", description=f"You are missing {missing_items_text} for crafting {item_name}.", color=embed_error)
                    embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                    await ctx.send(embed=embed)
                else:
                    for ingredient, count in recipe.items():
                        if ingredient != 'result':
                            for _ in range(count):
                                remove_item_from_inventory(user_id, ingredient)

                    add_item_to_inventory(user_id, recipe['result'])

                    embed = discord.Embed(title="Crafting Successful", description=f"You have crafted {recipe['result']}.", color=COLOR_SUCCESS)
                    embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Error", description="This item cannot be crafted or does not exist.", color=embed_error)
                embed.set_footer(text=f"Need some help? Do {prefix}tutorial")
                await ctx.send(embed=embed)
        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_ready(self):
        t = time.strftime("%H:%M:%S", time.localtime())
        print(f'{Fore.LIGHTGREEN_EX}{t}{Fore.LIGHTGREEN_EX} | Crafting Cog Loaded! {Fore.RESET}')


def setup(bot):
    bot.add_cog(Crafting(bot))
