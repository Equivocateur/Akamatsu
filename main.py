import discord
from discord.ext import commands
from Cogs import poll, setup
import config
from Modules.TaskMaster import TaskMaster


class Akamatsu(commands.Bot):

    def __init__(self, token, pref):
        super().__init__(command_prefix=pref, case_insensitive=True, intents=discord.Intents.all())
        self.feed = 0
        self.taskmaster = TaskMaster(self)
        self.run(token)

    async def asyncinit(self):
        await self.taskmaster.setuploop()
        await self.add_cog(poll.Poll(self))
        await self.add_cog(setup.Setup(self))

    async def on_ready(self):
        await self.asyncinit()


Kaede = Akamatsu(config.TOKEN, config.PREF)
