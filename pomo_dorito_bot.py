# This example requires the 'message_content' intent.

import asyncio
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
    
    start_work_em = discord.Embed(title= "Time to lock in, kid", color = 0xaf6df9 )
    await ctx.send(embed = start_work_em)
    await asyncio.sleep(5)
    start_play_em = discord.Embed(title= "Yay you can dissociate and ruminate now!", color = 0xaf6df9 )
    await ctx.send(embed = start_play_em)
    
@bot.command(name="stop", help = "Stop a pomodoro timer")
async def stop_timer(ctx):
    
    stop_timer_em = discord.Embed(title= "Timer's stopped!", color = 0xff8da1 )
    await ctx.send(embed = stop_timer_em)

#client.run(os.environ['BOT_TOKEN'])
bot.run(os.environ['BOT_TOKEN'])