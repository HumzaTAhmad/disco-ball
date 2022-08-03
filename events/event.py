from main import commands, discord, bot
    
with open('profanity.txt') as f:
    badwords = f.read()
    badwords_list = badwords.split(",")


class Event(commands.Cog):

    def _init_(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_profanity(self, message, word, channel):
        server_logo = message.guild.icon_url_as(size=1024)
        embed = discord.Embed(title="Profanity Alert!",description=f"{message.author.name} just said ||{word}||", color=discord.Color.blurple()) # Let's make an embed!
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("BOT IS ONLINE")

    @commands.Cog.listener()
    async def on_message(self, msg):
        username = msg.author.display_name
        channel = msg.channel
        for word in badwords_list:
            if word in msg.content:
                await msg.delete()
                await msg.channel.send(f"{username} Don't use that word!")
                bot.dispatch('profanity', msg, word, channel)
                return # So that it doesn't try to delete the message again, which will cause an error.
        #await bot.process_commands(msg) #Default one_message listener already calls process_commands, so we are calling it twice here
    
    @commands.Cog.listener()
    async def on_member_join(member):
        guild = member.guild
        guildname = guild.name
        dmchannel = await member.create_dm()
        await dmchannel.send(f"Welcome to {guildname}!")

def setup(bot):
    bot.add_cog(Event(bot))
