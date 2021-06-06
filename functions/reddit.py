#Importing modules

from .loopsub import loopSub
from .subtt import subtt


def askReddit(reddit,drum:bool=True,loop:bool=True, drumMin:int=20,loopMin:int=10):
    #Connection to reddit
    output = []
    if drum:
        output.append(drums(reddit, drumMin))
    if loop:
        output.append(loops(reddit, loopMin))
    return output

def drums(reddit, min):
    #r/Drumkits Subreddit
    dksub = reddit.subreddit("drumkits")
    #Drum kits
    dkKits = loopSub(dksub, min)
    dkKits = subtt(dkKits)
    return dkKits

def loops(reddit, min):
    #r/Loopkits Subreddit
    lksub = reddit.subreddit("loopkits")  
    #Loop kits
    lkKits = loopSub(lksub, min) 
    lkKits = subtt(lkKits)
    return lkKits