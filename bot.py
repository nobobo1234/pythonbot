from discord.ext.commands import Bot
from managers.command import CommandManager


class BotClass(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command_system = CommandManager(self)

    async def on_ready(self):
        self.command_system.load_commands()
        print('Ready!')

    async def on_message(self, msg):
        await self.command_system.handle_command(msg)


bot = BotClass(command_prefix='kirby!', owner_id='188725806065909760')
bot.run('MzQ0MDIzMzA5Mjk5NDgyNjI1.DTAn0w.C4vGSoBvpEy56SO4NfxoEdhmrGk')
