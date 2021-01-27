import random

from discord.ext import commands


class LoL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #commands
    @commands.command()
    async def pantheon(self, ctx):
        """
                A method that sends a random quote from pantheon.
                Parameters:
                    ctx (commands.Context): The invocation context.
                Output:
                     A random quote from Pantheon.
                Returns:
                    None.
                """
        quotes = [
            '"In battle, we are reborn"',
            '"Flee, and the spear will find your back."',
            '"I fight until the blood takes the spear from my grasp, until I can only crawl. And even then, you will not '
            'defeat me, even then, I will spit in your face!"',
            '"Let this day be legend."',
            '"My name is Soldier. By my spear, they will know war."',
            '"They are called gods, but when they die you cannot hear their howls above the wind."',
            '"Brother to warriors resting beneath wheat. Son of battles a thousand times lost. I know who I am, '
            'and I will show the gods what I can become!"',
            ''"Shields defend hearts. Both yours, and those beside you."'',
            '"We cry out to the heavens... and they answer in wing and flame."',
            '"Aatrox has slaughtered gods. But now, he faces a man."',
            '"I am no more than a soldier, and no less."',
            '"Our destiny is to fight, and only the bravest do not refuse it. I understand this, Lunari."',
            '"It is not why I fight, but who I fight for."',
            '"I cast my excuses into the dirt."',
            '"The earth is beneath me."',
            '"Onward! The spear points in only one direction."',
            '"Death is the only thing that ever embraced me."',
            '"We are what we overcome."',
            '"A clashing of steel... I have heard it all go silent."',
            '"I wield my fate as a weapon!"',
            '"Pressing forward is not the same as running from your mistakes."',
            '"If they bleed I will call them sister or brother."',
            '"The world moves as the heavens lie still."'
            '"Because we fall, the climb must be our destination."',
            '"I wear a helm so that I am only a soldier."',
            '"I will carve my scars into the heavens."',
            '"I buried regret in a grave, along with my name."',
            "The power of these 'gods' is but an echo of our own.",
            '"I do not set the pace, I race against it."',
            '"The past marches with me."',
            '"There are no enemies, no allies. Only those about to die"',
            '"From the skies they see war, but on earth there is only carnage."',
            '"The art of war is hearing your heart beating, knowing you are alive!"',
            '"If they kill me, at least I die a man."',
            '"I am the tip of the spear, raised against surrender!"',
            '"I have found my limit a thousand times, and still I press further."',
            '"The people cry out for strength that is already theirs!"',
            '"How much further could we march if we were not forced to carry our fears on our backs?"',
            '"We must all find our place. Mine is being cast down, so I can rise once more!"',
            '"We are privileged to breath, to taste the air! It is the last gasp of all who have died before us."',
            '"The stars are beyond my reach, and so I grasp my spear and take aim."',
            '"Heavier than my spear is the weight of only one life."',
            '"After every defeat, I ran around the mountain until even shame could not keep up."',
            '"Behind me lies a farm. I wonder if there is bread above the hearth, and if I will ever return."',
            '"Face me."',
            '"We bleed into the same earth, and bleed we must."',
            '"Why do you fight?"',
            '"Aatrox would drown the world in blood just to stain the heavens."',
            '"Aatrox! The World Ender. But from death, comes life."',
            '"The power you sought has destroyed you, Aatrox. You will find no other end."',
            '"I am not the Pantheon you knew, creature. I am Atreus, a mortal, about to slay a dragon!"',
            '"I once trusted my destiny to the stars, dragon. Now, I trust in steel."',
            '"Battle is a dance, and the fortunate find their partner."',
        ]
        await ctx.send(random.choice(quotes))


def setup(bot):
    bot.add_cog(LoL(bot))