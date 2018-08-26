import random
import asyncio
import aiohttp
from discord import Game

import discord
from discord.ext import commands



client = commands.Bot(case_insensitive=True, command_prefix='test')

@client.command()
async def hoi():
    await ctx.send("hOI")

client.run(os.getenv("TOKEN"))
