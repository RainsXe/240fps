import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print("ログイン完了")

@client.event
async def on_message(message):
    # !などはwake word
    # 普通の発言などでボットが動かないように記号を頭につけてください。
    if message.content == "!占い":
        unsei = ["大吉", "中吉", "吉", "末吉", "小吉", "凶", "大凶"]
        choice = random.choice(unsei)
        await message.channel.send(choice)

client.run(os.getenv('TOKEN'))
