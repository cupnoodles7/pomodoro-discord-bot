

import asyncio
import discord
import os
import sqlite3
from dotenv import load_dotenv
from datetime import datetime
from pomobot.timer import Timer, TimerStatus
from discord.ext import commands

COLOR_HAPPY = 0xaf6df9
COLOR_DANGER = 0xff8da1


class DiscordCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timer = Timer()
        self.db = sqlite3.connect('pomobot.db')
        self.create_tables()

    def create_tables(self):
        cur = self.db.cursor()
        # create table
        cur.execute('''
        CREATE TABLE IF NOT EXISTS alarms(
            id integer PRIMARY KEY AUTOINCREMENT,
            username text NOT NULL,
            start_time text NOT NULL,
            delay text NOT NULL
            )
        ''')

        self.db.commit()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'We have logged in as {self.bot.user}')

    @commands.command()
    async def start(self, ctx):
        if self.timer.get_status() == TimerStatus.RUNNING:
            await self.show_message(ctx, "chat timer's already running, finish up this session to start again smh my head", COLOR_HAPPY)
            return

        # setting time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        cur = self.db.cursor()
        cur.execute('''
        INSERT INTO alarms (username, start_time, delay) VALUES
        (?,?,?)
        ''', [str(ctx.author), current_time, '10'])
        self.db.commit()

        cur = self.db.cursor()
        for row in cur.execute("SELECT * FROM alarms"):
            print(row)

        await self.show_message(ctx, "LOCK TF IN", COLOR_HAPPY)
        self.timer.start(max_ticks=10)
        while self.timer.get_status() == TimerStatus.RUNNING:
            await asyncio.sleep(1)  # 25*60
            self.timer.tick()
        if self.timer.get_status() == TimerStatus.EXPIRED:
            await self.show_message(ctx, "yay you can dissociate and ruminate now ~", COLOR_HAPPY)
            self.timer.start(max_ticks=10)
            while self.timer.get_status() == TimerStatus.RUNNING:
                await asyncio.sleep(1)  # 25*60
                self.timer.tick()
            if self.timer.get_status() == TimerStatus.EXPIRED:
                await self.show_message(ctx, "break over :(", COLOR_HAPPY)

    async def show_message(self, ctx, title, color):
        start_work_em = discord.Embed(title=title, color=color)
        await ctx.send(embed=start_work_em)

    @commands.command()
    async def stop(self, ctx):

        if self.timer.get_status() != TimerStatus.RUNNING:
            await self.show_message(ctx, "Chat timer stopped ages ago", COLOR_HAPPY)
            return
        await self.show_message(ctx, "Timer's stopped!", COLOR_DANGER)
        self.timer.stop()

    @commands.command()
    async def show_time(self, ctx):
        await ctx.send(f"Current timer status is : {self.timer.get_status()}")
        await ctx.send(f"Current time is : {self.timer.get_ticks()}")

    @commands.command()
    async def show_help(self, ctx):
        help_commands = dict()
        for command in self.bot.commands:
            help_commands[command.name] = command.help
        description = "Bot commands are: {}".format(help_commands)
        show_help_em = discord.Embed(
            title="hi hi, this is Pomo Dorito, your friendly Pomodororo bot! ", description=description, color=0xff8da1)
        await ctx.send(embed=show_help_em)
