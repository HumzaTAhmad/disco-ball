import calendar

from main import discord, commands, bot, tasks
from discord.ext.commands import MemberConverter
from datetime import datetime

class polls(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.numbers = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
    
    @commands.command()
    async def poll(self, context, minutes: int, title, *options):
        self.guild = context.guild
        self.server_logo = self.guild.icon_url_as(size=1024)

        if len(options) == 0:
            embedPoll = discord.Embed(title = title, description = f"You have **{minutes}** minutes remaining!", color = discord.Colour.dark_green())
            embedPoll.set_thumbnail(url = self.server_logo)
            msg = await context.send(embed = embedPoll)
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")

        else:
            embedPoll = discord.Embed(title = title, description = f"You have **{minutes}** minutes remaining!", color = discord.Colour.dark_green())
            embedPoll.set_thumbnail(url = self.server_logo)
            for number, option in enumerate(options):
                embedPoll.add_field(name = f"{self.numbers[number]}", value = f"**{option}**", inline = False)
            msg = await context.send(embed = embedPoll)

            for x in range(len(embedPoll.fields)):
                await msg.add_reaction(self.numbers[x])

        self.poll_loop.start(context, minutes, title, options, msg)
    
    @tasks.loop(minutes = 1)
    async def poll_loop(self, context, minutes, title, options, msg):
        count = self.poll_loop.current_loop
        remaining_time = minutes - count

        newEmbed = discord.Embed(title = title, description = f"You have **{remaining_time}** minutes remaining!", color = discord.Colour.dark_green())
        newEmbed.set_thumbnail(url = self.server_logo)
        for number, option in enumerate(options):
                newEmbed.add_field(name = f"{self.numbers[number]}", value = f"**{option}**", inline = False)
        
        await msg.edit(embed = newEmbed)

        if remaining_time == 0:
            counts = []
            msg = discord.utils.get(bot.cached_messages, id=msg.id)
            reactions = msg.reactions

            for reaction in reactions:
                counts.append(reaction.count)
            max_value = max(counts)
            i = 0
            for count in counts:
                if count == max_value:
                    i = i + 1

            if i > 1:
                await context.send("Its a draw")
            else:
                max_index = counts.index(max_value)

                if len(options) == 0:
                    emojiWinner = reactions[max_index]
                    if emojiWinner.emoji == "👍":
                        await context.send("More people agree.")
                    if emojiWinner.emoji == "👍":
                        await context.send("More people don't agree.")

                else:
                    winner = options[max_index]
                    emojiWinner = reactions[max_index]

                    await context.send("Times Up!")
                    await context.send(f"**{winner}** has won the Poll!")
                    
                    if winner[1] == "@":
                        #look into message mentions
                    
                self.poll_loop.stop()

    @tasks.loop(minutes = 1)
    async def newadmin(self, context, new_admin: discord.Member):
        guild = context.guild

        admin_role = guild.get_role(1003116038839353365)
        old_admin_list = admin_role.members

        if(len(old_admin_list) == 0):
            await new_admin.add_roles(admin_role, reason=None, atomic=True)
            await context.send(f"Gave the Head Admin role to @{new_admin}")
        else:
            old_admin = old_admin_list[0]
            
            await old_admin.remove_roles(admin_role, reason=None, atomic=True)
            #old_admin, old_admin_discriminator = old_admin.split("#")

            await new_admin.add_roles(admin_role, reason=None, atomic=True)
            #new_admin, new_admin_discriminator = new_admin.split("#")

            new_admin_pic = new_admin.avatar_url_as(size=1024)
            server_logo = guild.icon_url_as(size=1024)
            this_month_number = datetime.now().month
            this_month_name = calendar.month_name[this_month_number]

            myEmbed = discord.Embed(title = f"HEAD ADMIN FOR {this_month_name.upper()}!!!", description = "@everyone: This is an announcement declaring the new admin for this month", color = discord.Colour.dark_green())
            myEmbed.add_field(name = "NAME", value = f"@{new_admin} is now your new admin!", inline=False)
            myEmbed.add_field(name = "WHY", value = f"@{new_admin} Earned the support of the community, and as a result earned the most votes", inline=False)
            myEmbed.set_image(url = new_admin_pic)
            myEmbed.set_thumbnail(url = server_logo)
            myEmbed.set_footer(text="Made by @Shxjo")
            await context.send(embed = myEmbed)

        self.newadmin.stop()

def setup(bot):
    bot.add_cog(polls(bot))