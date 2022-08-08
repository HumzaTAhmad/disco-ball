import discord
import os

from discord.ext import tasks, commands
from dotenv import load_dotenv

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", help_command = None, intents = intents)


load_dotenv('.env')
TOKEN = os.getenv("TOKEN")

class Main:

    def __init__(self, bot):
        self.bot = bot
        
    
    
    #function that returns the available commands that can be executed by the bot


    bot.load_extension("commands.moderation")
    bot.load_extension("commands.announcement")
    bot.load_extension("commands.music")
    bot.load_extension("commands.assistance")
    bot.load_extension("events.event")
    bot.load_extension("minigames.battleship")
    bot.load_extension("minigames.small_minigames")
    bot.load_extension("minigames.polls")

    @commands.command()
    async def reload(self, context):
        bot.reload_extension("commands.moderation")
        bot.reload_extension("commands.announcement")
        bot.reload_extension("commands.music")
        bot.reload_extension("commands.assistance")
        bot.reload_extension("events.event")
        bot.reload_extension("minigames.battleship")
        bot.reload_extension("minigames.polls")

    bot.run(TOKEN)



