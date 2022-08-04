
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
        await self.player1.send("Welcome to Battleships! Type !place to place your ships")
        await self.player2.send("Welcome to Battleships! Type !place to place your ships")

    def shipcount(self, board):
        count = 0
        for row in board:
            for square in row:
                if square == ":ship:":
                    count = count + 1
                    
        return count

    @commands.command()
    async def place(self, context, *coordinates): #*coordinates stores inputs in tuple
        if self.playing == True:
            if context.author == self.player1:
                board = self.board1
            if context.author == self.player2:
                board = self.board2

            for coordinate in coordinates:
                if self.shipcount(board) == 6:       # type: ignore
                    await context.send("You are only allowed to have 6 ships")
                alphabet = coordinate[0].lower()
                number = coordinate[1]
                x = ord(alphabet) - 97 #allows alpahbet a to start at 0
                y = int(number) - 1
                board[y][x] = ":ship:"               # type: ignore
            await self.render(context.author,board)  # type: ignore


    [[":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:"],
    [":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:"],
    [":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:"],
    [":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:", ":blue_square:"],
    [":blue_square:", ":blue_square:",":blue_square:",":blue_square:",":blue_square:"]]

def setup(bot):
    bot.add_cog(battleship(bot))