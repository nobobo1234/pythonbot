from discord.ext.commands import Context
import asyncio


class CustomContext(Context):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def tell(self, msg, timeout=50.00):
        return await self.send(msg, delete_after=timeout)
