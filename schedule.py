from time import sleep
from datetime import date
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC

weekNumber = date.today().isocalendar().week
todayDate = date.today().day

# Checks if day of request is EOW; if is makes request with next week
weekDay = date.today().isoweekday()
if weekDay >= 6:
    weekNumber+=1

driver = webdriver.Edge()
driver.get("https://nvna.eu/wp/?group=128211&queryType=group&Week=%s" % str(weekNumber))

dayName = ['Понеделник', 'Вторник', 'Сряда', 'Четвъртък', 'Петък', 'Събота', 'Неделя']
element = driver.find_element(By.XPATH, "//*[contains(text(),'%s')]" % dayName[weekDay])
actions = AC(driver)
actions.scroll_by_amount(0, element.location['y']).perform()

sleep(10)