from main import discord, commands

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



def setup(bot):
    bot.add_cog(moderation(bot))