from discord.ext import commands


class Ping:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        m = await ctx.send('Ping!')
        await m.edit(
            content=f'Pong, pong! I\'m still alive {(m.created_at-ctx.message.created_at).microseconds/1000}ms'
        )


def setup(bot):
    bot.add_cog(Ping(bot))
