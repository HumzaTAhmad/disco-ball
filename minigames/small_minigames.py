import random
from main import discord, commands, bot



class smallMiniGames(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def RPS(self, context, hand):
        hands = ["✌️", "🤚", "✊"]
        bothand = random.choice(hands)
        
        await context.send(bothand)
        if hand == bothand:
            await context.send("Its a Draw!")
        elif hand == "✌️":
            if bothand == "🤚":
                await context.send("You Win!")
            elif bothand == "✊":
                await context.send("You Lose!")
        elif hand == "🤚":
            if bothand == "✊":
                await context.send("You Win!")
            elif bothand == "✌️":
                await context.send("You Lose!")
        elif hand == "✊":
            if bothand == "✌️":
                await context.send("You Win!")
            elif bothand == "🤚":
                await context.send("You Lose!")
                
    @commands.command()
    async def coinflip(self, context):
        num = random.randint(1,2)

        if num == 1:
            await context.send("Heads")
        elif num == 2:
            await context.send("Tails")

def setup(bot):
    bot.add_cog(smallMiniGames(bot))