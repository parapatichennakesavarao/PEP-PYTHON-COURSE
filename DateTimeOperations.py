import datetime
import math
"""current=datetime.datetime.now()
today=datetime.date.today()
current.date()
current.time()
current.year
print("Current Date and Time:",current)
print("Today's Date:",today)
print("Current Year:",current.year)"""

date1=datetime.date(2026,1,1)
date2=datetime.date(2026,1,29)
difference=math.fabs((date1 - date2).days)
print("Difference between",date1,"and",date2,"is",difference,"days")