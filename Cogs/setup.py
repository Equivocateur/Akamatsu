from discord.ext import commands


class Setup(commands.Cog):

    def __init__(self, parent):
        self.parent = parent

    @commands.command(name="feed")
    async def setfeed(self, ctx, channel):
        self.parent.feed = channel
        await ctx.reply(f"Feed changed to <#{channel}>")
