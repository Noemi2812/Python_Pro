import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def sottrarre(ctx, left: int, right: int):
    """sottrarre two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def moltiplicare(ctx, left: int, right: int):
    """moltiplicare two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def dividere(ctx, left: int, right: int):
    """dividere two numbers together."""
    await ctx.send(left / right)

bot.run("MTQyMTE2MjkxNTUwNjk0NjEzOA.GBY0v1.rP98vDxw01BzD7DdbwYizQ9vtDLGtzH1vAVceA")
