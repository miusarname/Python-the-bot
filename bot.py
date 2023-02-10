import discord
from discord.ext import commands


client = commands.Bot(command_prefix='/',intents=discord.Intents.all())


@client.event
async def on_ready():
    print('el bot esta conectado')

@client.command()
async def ping(ctx):
    await ctx.send("pong")

client.run('MTA3MzYwODA1NDE2MTAxNDg0NQ.G0t0Il.Vh0oK00-cjSnKTqYf4g76cciZpG-looeHbVfp4')
