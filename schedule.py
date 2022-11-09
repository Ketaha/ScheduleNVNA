from time import sleep
from webbrowser import open
from datetime import date

weekNumber = date.today().isocalendar().week

# Checks if day of request is EOW; if is makes request with next week
weekDay = date.today().isoweekday()
if weekDay >= 6:
    weekNumber+=1

open("https://nvna.eu/wp/?group=128211&queryType=group&Week=%s" % str(weekNumber))
sleep(1)