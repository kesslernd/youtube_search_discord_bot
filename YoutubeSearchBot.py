import discord
from discord.ext import commands
import YoutubeSearchClient


class YoutubeSearchBot(commands.Bot):

    yt_client = None

    def __init__(self, yt_client: YoutubeSearchClient):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='$', intents=intents)
        self.yt_client = yt_client
        self.add_command(self.search)

    @commands.command()
    async def search(ctx, *args):
        message = ' '.join(ctx.message.clean_content.split(' ')[1:])
        results = ctx.bot.yt_client.search(message)
        resp = f'https://youtube.com/watch?v={results[0]["id"]}'
        await ctx.send(resp)