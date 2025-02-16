import discord
from discord.ext import commands
import os
import re
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

reaction_enabled = True

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()

@bot.tree.command(name="nuts_on", description="Enable nuts reaction")
async def nuts_on(interaction: discord.Interaction):
    global reaction_enabled
    reaction_enabled = True
    await interaction.response.send_message("Nuts reaction enabled!")

@bot.tree.command(name="nuts_off", description="Disable nuts reaction")
async def nuts_off(interaction: discord.Interaction):
    global reaction_enabled
    reaction_enabled = False
    await interaction.response.send_message("Nuts reaction disabled!")

@bot.event
async def on_message(message):
    global reaction_enabled
    if reaction_enabled and re.search(r'\bnuts\b', re.sub(r'[^\w\s]', '', message.content.lower())):
        await message.add_reaction('🥜')
    await bot.process_commands(message)

bot.run(TOKEN)
