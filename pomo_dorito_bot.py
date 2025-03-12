# This example requires the 'message_content' intent.


import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

#client = discord.Client(intents=intents)

#@client.event
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


#@client.event
@bot.command(name="start", help = "Starts a pomodoro timer")
async def start_timer(ctx):
    await ctx.send("LOCK IN KID")

#client.run(os.environ['BOT_TOKEN'])
bot.run(os.environ['BOT_TOKEN'])