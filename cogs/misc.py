import os
import random

import discord
from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #commands
    @commands.command()
    async def kickflip(self, destination):
        """
                     A method that sends a random picture of a kickflip to discord.
                     Parameters:
                         ctx (commands.Context): The invocation context.
                     Output:
                         Success: A random kickflip image is sent to discord.
                     Returns:
                         None.
        """
        path = './kickflipImages'
        choice = random.choice(os.listdir(path))
        await destination.send(file=discord.File(f'{path}\\{choice}'))

    @commands.command()
    async def ping(self, ctx):
        """
                             A method that sends a simple pong after a ping is recieved.
                             Parameters:
                                 ctx (commands.Context): The invocation context.
                             Output:
                                 Success: Pong is sent to chat.
                             Returns:
                                 None.
         """
        await ctx.send('Pong!')

    @commands.command(aliases=['8ball', 'test'])
    async def eightball(self, ctx, *, question):
        """
                             A method that simulates the magic 8 ball. .
                             Parameters:
                                 ctx (commands.Context): The invocation context.
                                 *
                                 question (str): The question that is sent t the bot.
                             Output:
                                 Success: The magic 8 ball sends a random answer to the question.
                             Returns:
                                 None.
        """
        responses = [
            'Ask again later.',
            'Better not tell you now',
            'Cannot predict now.',
            'Concentrate and ask again.',
            "Don't count on it",
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy',
            'Try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'Yes – definitely.',
            'You may rely on it.',
        ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


def setup(bot):
    bot.add_cog(Misc(bot))