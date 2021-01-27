#import modules
from datetime import date, datetime


def daysInMonth(month1):
    #get time
    now = datetime.now()
    year1 = now.year
    if month1 == 12:
        return (date(year1+1, 1, 1) - date(year1, month1, 1)).days
    else:
        return (date(year1, month1+1, 1) - date(year1, month1, 1)).days

