
import asyncio
import discord
import os
from dotenv import load_dotenv
from pomobot.timer import Timer
from discord.ext import commands
from pomobot.discord_cogs import DiscordCog


load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', help_command = None, intents=intents)

async def main():
    async with bot:
        await bot.add_cog(DiscordCog(bot))
        await bot.start(os.environ['BOT_TOKEN'])

asyncio.run(main())
