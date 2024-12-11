import discord
import os
import random
from os.path import join, dirname
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.default())

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@client.event #起動時
async def on_ready():
    print('ログインしました')

@client.event #占い
async def on_message(message):
    if message.content == "!占い":
        unsei = ["大吉", "中吉", "吉", "末吉", "凶", "大凶"]
        choice = random.choice(unsei)
        await message.channel.send(choice)
        
@client.event #ping
async def on_message(message):
    if message.content == "!ping":
        #ping値を秒単位で取得
        raw_ping = client.latency
        
        #ミリ秒に変換
        raw_ping = round(raw_ping * 1000)
        
        #送信
        await message.reply(f"Pong!\n{raw_ping}ms")

client.run(MTMxNTgwNjg2OTk3NzA0Mjk3NA.GNW6DH.YDFJe3Pm6KkG6EB6uKekldOCAfeJrM7CgvDmig)