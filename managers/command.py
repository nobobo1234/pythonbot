import os


class CommandManager:
    def __init__(self, bot):
        self.bot = bot
        self.prefix = self.bot.command_prefix

    def load_commands(self):
        for file in os.listdir('./commands/'):
            filename = os.fsdecode(file)
            if filename.endswith('.py') and filename != '__init__.py':
                command_name = filename.split('.')[0]
                self.bot.load_extension('commands.' + command_name)

    def get_cogs(self):
        return self.bot.cogs

    def get_cog(self, name):
        return self.bot.get_cog(name)

    async def handle_command(self, msg):
        if msg.author == self.bot.user:
            return None

        if not msg.content.startswith(self.prefix):
            return None

        # TODO: Add blacklisting

        ctx = await self.bot.get_context(msg)
        return await self.bot.invoke(ctx)
