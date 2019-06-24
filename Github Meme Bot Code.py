import discord
from discord.ext import commands
from random import randint
#XXXXXX is where you will enter your Discord Bot token
tkn='XXXXXXXXXXXXXXXXXXXXXXX'

#Creates the bot user
bot = commands.Bot(command_prefix='!', description='A bot that sends memes and meme accessories.')

#Used on start up to indicate bot is working, and shows relevant information
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('OwO We up in this piece!')
    print('------')

#When prompted, bot will send a greeting in the chat
@bot.command()
async def greet(ctx):
    await ctx.send(':wave: Hello, there!')

#When prompted, bot will link the chat to the meme of the day
@bot.command()
async def motd(ctx):
    await ctx.send("https://www.memecenter.com/top/daily")

#Runs the bot on start-up
bot.run(tkn)