
from main import discord, commands, bot


class battleship(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.playing = False
        self.board1 = ""
        self.board2 = ""
        self.boardtoshow1 = ""
        self.boardtoshow2 = ""
        self.turn = ""

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
        if self.playing == False:
            self.playing = True
            self.player1 = context.author #This is now in the constructor
            self.player2 = player2        #This is now in the constructor
            self.turn = self.player1
            self.board1 = [[":blue_square:"]*hor for x in range(ver)]
            self.board2 = [[":blue_square:"]*hor for x in range(ver)]
            self.boardtoshow1 = [[":blue_square:"]*hor for x in range(ver)]
            self.boardtoshow2 = [[":blue_square:"]*hor for x in range(ver)]
            await self.render(self.player1, self.board1)
            await self.render(self.player2, self.board2)
            await self.player1.send("Welcome to Battleships! Type !place to place your ships")
            await self.player2.send("Welcome to Battleships! Type !place to place your ships")
        else:
            await context.send("Game is already in progress.")

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
            if len(coordinates) == 0:
                await context.send("Please type in the coordinates.")
            else:
                for coordinate in coordinates:
                    if self.shipcount(board) == 6:       # type: ignore
                        await context.send("You are only allowed to have 6 ships")
                    alphabet = coordinate[0].lower()
                    number = coordinate[1]
                    x = ord(alphabet) - 97 #allows alpahbet a to start at 0
                    y = int(number) - 1
                    board[y][x] = ":ship:"               # type: ignore
                await self.render(context.author,board)  # type: ignore
        else:
             await context.send("Please start a game by typing !battleships.")
             
    @commands.command()
    async def shoot(self, context, coordinate):
        if self.turn == context.author:
            if self.playing == True:

                if context.author == self.player1:
                    boardtoshoot = self.board2
                    boardtoshow = self.boardtoshow2
                    previousshooter = self.player1
                    nextshooter = self.player2
                
                if context.author == self.player2:
                    boardtoshoot = self.board1
                    boardtoshow = self.boardtoshow1
                    previousshooter = self.player2
                    nextshooter = self.player1

                loweralphabet = coordinate[0].lower()
                number = coordinate[1]
                x = ord(loweralphabet) - 97
                y = int(number) - 1
                square = boardtoshoot[y][x]

                if square == ":ship:":
                    await context.send("Hit!")
                    boardtoshoot[y][x] = ":boom:"
                    boardtoshow[y][x] = ":boom:"
                
                if square == ":blue_square:":
                    await context.send("No Hit.")
                    boardtoshoot[y][x] = ":white_medium_square:"
                    boardtoshow[y][x] = ":white_medium_square:"
                    self.turn = nextshooter
                    await previousshooter.send("You turn has ended.")
                    await nextshooter.send("Its your turn to shoot.")
                
                if square == ":white_medium_square:" or square == ":boom:":
                    await context.send("You have already shot this square, try again.")
                
                await self.render(context.author, boardtoshow)

                if self.shipcount(boardtoshoot) == 0:
                    self.playing = False

                    if context.author == self.player1:
                        await self.player1.send("You have won the Game!")

                        await self.player2.send("You have lost the Game!")
                        await self.render(self.player2, self.board1)
                    
                    if context.author == self.player2:
                        await self.player2.send("You have won the Game!")

                        await self.player1.send("You have lost the Game!")
                        await self.render(self.player1, self.board2)
            else:
                await context.send("Please start a game by typing !battleships.")
        else:
            await context.send("Its not your turn!")

    @battleships.error
    async def errorhandler(self,context,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await context.send("Please mention the second player.")
    
    @shoot.error
    async def errorhandler(self,context,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await context.send("Please define the coordinate")
 
    @place.error
    async def errorhandler(self,context,error):
        if isinstance(error,commands.errors.CommandInvokeError):
            await context.send("Please type in a proper coordinate")

def setup(bot):
    bot.add_cog(battleship(bot))