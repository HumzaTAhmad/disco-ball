import calendar

from main import discord, commands, bot
from datetime import datetime

class Announcement(commands.Cog):

    def _init_(self, bot):
        self.bot = bot

    @commands.command()
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

def setup(bot):
    bot.add_cog(Announcement(bot))