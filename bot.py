from discord.ext.commands import Bot
from managers.command import CommandManager
import yaml
config = yaml.safe_load(open('./config.yml'))


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
bot.run(config.token)
