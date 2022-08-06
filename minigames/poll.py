from main import discord, commands, bot


class poll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.numbers = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
    
    @commands.command()
    async def poll(self, context, minutes: int, title, *options):
       

def setup(bot):
    bot.add_cog(poll(bot))