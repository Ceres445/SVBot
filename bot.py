from discord.ext import commands
import discord
from aiohttp import ClientSession

from config import token, postgres
import asyncio

initial = [
    'cogs.meme'
]


class SVBot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix='sv.', case_insensitive=True,
                         allowed_mentions=discord.AllowedMentions(everyone=False, roles=True, users=True),
                         status=discord.Status.online, activity=discord.Game(name='use the prefix "sv."'))
        self.session = ClientSession(loop=self.loop)
        self.clean_text = commands.clean_content(escape_markdown=True, fix_channel_mentions=True)
        self.db = None
        for cog in initial:
            self.load_extension(cog)
            print("loaded", cog)

    async def on_message(self, message):
        ctx = await self.get_context(message)
        if message.author.bot:
            return
        elif message.content == f'<@!{self.user.id}>' or message.content == f'<@{self.user.id}>':
            prefix = await self.get_prefix(message)
            await ctx.send(f"use the prefix` {prefix[0]}`")
        await self.process_commands(message)

    async def on_ready(self):
        print(f'Successfully logged in as {self.user}\nSharded to {len(self.guilds)} guilds')

    @classmethod
    async def setup(cls):
        bot = cls()
        try:

            await bot.start(token)
        except KeyboardInterrupt:
            await bot.close()


if __name__ == '__main__':
    postgres, token = postgres, token
    loop = asyncio.get_event_loop()
    loop.run_until_complete(SVBot.setup())
