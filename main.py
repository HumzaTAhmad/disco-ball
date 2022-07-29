import discord
intents = discord.Intents.all()
bot = discord.Client(intents = intents)

with open('token.txt') as f:
    TOKEN = f.readline()

class main:
    def __init__(self):
        pass



bot.run(TOKEN)