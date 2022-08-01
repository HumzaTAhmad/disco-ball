import discord

from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", help_command = None, intents = intents)


with open('token.txt') as f:
    TOKEN = f.readline()

class main:
    
    def __init__(self):
        pass

    #function that returns the available commands that can be executed by the bot
    @commands.command(aliases = ["about"])
    async def help(self, context):
        myEmbed = discord.Embed(title = "Commands", description = "These are the commands that you can use for this bot.", color = discord.Colour.dark_purple())
        myEmbed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuWrXM1JcQ_CKMWg6PlvVSxioV6HKlLEB-yA&usqp=CAU")
        myEmbed.add_field(name = "!edit servername", value = "This command allows you to change the server name", inline=False)
        myEmbed.add_field(name = "!edit servername", value = "This command allows you to change the server name", inline=False)
        #myEmbed.add_field(name = "!coinflip", value = "This Command lets you flip a coind", inline=False)
        #myEmbed.add_field(name = "!RPS", value = "This command allows you to play a game of rock paper scissors with the bot.", inline=False)
        await context.send(embed = myEmbed)

    bot.load_extension("commands.moderation")
    bot.load_extension("commands.announcement")

    @commands.command()
    async def reload(self, context):
        bot.reload_extension("commands.moderation")
        bot.reload_extension("commands.announcement")

    bot.run(TOKEN)



