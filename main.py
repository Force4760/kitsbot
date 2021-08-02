# imports
from functions.reddit import askReddit
import praw
import asyncio
import discord
from db.sql import *
from discord.ext import commands
from secret.passw import c_id, c_secret, agent, discordToken

# prefix
def get_prefix(client,message):
    return getP(str(message.guild.id))


# Connect to reddit
reddit = praw.Reddit(client_id=c_id,client_secret=c_secret,user_agent=agent)

# Connect to  discord
bot = commands.Bot(command_prefix = get_prefix)

# messages and constants
DIVDK = "*** ══════ DRUM KITS ══════ ***\n"
DIVLK = "*** ══════ LOOP KITS ══════ ***\n"
ERRORMSG = "Sorry! An Error occured."
STARTMSG = "***Gathering kits***"
ENDMSG = "***ALL CAPS WHEN U SPELL THE MAN'S NAME***"
SLEEP = 1
MSG = """
**════ WHO AM I ════ **
I'm a reddit/discord bot that a lazy music producer made so that he did not need to browse through reddit posts to find good kits.  

**════ WHO'S DOOM ════ **
DOOM (or MF DOOM) is one of the greatest rappers ever. Look it up, you wont regret it.
    
***════ Commands ════ ***
**>kits** : Best r/loopkits and r/drumkits kits
**>drums MinimunScore** : Best r/drumkits kits
**>loops MinimumScore** : Best r/loopkits kits
*MinimumScore is a number you can provide to change the minimum score a kits should have.*

***════ Socials ════ ***
**GitHub:** https://github.com/Force476
**SoundCloud:** https://soundcloud.com/g-force-beats
**Instagram: ** https://www.instagram.com/force_4760/
**Website: ** https://force4760.netlify.app/

***ALL CAPS WHEN U SPELL THE MAN NAME***
"""


@bot.event
async def on_guild_join(guild):
    insert(str(guild.id))


@bot.command()
@commands.has_permissions(administrator=True)
async def changePrefix(ctx,prefix):
    try:
        if prefix:
            
            changeP(str(ctx.guild.id), str(prefix))
            await ctx.channel.send(f"My prefix is now: {prefix}")
    except:
        await ctx.channel.send(ERRORMSG)


@bot.command()
async def DOOM(ctx):    
    await ctx.channel.send(MSG)

@bot.command()
async def drums(ctx, min=None):
    if not min:
        min = 20
    channel = ctx.channel
    await channel.send(STARTMSG)
    try:
        o = askReddit(reddit, drum=True, loop=False, drumMin=int(min))
        await channel.send(DIVDK)
        for kit in o[0]:
            await channel.send(kit)
            await asyncio.sleep(SLEEP)
        await channel.send(ENDMSG)
    except:
        await channel.send(ERRORMSG)

@bot.command()
async def loops(ctx, min=None):
    if not min:
        min = 10
    channel = ctx.channel
    await channel.send(STARTMSG)
    try:
        o = askReddit(reddit, drum=False, loop=True, loopMin=int(min))
        await channel.send(DIVLK)
        for kit in o[0]:
            await channel.send(kit)
            await asyncio.sleep(SLEEP)
        await channel.send(ENDMSG)
    except:
        await channel.send(ERRORMSG)

@bot.command()
async def kits(ctx):
    channel = ctx.channel
    await channel.send(STARTMSG)
    try:
        o = askReddit(reddit, drum=True, loop=True)
        await channel.send(DIVDK)
        for kit in o[0]:
            await channel.send(kit)
            await asyncio.sleep(SLEEP)
        await channel.send(DIVLK)
        for kit in o[1]:
            await channel.send(kit)
            await asyncio.sleep(SLEEP)
        await channel.send(ENDMSG)
    except:
        await channel.send(ERRORMSG)



bot.run(discordToken)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  _______     _______     _______      _______     _______   # 
# |  _____|   |  ___  |   |  ___  |    |  _____|   |  _____|  # 
# | |___      | |   | |   | |___| |    | |         | |_____   # 
# |  ___|     | |   | |   |  ___  |    | |         |  _____|  # 
# | |         | |___| |   | |   \ \    | |_____    | |_____   # 
# |_|         |_______|   |_|    \_\   |_______|   |_______|  # 
#                                                             # 
# Made by Force4760                                           # 
#                                                             # 
# Start Date: 27/1/2021                                       # 
# Description: Reddit/discord bot for sending drum/loop kits  #  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 