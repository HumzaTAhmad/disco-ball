import asyncio

from main import discord, commands, bot



class Assistance(commands.Cog):

    def _init_(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, context):
        myEmbed = discord.Embed(title = "Commands", description = "These are the commands that you can use for this bot.", color = discord.Colour.dark_purple())
        myEmbed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuWrXM1JcQ_CKMWg6PlvVSxioV6HKlLEB-yA&usqp=CAU")
        myEmbed.add_field(name = "!edit servername", value = "This command allows you to change the server name", inline=False)
        myEmbed.add_field(name = "!edit servername", value = "This command allows you to change the server name", inline=False)
        #myEmbed.add_field(name = "!coinflip", value = "This Command lets you flip a coin", inline=False)
        #myEmbed.add_field(name = "!RPS", value = "This command allows you to play a game of rock paper scissors with the bot.", inline=False)
        await context.send(embed = myEmbed)

def setup(bot):
    bot.add_cog(Assistance(bot))