import asyncio

from main import discord, commands, bot



class Assistance(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, context):
        myEmbed = discord.Embed(title = "Commands Page 1", description = "These are the commands that you can use for this bot.", color = discord.Colour.dark_green())
        myEmbed2 = discord.Embed(title = "Commands Page 2", color = discord.Colour.dark_green())
        myEmbed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuWrXM1JcQ_CKMWg6PlvVSxioV6HKlLEB-yA&usqp=CAU")
        myEmbed.add_field(name = "MODERATION", value = "--------------------------------------------------------------------------", inline=False)
        myEmbed.add_field(name = "-shutdown", value = "This command allows you to shut down the bot *need owner role", inline=False)
        myEmbed.add_field(name = "-purge <amount>", value = "This command allows you to delete previous messages [EX: '-purge 5'] *need owner role", inline=False)
        myEmbed.add_field(name = "-edit servername <name>", value = "This command allows you to change the server name [EX: '-edit servername xbox'] *need owner role", inline=False)
        myEmbed.add_field(name = "-edit region <region>", value = "This command allows you to change the server region [EX: '-edit region Europe'] *need owner role", inline=False)
        myEmbed.add_field(name = "-edit createtextchannel <name>", value = "This command allows you to create a text channel [EX: '-edit createtextchannel general'] *need admin role", inline=False)
        myEmbed.add_field(name = "-edit createvoicechannel <name>", value = "This command allows you to create a voice channel [EX: '-edit createvoicechannel party2'] *need admin role", inline=False)
        myEmbed.add_field(name = "-edit create_role <name>", value = "This command allows you to create roles [EX: '-edit create_role crew'] *need admin role", inline=False)
        myEmbed.add_field(name = "-mute <user>", value = "This command allows you to mute a user [EX: '-mute @beta'] *need admin role", inline=False)
        myEmbed.add_field(name = "-unmute <user>", value = "This command allows you to unmute a user [EX: '-unmute @beta'] *need admin role", inline=False)
        myEmbed.add_field(name = "-deafen <user>", value = "This command allows you to deafen a user [EX: '-deafen @beta'] *need admin role", inline=False)
        myEmbed.add_field(name = "-undeafen <user>", value = "This command allows you to undeafen a user [EX: '-undeafen @beta'] *need admin role", inline=False)
        myEmbed.add_field(name = "-voicekick <user>", value = "This command allows you to kick a user from the voice channel [EX: '-voicekick @beta'] *need admin role", inline=False)
        myEmbed.add_field(name = "-kick <user> <reason[optional]>", value = "This command allows you to kick a user from the server [EX: '-kick @beta'] *need owner role", inline=False)
        myEmbed.add_field(name = "-ban <user> <reason[optional]>", value = "This command allows you to ban a user from the server [EX: '-ban @beta'] *need owner role", inline=False)
        myEmbed.add_field(name = "-unban <user> <reason[optional]>", value = "This command allows you to unban a user from the server [EX: '-unban @beta'] *need owner role", inline=False)
        myEmbed.add_field(name = "-unewadmin <user>", value = "This command adds removes the head admin role from a user, and assigns it to the specified user [EX: '-newadmin @beta'] *need Admin role", inline=False)
        myEmbed.add_field(name = "MUSIC", value = "--------------------------------------------------------------------------", inline=False)
        myEmbed.add_field(name = "-join", value = "This command allows the discord bot to join the voice channel [EX: '-join'] *need DJ role", inline=False)
        myEmbed.add_field(name = "-leave", value = "This command allows the discord bot to leave the voice channel [EX: '-leave'] *need DJ role", inline=False)
        myEmbed.add_field(name = "-pause", value = "This command pauses the music/video the bot is playing [EX: '-pause'] *need DJ role", inline=False)
        myEmbed.add_field(name = "-resume", value = "This command resumes the music/video the bot was playing [EX: '-resume'] *need DJ role", inline=False)
        myEmbed.add_field(name = "-skip", value = "This command skips the current playing video/music [EX: '-skip'] *need DJ role", inline=False)
        myEmbed.add_field(name = "-clear", value = "This command completely clears the music/video queue [EX: '-clear'] *need DJ role", inline=False)
        myEmbed.add_field(name = "-clear_loop_start", value = "(WARNING: only run this command once) This command deletes the song files downloaded in the backend every 2 hours. [EX: '-clear_loop_start'] *need Owner role", inline=False)
        myEmbed.add_field(name = "-viewqueue", value = "This command allows you to see the music/videos in the queue [EX: '-viewqueue']", inline=False)
        myEmbed.add_field(name = "-play <name> or <url>", value = "This command allows you to play music/videos from youtube [EX: '-play eminem']", inline=False)
        myEmbed2.add_field(name = "BATTLESHIP", value = "--------------------------------------------------------------------------", inline=False)
        myEmbed2.add_field(name = "-battleships <opponent> <size of board: vert> <size of board: hor>", value = "This command allows you to start a game of battleship and specify the size of the board [EX: '-battleships @SuperMcNilliam 6 6']", inline=False)
        myEmbed2.add_field(name = "-place <coordinates>", value = "This command allows you to place your ships on the board, 6 is the max amount [EX: '-place a1 a2 a3 a4 a5 a6']", inline=False)
        myEmbed2.add_field(name = "-shoot <coordinate>", value = "This command allows you to shoot a coordinate on the opponents board [EX: '-shoot b1']", inline=False)
        myEmbed2.add_field(name = "POLLS", value = "--------------------------------------------------------------------------", inline=False)
        myEmbed2.add_field(name = "-poll <time-limit> '<question>' <options[optional]> ", value = "This command allows you to create a timed poll with or without options [EX: '-poll 60 'Who should be admin?' @userA @userB @userC]", inline=False)
        myEmbed2.add_field(name = "EXTRA GAMES", value = "--------------------------------------------------------------------------", inline=False)
        myEmbed2.add_field(name = "-coinflip", value = "This Command lets you flip a coin", inline=False)
        myEmbed2.add_field(name = "-RPS", value = "This command allows you to play a game of rock paper scissors with the bot.", inline=False)
        await context.send(embed = myEmbed)
        await context.send(embed = myEmbed2)

def setup(bot):
    bot.add_cog(Assistance(bot))