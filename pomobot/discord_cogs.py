

import asyncio
import discord
import os
from dotenv import load_dotenv
from pomobot.timer import Timer, TimerStatus
from discord.ext import commands

COLOR_HAPPY = 0xaf6df9
COLOR_DANGER = 0xff8da1


class DiscordCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timer = Timer()
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'We have logged in as {self.bot.user}')

    @commands.command()
    async def start(self, ctx):
        await self.show_message(ctx,"Time to lock in, kid", COLOR_HAPPY)
        self.timer.start()
        while self.timer.getStatus() == TimerStatus.RUNNING:
            await asyncio.sleep(1) #25*60
            self.timer.tick()
        if self.timer.getStatus() == TimerStatus.EXPIRED:
            await self.show_message(ctx,"Yay you can dissociate and ruminate now!", COLOR_HAPPY)

    async def show_message(self, ctx, title, color):
        start_work_em = discord.Embed(title= title, color = color )
        await ctx.send(embed = start_work_em)


        
    @commands.command()
    async def stop(self, ctx): 
        await self.show_message(ctx,"Timer's stopped!", COLOR_DANGER)
        self.timer.stop()
        
    @commands.command()
    async def show_time(self, ctx): 
        await ctx.send(f"Current timer status is : {self.timer.getStatus()}")
        await ctx.send(f"Current time is : {self.timer.get_ticks()}")
        
    @commands.command()
    async def show_help(self, ctx): 
        help_commands = dict()
        for command in self.bot.commands:
            help_commands[command.name] = command.help
        description = "Bot commands are: {}".format(help_commands)
        show_help_em = discord.Embed(title= "hi hi, this is Pomo Dorito, your friendly Pomodororo bot! ", description=description, color = 0xff8da1 )
        await ctx.send(embed = show_help_em)
