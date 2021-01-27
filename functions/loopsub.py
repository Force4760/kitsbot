#import modules
import time
from functions.timeconvert import tcon
from functions.daysinmonth import daysInMonth
from datetime import date, datetime

def loopSub(sub, minimum):
    kitlist = []
    #get actual time
    timeStrMe = tcon(time.time())
    timeListMe = list(timeStrMe.split(" "))
    dayMe = int(timeListMe[1])
    #for every post (max 10)
    for post in sub.new(limit=100):
        #get the post score
        score = post.score

        #If the score is "good"
        if score >= minimum:
            title = post.title
            date = post.created_utc
            author = post.author
            link = post.url

            #convert post time
            timeStr = tcon(date)
            timeList = list(timeStr.split(" "))

            #get the day
            dayPost = int(timeList[1])

            #if more than a week has passed since the beggining of the month
            if dayMe >= 7:
                #if in last week
                if (dayPost >= dayMe - 6) and (dayPost <= dayMe):
                    kitlist.append([title, timeStr, author, link])
            else:
                #number of days in last month
                now = datetime.now()
                month = now.month
                if month == 1:
                    month = 13
                newDay = daysInMonth(month-1)

                #if in last week
                if (dayPost >= 1) and (dayPost <= dayMe):
                    kitlist.append([title, timeStr, author, link])
                
                if (dayPost > newDay - (7-dayMe)) and (dayPost <= newDay):
                    kitlist.append([title, timeStr, author, link])
    return kitlist