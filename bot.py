import discord
from discord.ext import commands
import random


client = commands.Bot(command_prefix='/',intents=discord.Intents.all())


@client.event
async def on_ready():
    print('el bot esta conectado')

@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command(aliases=["RandomQ","Split Question","QR"])
async def question_ramdom(ctx,*,starComand):
    with open('example_question.txt','r')as f:
        random_response =f.readlines()
        response=random.choice(random_response)

    await ctx.send(response)
        

client.run('MTA3MzYwODA1NDE2MTAxNDg0NQ.GydovL.vompnPYjvunYN3-lzqmuo-x6h8TKDp3wu1sWsk')
