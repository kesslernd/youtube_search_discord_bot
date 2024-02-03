from dotenv import load_dotenv
from YoutubeSearchClient import YoutubeSearchClient
from YoutubeSearchBot import YoutubeSearchBot

DISCORD_TOKEN = '<DISCORD TOKEN>'
YT_API_KEY = '<YOUTUBE API KEY>'

load_dotenv()
bot = YoutubeSearchBot(yt_client=YoutubeSearchClient(YT_API_KEY))
bot.run(DISCORD_TOKEN)