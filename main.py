import os

import discord
from discord.ext import commands

description = "A bot for our uni's videogames competition."

intents = discord.Intents.default()

bot = commands.Bot(command_prefix=['!', '$'], description=description, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


bot.run(os.getenv("UniCompetitionBot"))
