import discord
from discord.ext import commands
from config import *
from app import *

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")


@bot.command(pass_context=True)
async def feedback(ctx):
    embed=discord.Embed(title="Yet Another Feedback System", url="https://127.0.0.1:5000/",
description="Welcome to the Yet Another Feedback System (YAFS)! Thanks for taking the time to fill out some feedback. To get started, [CLICK HERE](https://127.0.0.1:5000/)!",
color=0x33BBEE)
    await ctx.send(embed=embed)

bot.run(TOKEN)
