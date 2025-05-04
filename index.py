import discord 
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("token")

intents = discord.Intents.all()
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix = "!", intents=intents)

@bot.event
async def on_ready():
    print("running bot")

bot.run(token)

