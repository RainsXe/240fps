import discord
from discord import app_commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event  # 起動時
async def on_ready():
    print('ログインしました')

    # スラッシュコマンドを同期
    await tree.sync()

@tree.command(name='hello', description='Say hello to the world!')
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('Hello, World!')

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

    elif message.content == "!RandAtkOpe":
        atkOpe = ["STRIKER", "DEMOS", "RAM", "BRAVA", "GRIM", "SENS", "OSA", "FLORES", "ZERO", "ACE", "IANA", "KALI", "AMARU",
                  "NOKK", "GRIDLOCK", "NOMAD", "MAVERICK","LION", "FINKA", "DOKKAEBI", "ZOFIA", "YING", "JACKAL", "HIBANA",
                  "CAPITAO", "BLACKBEARD", "BUCK", "SLEDGE", "THATCHER", "ASH", "THERMITE", "MONTAGNE", "TWITCH", "BLITZ",
                  "IQ", "FUZE", "GLAZ"]

        choice = random.choice(atkOpe)
        await message.channel.send(choice)

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
    client.run(TOKEN)
else:
    print("Tokenが見つかりませんでした")