import calendar

from main import discord, commands, bot
from datetime import datetime

class moderation(commands.Cog):
    
    def _init_(self, bot):
        self.bot = bot

    
    @commands.command(aliases = ["about"])
    async def help(self, context):
        myEmbed = discord.Embed(title = "Commands", description = "These are the commands that you can use for this bot.", color = discord.Colour.dark_purple())
        myEmbed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuWrXM1JcQ_CKMWg6PlvVSxioV6HKlLEB-yA&usqp=CAU")
        #myEmbed.add_field(name = "!ping", value = "This Command replies back with Pong whenever you write !ping.", inline=False)
        #myEmbed.add_field(name = "!coinflip", value = "This Command lets you flip a coind", inline=False)
        #myEmbed.add_field(name = "!RPS", value = "This command allows you to play a game of rock paper scissors with the bot.", inline=False)
        await context.send(embed = myEmbed)

    @commands.command()
    async def shutdown(self, context):
        if context.message.author.id == 322220501898362880: #replace OWNERID with your user id
            print("shutdown")
        try:
            await bot.logout()
        except:
            print("EnvironmentError")
            self.bot.clear()
        else:
            await context.send("You do not own this bot!")

    @commands.group()
    async def edit(self, context):
        pass

    @edit.command()
    async def servername(self, context, *, input):
        await context.guild.edit(name = input)

    @edit.command()
    async def region(self, context, *, input):
        await context.guild.edit(region = input)

    @region.error
    async def errorhandler(self, context, error):  # type: ignore
        if isinstance(error, commands.CommandInvokeError):
            await context.send("Please enter a valid region name.")

    @edit.command()
    async def createtextchannel(self, context, *, input):
        await context.guild.create_text_channel(name = input)

    @edit.command()
    async def createvoicechannel(self, context, *, input):
        await context.guild.create_voice_channel(name = input)

    @edit.command()
    async def create_role(self, context, *, input):
        await context.guild.create_role(name= input)

    @commands.command()
    @commands.has_role("Owner")
    async def kick(self, context, member: discord.Member, *, reason = None):
        await context.guild.kick(member, reason = reason)

    @commands.command()
    @commands.has_role("Owner")
    async def ban(self, context, member: discord.Member, *, reason = None):
        await context.guild.ban(member, reason = reason)
    
    @commands.command()
    @commands.has_role("Owner")
    async def unban(self, context, *, input):
        name, discriminator = input.split("#")
        banned_member = await context.guild.bans()
        for bannedmember in banned_member:
            username = bannedmember.user.name
            disc = bannedmember.user.discriminator
            if name == username and discriminator == disc:
                await context.guild.unban(bannedmember.user)

    @kick.error
    async def errorhandler(context, error):  # type: ignore
        if isinstance(error, commands.MissingRole):
            await context.send("You don't have the necessary Roles for this command")

    @ban.error
    async def errorhandler(context, error):  # type: ignore
        if isinstance(error, commands.MissingRole):
            await context.send("You don't have the necessary Roles for this command")

    @unban.error
    async def errorhandler(context, error):  # type: ignore
        if isinstance(error, commands.MissingRole):
            await context.send("You don't have the necessary Roles for this command")

def setup(bot):
    bot.add_cog(moderation(bot))