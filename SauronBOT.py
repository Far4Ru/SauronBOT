import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()

# @client.event
# async def on_ready():

    # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    # print(
        # f'{client.user} is connected to the following guild:\n'
        # f'{guild.name}(id: {guild.id})'
    # )

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Eternal Magic"))
    print("Bot is ready!")

bot.run(TOKEN)