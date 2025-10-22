import discord, random, os
from discord.ext import commands


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

@bot.command()
async def leggi(ctx):
    with open('text.txt', 'r', encoding='utf-8') as f:
        #print(f.read())
        await ctx.send(f.read())

@bot.command()
async def scrivi(ctx):
    with open('text.txt', 'w', encoding='utf-8') as f:
        text = "Ciao a tutti! domani è sabato"
        f.write(text)

@bot.command()
async def mem(ctx):
    with open('images/mem1.png', 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
   # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("Token")
