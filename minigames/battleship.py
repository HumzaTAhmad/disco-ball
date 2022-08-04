
from main import discord, commands, bot


class battleship(commands.Cog):

    def _init_(self, bot):
        self.bot = bot
        self.playing = False
        self.board1 = ""
        self.board2 = ""
        self.boardtoshow1 = ""
        self.boardtoshow2 = ""

    @commands.command()
    async def render(self, context, board):
        numbers = [":one:",":two:",":three:",":four:",":five:",":six:",":seven:",":eight:",":nine:",":ten:"]

        alphabets = [":regional_indicator_a:",":regional_indicator_b:",":regional_indicator_c:",":regional_indicator_d:",":regional_indicator_e:",":regional_indicator_f:",":regional_indicator_g:",":regional_indicator_h:",":regional_indicator_i:",":regional_indicator_j:"]

        stringboard = ""

        stringboard = stringboard + ":black_medium_small_square:"
        for x in range(len(board[0])):
            stringboard = stringboard + alphabets[x]
        stringboard = stringboard + "\n"

        i = 0
        for row in board:
            stringboard = stringboard + numbers[i]
            i = i + 1
            for square in row:
                stringboard = stringboard + square
            stringboard = stringboard + "\n"

        await context.send(stringboard)

    [[":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:"],
    [":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:"],
    [":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:"],
    [":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:"],
    [":blue_square:", ":blue_square:",":blue_square:",":blue_square:",":blue_square:"]]

    @commands.command()
    async def battleships(self, context, player2: discord.Member, ver: int = 5, hor: int=5):
        self.playing = True
        self.player1 = context.author
        self.player2 = player2
        self.board1 = [[":blue_square:"]*hor for x in range(ver)]
        self.board2 = [[":blue_square:"]*hor for x in range(ver)]
        self.boardtoshow1 = [[":blue_square:"]*hor for x in range(ver)]
        self.boardtoshow2 = [[":blue_square:"]*hor for x in range(ver)]
        await self.render(self.player1, self.board1)
        await self.render(self.player2, self.board2)

def setup(bot):
    bot.add_cog(battleship(bot))