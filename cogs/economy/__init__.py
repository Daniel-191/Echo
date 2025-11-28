"""
Economy system for Echo bot.
Main package that combines all economy-related commands.
"""

from discord.ext import commands
from colorama import Fore
import time

from .inventory import InventoryCommands
from .transactions import TransactionCommands
from .games import GameCommands


class Economy(commands.Cog):
    """
    Main Economy cog that combines all economy functionality.
    This cog doesn't have its own commands - it just loads the sub-cogs.
    """

    def __init__(self, bot):
        self.bot = bot

        # Add all economy sub-cogs
        bot.add_cog(InventoryCommands(bot))
        bot.add_cog(TransactionCommands(bot))
        bot.add_cog(GameCommands(bot))

    @commands.Cog.listener()
    async def on_ready(self):
        t = time.strftime("%H:%M:%S", time.localtime())
        print(f'{Fore.LIGHTGREEN_EX}{t}{Fore.LIGHTGREEN_EX} | Economy Cog Loaded! {Fore.RESET}')


def setup(bot):
    """Setup function for loading the Economy cog."""
    bot.add_cog(Economy(bot))


# Export for easier imports
__all__ = ['Economy', 'InventoryCommands', 'TransactionCommands', 'GameCommands']
