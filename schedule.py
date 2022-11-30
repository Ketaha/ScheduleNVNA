import selenium.webdriver as WD
from time import sleep
from datetime import date
from argparse import ArgumentParser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

# CLI arguments
parser = ArgumentParser(description='Check schedule')
parser.add_argument('cg', type=str, help='number of group to test the schedule for')
parser.add_argument('-t', '--tomorrow', action='store_true', help='displays schedule for tomorrow')
args = parser.parse_args()

weekNumber = date.today().isocalendar().week

# Checks if day of request is EOW; if is makes request with next week
weekDay = date.today().isoweekday()
if weekDay >= 6:
    weekNumber+=1
    weekDay = 1
dayName = ['Неделя', 'Понеделник', 'Вторник', 'Сряда', 'Четвъртък', 'Петък', 'Събота']

weekDay += 1 if args.tomorrow == True else None

driver = WD.Edge()
driver.get("https://nvna.eu/wp/?group=%s&queryType=group&Week=%s" % (args.cg, str(weekNumber)))
element = driver.find_element(By.XPATH, "//*[contains(text(),'%s')]" % dayName[weekDay])
AC(driver).scroll_by_amount(0, element.location['y']).perform()

sleep(7)