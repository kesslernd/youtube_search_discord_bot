from dotenv import load_dotenv
from YoutubeSearchClient import YoutubeSearchClient
from YoutubeSearchBot import YoutubeSearchBot
import os

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
YT_TOKEN = os.getenv('YT_TOKEN')

load_dotenv()
bot = YoutubeSearchBot(yt_client=YoutubeSearchClient(YT_TOKEN))
bot.run(DISCORD_TOKEN)