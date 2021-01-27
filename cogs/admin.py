from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #events
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True, read_message_history=True)
    @commands.command()
    async def deleteMessages(self, ctx, amount=5):
        """
                    A method that deletes messages from a channel.
                    Parameters:
                        ctx (commands.Context): The invocation context.
                        amount (int): the amount of messages to be deleted. the default is 5
                    Output:
                        None.
                    Returns:
                        None.
        """
        if amount >= 50:
            await ctx.send("Up to 50 messages can be deleted at one time")
        else:
            await ctx.channel.purge(limit=amount + 1)


def setup(bot):
    bot.add_cog(Admin(bot))