from main import discord, commands, bot


class poll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.numbers = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
    
    @commands.command()
    async def poll(self, context, minutes: int, title, *options):
        guild = context.guild
        server_logo = guild.icon_url_as(size=1024)

        if len(options) == 0:
            embedPoll = discord.Embed(title = title, description = f"You have **{minutes}** minutes remaining!", color = discord.Colour.dark_green())
            embedPoll.set_thumbnail(url = server_logo)
            msg = await context.send(embed = embedPoll)
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")

        else:
            embedPoll = discord.Embed(title = title, description = f"You have **{minutes}** minutes remaining!", color = discord.Colour.dark_green())
            embedPoll.set_thumbnail(url = server_logo)
            for number, option in enumerate(options):
                embedPoll.add_field(name = f"{self.numbers[number]}", value = f"**{option}**", inline = False)
            msg = await context.send(embed = embedPoll)

            for x in range(len(embedPoll.fields)):
                await msg.add_reaction(self.numbers[x])

def setup(bot):
    bot.add_cog(poll(bot))