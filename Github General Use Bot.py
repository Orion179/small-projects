import discord
import wikipedia
import beautifulsoup4
from discord.ext import commands
tkn='XXXXXXXXXXXXXXXXXXXXXXXX'

bot = commands.Bot(command_prefix='!', description="I'm here to give you information, videos, and much more!")

@bot.event #Let's host know that bot is running
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Mk 2, Ready for duty!')
    print('------')

@bot.command() #Will send a greeting in the caht
async def greet(ctx):
    await ctx.send(':wave: Hello, there!')

@bot.command() #Gives 30 result suggestions based on the words typed
async def search(ctx):
    result= str(wikipedia.search(ctx.message.content[7:], results=30))
    await ctx.send(result)

@bot.command() #Gives a summary of the words entered, then links user to full Wiki site
async def summary(ctx):
    result = (wikipedia.summary(ctx.message.content[9:], sentences=5))
    link = (wikipedia.page(ctx.message.content[9:]).url)
    await ctx.send(result)
    await ctx.send("For more information, check here: ")
    await ctx.send(link)

@bot.command() #Posts the description of the bot in the chat
async def aboutme (ctx):
    await ctx.send(bot.description)

@bot.command() #Lets user know about tags for the bot
async def info(ctx):
    await ctx.send(":smile: So here's the rundown:")
    await ctx.send('!greet: I will say hello!')
    await ctx.send("!aboutme: Learn a bit about me!")
    await ctx.send("!search: Type what you want me to find and I'll pull up relevant results")
    await cta.send("!summary: I'll provide some info on a specific items you type.")
    await ctx.send("!info: I will send this message again.")

#Runs the bot on start-up
bot.run(tkn)