import json
import requests
import discord
from discord.ext import commands
from Cogs import poll, setup
import config


class Akamatsu(commands.Bot):

    def __init__(self, token, pref):
        super().__init__(command_prefix=pref, case_insensitive=True, intents=discord.Intents.all())
        self.run(token)
        self.feed = 0

    async def on_ready(self):
        await self.add_cog(poll.Poll(self))
        await self.add_cog(setup.Setup(self))


Kaede = Akamatsu(config.TOKEN, config.PREF)
