import discord

from discord.ext import commands

bot = commands.Bot(command_prefix = "!", help_command = None)


with open('token.txt') as f:
    TOKEN = f.readline()

class main:
    def __init__(self):
        pass
    bot.load_extension("commands.moderation")
    bot.run(TOKEN)



