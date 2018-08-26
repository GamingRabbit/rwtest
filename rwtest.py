import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
import discord
from discord.ext import commands

BOT_PRE="test"

client = Bot(case_insensitive=True, command_prefix=BOT_PRE)

@client.command()
async def hOI():
    ctx.send("hOI")

client.run(os.getenv("TOKEN"))
