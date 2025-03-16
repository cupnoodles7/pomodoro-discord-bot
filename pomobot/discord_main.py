
import asyncio
import discord
import os
from dotenv import load_dotenv
from pomobot.timer import Timer
from discord.ext import commands


load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', help_command = None, intents=intents)
bot.add_cog(Discordcog(bot))
bot.run(os.environ['BOT_TOKEN'])
