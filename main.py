#Importing modules
import praw
import time
from functions.timeconvert import tcon
from functions.loopsub import loopSub
from functions.subtt import subtt
from functions.makemail import makeMail
from functions.mail import send
from secret.passw import c_id, c_secret, agent

#Connection to reddit
reddit = praw.Reddit(client_id=c_id,
                     client_secret=c_secret,
                     user_agent=agent)
#r/Drumkits Subreddit
dksub = reddit.subreddit("drumkits")

#r/Loopkits Subreddit
lksub = reddit.subreddit("loopkits")

#Drum kits
dkKits = loopSub(dksub, 15)
dkKits = subtt(dkKits)

#Loop kits
lkKits = loopSub(lksub, 10)    
lkKits = subtt(lkKits)

#Make email from template
mail = makeMail(dkKits, lkKits)

#get time
timeStrMe = tcon(time.time())
timeListMe = list(timeStrMe.split(" "))
dayMe = timeListMe[1]

#send it
send(mail, dayMe)






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
# Description: Reddit bot for emailing drum/loop kits         #  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 