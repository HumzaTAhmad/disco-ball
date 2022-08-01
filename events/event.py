from main import commands, bot
    
txt_file = open("profanity.txt", "r")
badwords = txt_file.readlines()


class event(commands.Cog()):

    def _init_(self, bot):
        self.bot = bot

    

