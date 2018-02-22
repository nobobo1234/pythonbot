import discord
import yaml
from discord.ext.commands import Bot

from managers.command import CommandManager

config = yaml.safe_load(open('./config.yml'))


class BotClass(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_id = None
        self.owner_id = None
        self.command_system = CommandManager(self)

    async def on_ready(self):
        app_info = await self.application_info()
        self.owner_id = app_info.owner.id
        self.app_id = app_info.owner.id
        self.command_system.load_commands()
        print('Ready!')
        print(f'Invite url: {discord.utils.oauth_url(self.app_id)}')

    async def on_message(self, msg):
        await self.command_system.handle_command(msg)

    async def on_command_error(self, ctx, exception):
        await ctx.send(exception)


bot = BotClass(command_prefix='kirby!', owner_id='188725806065909760')
bot.run(config['token'])
