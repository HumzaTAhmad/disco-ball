
import string
from main import discord, commands, bot

class battleship(commands.Cog):

    def _init_(self, bot):
        self.bot = bot

    async def render(context, board):
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
