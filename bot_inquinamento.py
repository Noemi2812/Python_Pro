import discord, random, os
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def inquinamento(ctx):
    idee = ["L'inquinamento è l'alterazione dell'ambiente da parte dell'uomo","Solo noi umani produciamo rifiuti che la natura non può digerire","Con i l'emissione industriali sporcano l'aria","L'aria che respiriamo è piena di veleni invisibili","Le cause dell'inquinamento sono scarichi di automobili, industrie e rifiuti non differenziati"]
    idee_inquinamento  = random.choice(idee)
    await ctx.send(idee_inquinamento)

@bot.command()
async def inquinamento2(ctx):
    with open('inquinamento.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())

@bot.command()
async def inquinamento3(ctx):
    img_name = random.choice(os.listdir("images2"))
    with open(f'images2/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTQyMTE2MjkxNTUwNjk0NjEzOA.GzimZL.hUT0yTxsEMARv6pBmLTD0dizf2BhRmeHZBQwwo")