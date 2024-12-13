import discord
import random
import os

from dotenv import load_dotenv
from discord import app_commands


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event  # 起動時
async def on_ready():
    print('ログインしました')
    
    #スラッシュコマンド同期
    await tree.sync()

@tree.command(name="test",description="テストコマンドです。")
async def test_command(interaction: discord.Interaction,text:str="てすと"):#デフォルト値を指定
    await interaction.response.send_message(text,ephemeral=True)

@client.event  # メッセージ受信時
async def on_message(message):
    # Bot自身のメッセージは無視
    if message.author.bot:
        return

    # 占いコマンド
    if message.content == "!占い":
        unsei = ["大吉", "中吉", "吉", "末吉", "凶", "大凶"]
        choice = random.choice(unsei)
        await message.channel.send(choice)

    # pingコマンド
    elif message.content == "!ping":
        raw_ping = round(client.latency * 1000)  # ミリ秒に変換
        await message.reply(f"Pong!\n{raw_ping}ms")

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
    client.run(TOKEN)
else:
    print("TOKENが見つかりませんでした。")