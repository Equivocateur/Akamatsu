import requests
import json
import asyncio
from discord.ext import commands
from dict import serverDict


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
        return serverDict

    async def getplayers(self, url):
        data = await self.getstatus(url)
        return [data['players'], data['soft_max_players']]

    @commands.command(name="status")
    async def status(self, ctx, server):
        data = await self.getstatus(serverDict[server])
        await ctx.reply(data)

    @commands.command(name="info")
    async def info(self, ctx, server):
        data = await self.getinfo(serverDict[server])
        await ctx.reply(data)

    @commands.command(name="servers")
    async def servers(self, ctx):
        await ctx.reply(await self.getdict())

    @commands.command(name="players")
    async def players(self, ctx, server):
        playercount = await self.getplayers(serverDict[server])
        await ctx.reply(f"{server} has {playercount[0]}/{playercount[1]} players.")

    async def startqueue(self, user, server):
        await self.parent.feed.send(f"Queuing for {server}.")
        while True:
            counts = await self.getplayers(serverDict[server])
            if counts[0] < counts[1]:
                await self.parent.feed.send(f"<@{user}> - {server} has a free slot: {counts[0]}/{counts[1]}")
                break
            await asyncio.sleep(0.15)

    @commands.command(name="Queue")
    async def queue(self, ctx, server):
        if self.parent.feed == 0:
            await ctx.reply("Feed isn't set!")
            return

        await self.parent.taskmaster.createtask(self.startqueue, ctx.author.id, server)

