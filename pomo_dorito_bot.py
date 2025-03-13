

import asyncio
import discord
import os
from dotenv import load_dotenv
from timer import Timer
from discord.ext import commands


load_dotenv()

COLOR_HAPPY = 0xaf6df9
COLOR_DANGER = 0xff8da1

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', help_command = None, intents=intents)

timer = Timer()

#client = discord.Client(intents=intents)

#@client.event
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


#@client.event
@bot.command(name="start", help = "Starts a pomodoro timer")
async def start_timer(ctx):
    await show_message(ctx,"Time to lock in, kid", COLOR_HAPPY)
    
    timer.start()
    while timer.is_running():
        await asyncio.sleep(1) #25*60
        timer.tick()
        if timer.get_ticks() >= 10:
            timer.stop()
        
    await show_message(ctx,"Yay you can dissociate and ruminate now!", COLOR_HAPPY)

async def show_message(ctx, title, color):
    start_work_em = discord.Embed(title= title, color = color )
    await ctx.send(embed = start_work_em)


    
@bot.command(name="stop", help = "Stop a pomodoro timer")
async def stop_timer(ctx): 
    await show_message(ctx,"Timer's stopped!", COLOR_DANGER)
    timer.stop()
    
@bot.command(name="time", help = "Show current time")
async def show_time(ctx): 
    await ctx.send(f"Current timer status is : {timer.is_running()}")
    await ctx.send(f"Current time is : {timer.get_ticks()}")
    
@bot.command(name="help", help = "Show help text")
async def show_help(ctx): 
    help_commands = dict()
    for command in bot.commands:
        help_commands[command.name] = command.help
    description = "Bot commands are: {}".format(help_commands)
    show_help_em = discord.Embed(title= "hi hi, this is Pomo Dorito, your friendly Pomodororo bot! ", description=description, color = 0xff8da1 )
    await ctx.send(embed = show_help_em)
    timer.stop()
    
    

#client.run(os.environ['BOT_TOKEN'])
bot.run(os.environ['BOT_TOKEN'])