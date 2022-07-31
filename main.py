import discord

from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", help_command = None, intents = intents)


with open('token.txt') as f:
    TOKEN = f.readline()

class main:
    def __init__(self):
        pass
    bot.load_extension("commands.moderation")
    bot.load_extension("commands.announcement")
    bot.run(TOKEN)



