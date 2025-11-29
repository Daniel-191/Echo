"""
This file contains:
 - Imports
 - Variables
 - Some functions
"""

from discord.ext.commands import BucketType
from discord.ext import commands, tasks
from typing import List, Tuple, Union
from discord.ui import Button, View
from PIL import Image, ImageDraw
from discord import Interaction
from collections import Counter
from datetime import timedelta
from datetime import datetime
from colorama import Fore
from pathlib import Path
from io import BytesIO
from time import ctime
from card import Card # blackjack game uses this

import requests
import discord
import sqlite3
import asyncio
import random
import bisect
import qrcode
import json
import uuid
import time
import os


# Placeholder storage for buttons
button_storage = {} 

# embed colour (change it to discord.Color.{whatyouwant} or hex values)
embed_colour = discord.Color.from_rgb(0, 255, 255)  # RGB values for cyan

embed_error = discord.Color.red() # error message for embeds

# Just a cool logging variable
t = f"{Fore.LIGHTYELLOW_EX}{ctime()}{Fore.RESET}"

# Locked channels are now stored in database (loaded on-demand)

# Load config from json file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# ---LOAD VARIABLES FROM CONFIG.JSON---

token = config.get("TOKEN")

# Bot invite
bot_invite = config.get("bot_invite_link")

# prefix
prefix = config.get('prefix')

# Moderation
link_ban = config.get('LINK_BAN')
BANNED_LINKS = config.get('BANNED_LINKS', [])

# show guilds the bot is in at launch
show_guilds = config.get("show_guilds")

# welcome messages
member_join = config.get("member_join_message")
welcome_channel_id = config.get("welcome_channel")
welcome_message = config.get("welcome_message")

# carrot values
cost_per_carrot = config.get("carrot_plant_price")
carrot_sell = config.get("carrot_sell_price")
max_carrot_planted = config.get("max_carrots_planted")
growth_duration = 3600 * config.get("carrot_growth_duration")

# Daily reward
daily_reward = config.get('daily_reward')

# max bank size
max_bank_size = config.get("bank_size")

# max gamble amount
max_bet = config.get("max_gamble_amount")

# ----------------------------------------------------------MODERATION FUNCTIONS----------------------------------------------------------

# Check if the user invoking the command is the admin
def is_admin(ctx):
    return ctx.author.id == config.get("ADMIN_ID")

# Unlock channels after the specified duration
async def unlock_channel_after_delay(channel, delay):
    from eco_support import is_channel_locked, remove_locked_channel
    await asyncio.sleep(delay)
    await channel.set_permissions(channel.guild.default_role, send_messages=True)
    if is_channel_locked(channel.id):
        remove_locked_channel(channel.id)
        await channel.send("Channel unlocked automatically after scheduled duration.")


# Locked channels save/load functions moved to eco_support.py database functions


# convert the users parsed duration (seconds, minutes, hours, days) into the correct value
def convert_to_seconds(duration_str):
    try:
        unit = duration_str[-1]
        value = int(duration_str[:-1])
        if unit == 's':
            return value
        elif unit == 'm':
            return value * 60
        elif unit == 'h':
            return value * 3600
        elif unit == 'd':
            return value * 86400
    except Exception:
        return None


# --------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------Output Guilds the bot is in (main.py)----------------------------------------------------------

def guilds(bot):
    if show_guilds == "true":
        try:
            guild_count = 0

            for guild in bot.guilds:
                print(f"{Fore.RED}- {guild.id} (name: {guild.name})\n{Fore.RESET}")

                guild_count = guild_count + 1

            print(f"{t}{Fore.LIGHTBLUE_EX} | {bot.user.display_name} is in {str(guild_count)} guilds.\n{Fore.RESET}")

        except Exception as e:
            print(e)

# --------------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------CHECK LOCKED CHANNELS ON BOT LOAD----------------------------------------------------------


async def lock_function(bot, unlock_channel_after_delay):
    """Restore locked channels from database on bot startup."""
    from eco_support import get_locked_channels, remove_locked_channel

    # Get all locked channels from database
    locked_channels = get_locked_channels()

    # Reapply locks
    for channel_id, data in locked_channels.items():
        channel = bot.get_channel(int(channel_id))
        if channel:
            unlock_time = datetime.datetime.fromisoformat(data['unlock_time'])
            if datetime.datetime.now() < unlock_time:
                # Reapply lock
                await channel.set_permissions(channel.guild.default_role, send_messages=False)

                # Schedule unlock
                asyncio.create_task(unlock_channel_after_delay(channel, (unlock_time - datetime.datetime.now()).total_seconds()))
            else:
                # Unlock if the time has passed
                await channel.set_permissions(channel.guild.default_role, send_messages=True)
                remove_locked_channel(channel_id)


# ----------------------------------------------------------MAKE EMBED FUCNTION----------------------------------------------------------


def make_embed(title=None, description=None, color=None, author=None,
               image=None, link=None, footer=None) -> discord.Embed:
    """Wrapper for making discord embeds"""
    embed = discord.Embed(
        title=title,
        description=description,
        url=link,
        color=color if color else discord.Color.random()
    )
    if author: 
        embed.set_author(name=author)
    if image: 
        embed.set_image(url=image)
    if footer: 
        embed.set_footer(text=footer)
    else: 
        embed.set_footer(text=datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    return embed