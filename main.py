import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.default())

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@client.event
async def on_ready():
    print('ログインしました')


TOKEN = os.getenv("TOKEN")
if TOKEN:
    client.run(os.getenv('TOKEN'))
else:
    print("Tokenが見つかりませんでした")
