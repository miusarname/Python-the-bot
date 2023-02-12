import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import os
import asyncio


client = commands.Bot(command_prefix='/',intents=discord.Intents.all())

""" State """

bot_status=cycle(["Creando preguntas...","Leyendo documentaciones...","Consultadon API...","Programando preguntas..."])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print('el bot esta conectado')
    change_status.start()

    
""" Cogs """

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            """ client.load_extension(f"cogs.{filename[:-3]}")
            await print(f"{filename[:-3]} ha cargado") """
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start('MTA3MzYwODA1NDE2MTAxNDg0NQ.G9WW4k.11bYC4CbXW8luhSwyMVru6x0C3pFzo4-HVfIJ') 
        """ falta la al final c """




@client.command()
async def ping(ctx):
    bot_latency=round(client.latency * 100)
    await ctx.send(f"{bot_latency} Ms de ping...pong")


""" Command """
@client.command(aliases=["RandomQ","Split Question","QR"])
async def question_ramdom(ctx,*,starComand):
    with open('example_question.txt','r')as f:
        random_response =f.readlines()
        response=random.choice(random_response)

    await ctx.send(response)
        
asyncio.run(main())

""" client.run() """
