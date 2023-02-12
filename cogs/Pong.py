import discord
from discord.ext import commands


class Pong(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Pong.py esta listo")

    @commands.command()
    async def pong(self,ctx):
        bot_latency=round(self.client.latency * 1000)

        await ctx.send(f"Ping! {bot_latency} ms")


async def setup(client):
    await client.add_cog(Pong(client))