import discord
import os
import re
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if re.search(r'\bnuts\b', re.sub(r'[^\w\s]', '', message.content.lower())):
        await message.add_reaction('🥜')

client.run(TOKEN)