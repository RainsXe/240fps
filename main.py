import discord
import os
import random
from os.path import join, dirname, defpath
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.default())

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content == "!占い":
        unsei = ["大吉", "中吉", "吉", "末吉", "凶", "大凶"]
        choice = random.choice(unsei)
        await message.channel.send(choice)

client.run(os.getenv('TOKEN'))