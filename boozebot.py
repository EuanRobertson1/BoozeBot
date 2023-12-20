import discord
from dotenv import load_dotenv
import os


#Connecting to Discord
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client(intents=discord.Intents.default())

client.run(TOKEN)

    