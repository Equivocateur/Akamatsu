import discord
import requests
import json
from discord.ext import commands
from dict import serverdict


class Poll(commands.Cog):

    def __init__(self, parent):
        self.parent = parent

    @staticmethod
    async def getinfo(url):
        data = requests.get(url + "/info")
        return json.loads(data.content.decode("utf-8"))

    @staticmethod
    async def getstatus(url):
        data = requests.get(url + "/status")
        return json.loads(data.content.decode("utf-8"))

    @staticmethod
    async def getdict():
        return serverdict

    @commands.command(name="status")
    async def status(self, ctx, server):
        data = await self.getstatus(serverdict[server])
        await ctx.reply(data)

    @commands.command(name="info")
    async def info(self, ctx, server):
        data = await self.getinfo(serverdict[server])
        await ctx.reply(data)

    @commands.command(name="servers")
    async def servers(self, ctx):
        await ctx.reply(await self.getdict())
