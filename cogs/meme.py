
import discord
from discord.ext import commands, tasks

from cogs.utils.get_memes import get_meme, convert_to_seconds


class Memey(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.post = get_meme()
        self.automeme = None

    async def post_meme(self, ctx):
        post = next(self.post)
        embed = discord.Embed(title=post.title, colour=discord.Colour.random(),
                              url="https://www.reddit.com" + post.permalink)
        embed.set_image(url=post.url)
        embed.set_footer(text=f"\ud83d\udc4d {post.score} | \ud83d\udcac {post.num_comments}")
        await ctx.send(embed=embed)

    @commands.command()
    async def start(self, ctx, *, args: convert_to_seconds = 10):
        self.automemer.change_interval(seconds=args)
        await self.automemer.start(ctx)

    @commands.command()
    async def stop(self, ctx):
        self.automemer.cancel()
        await ctx.send('stopped memes ')

    @tasks.loop(seconds=10, count=100)
    async def automemer(self, ctx):
        await self.post_meme(ctx)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower() == 'memes bish':
            ctx = await self.bot.get_context(message)
            await self.post_meme(ctx)


def setup(bot):
    bot.add_cog(Memey(bot))
