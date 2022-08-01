
from main import discord, commands, bot
from datetime import datetime

class moderation(commands.Cog):
    
    def _init_(self, bot):
        self.bot = bot

    def starts_with(self, msg):
        return True

    #function that can stop the bot from running
    @commands.command()
    @commands.has_role("Owner")
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

    #function that allows you to delete many messages at once
    @commands.command()
    @commands.has_role("Owner")
    async def purge(self, context, amount, day: int = None, month: int = None, year: int = datetime.now().year):  # type: ignore
        if amount == "/":
            if day == None or month == None:
                return 
            else:
                await context.channel.purge(after = datetime(year, month, day), check = self.starts_with)
        else:
            await context.channel.purge(limit = int(amount)+1, check = self.starts_with)

    #Group of function that can be used to edit server
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

    #functions that allow you to moderate members in a voice channel
    @commands.command()
    async def mute(self, context, user: discord.Member):
        await user.edit(mute = True)

    @commands.command()
    async def unmute(self, context, user: discord.Member):
        await user.edit(mute = False)

    @commands.command()
    async def deafen(self, context, user: discord.Member):
        await user.edit(deafen = True)


    @commands.command()
    async def undeafen(self, context, user: discord.Member):
        await user.edit(defean = False)

    @commands.command()
    async def voicekick(context, user: discord.Member):
        await user.edit(voice_channel = None)


    #group of functions that allow you to moderate over user kick, ban, unban. And their specific errorhandlers
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