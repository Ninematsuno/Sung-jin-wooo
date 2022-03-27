from pyrogram import filters , Client
from redis import Redis
import os 

bot = Client(
    'bot',
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ['API_HASH'],
    bot_token=os.environ['BOT_TOKEN'],
    plugins=dict(root=f"{__name__}/plugins")
)


PYRO_SESSION = os.environ['PYRO_SESSION']

musicbot = Client(
    PYRO_SESSION,
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ['API_HASH'],
)


help_message = []
