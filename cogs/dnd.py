import random
import discord
import os

from discord.ext import commands

class DnD(commands.Cog):
    """
    A Cogs class that contains commands related to tabletop RPGs.

    Attributes: bot (commands.Bot) : The discord bot
    """
    def __init__(self, bot):
        self.bot = bot

    #commands
    @commands.command()
    async def roll(self, ctx, die):
        """
               A method to simulate the rolling of dice.
               Parameters:
                   ctx (commands.Context): The invocation context.
                   die (str): The dice being rolled. FE) 20d6 -> twenty six-sided dice.
               Output:
                   Success: The result of the die pattern rolled.
                   Failure: A message describing the proper format of a roll.
               Returns:
                   None.
               """
        try:
            sides = die.split('d')
            #split number by the d
            #sides [0] = number of dice
            #sides[1] is the number of sides the die hash
            rolls = [random.randrange(1, int(sides[1]) + 1) for _ in range (int(sides[0]))]
            #generate a list of numbers between 1 and sides[1] of length [0]
            await ctx.send(f' **Result:** {rolls}\n**Total:** {sum(rolls)}')
            #sends the result and total to discord
        except:
            await ctx.send('Try the format ".roll 3d6"')

    @commands.command()
    async def hots(self, ctx):
        """
                       Gets a potrait of a random character on demand from a folder.
                       Parameters:
                           ctx (commands.Context): The invocation context.
                       Output:
                           Success: A random character portrait is sent to discord.
                       Returns:
                           None.
                       """
        path = './hots'
        choiceFolder = random.choice(os.listdir(path))
        newPath = './hots/' + choiceFolder

        await ctx.send(file=discord.File(f'{newPath}\\Fulllength.png'))

    @commands.command()
    async def portrait(self, ctx):
        """
                              Gets a potrait of a random character on demand from a folder.
                              Parameters:
                                  ctx (commands.Context): The invocation context.
                              Output:
                                  Success: A random character portrait is sent to discord.
                              Returns:
                                  None.
                              """
        path = './dndPortraits'
        choice = random.choice(os.listdir(path))
        await ctx.send(file=discord.File(f'{path}\\{choice}'))


def setup(bot):
    bot.add_cog(DnD(bot))