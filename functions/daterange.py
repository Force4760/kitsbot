#import modules
import time
from .timeconvert import tcon
from .daysinmonth import daysInMonth
from datetime import date, datetime

def dateRange():
    #get time
    timeStrMe = tcon(time.time())
    timeListMe = list(timeStrMe.split(" "))
    dayMe = int(timeListMe[1])

    #get 1st and last day
    if dayMe >= 7:
        return f"{dayMe-6} - {dayMe}"
    else:
        #number of days in last month
        now = datetime.now()
        month = now.month
        if month == 1:
            month = 13
        newDay = daysInMonth(month-1)
        return f"{newDay - (7-dayMe) + 1} - {dayMe}"