
import discord
import random
import os

from dotenv import load_dotenv
from os import getenv
from discord.ext import commands

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='.')

HH = 742482272938229921

# specify intents (members requires explicit opt-in via dev portal)
intents = discord.Intents(guilds=True, members=True, bans=True, emojis=True, voice_states=True, messages=True,
                          reactions=True)
# events
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('.help | Let this day be legend'))
    print('Bot is ready.')


@bot.event
async def on_member_join(member):
    print(f'(member) has joined a server.')


@bot.event
async def on_member_remove(member):
    print(f'(member) has left a server.')

# commands
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'```{extension} cog has been loaded.```')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'```{extension} cog has been unloaded.```')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'```{extension} cog has been reloaded.```')

bot.run(TOKEN)
