import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
import discord
from discord.ext import commands
import os


client = commands.Bot(case_insensitive=True, command_prefix='t?')


@client.command()
async def say(ctx, message):
    await ctx.send(message)
    
    
@client.command()
async def hey(ctx):
    responses =["That is a resounding no", "It is not looking likely", "Too hard to tell", "It is quite possible", "Definitely", "no, sir", "yes", "of course!"]
    await ctx.send(random.choice(responses))

client.run(os.getenv("TOKEN"))
