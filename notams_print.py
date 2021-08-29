import requests
import time
from bs4 import BeautifulSoup as BS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

from selenium import webdriver
import requests


# import re

# airfield = "krdr phnl"
airfield = input ("Enter airfields (separated by spaces): ")


url = 'https://www.notams.faa.gov/dinsQueryWeb/queryRetrievalMapAction.do'

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
fp.set_preference("pdfjs.disabled", True)

fp.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
fp.set_preference("print.always_print_silent", True)
fp.set_preference("print.show_print_progress", False)
fp.set_preference("browser.download.show_plugins_in_list",False)
fp.set_preference("print.tab_modal.enabled", False)
driver = webdriver.Firefox(fp)

driver.get('https://www.notams.faa.gov/dinsQueryWeb/')
agree_btn = driver.find_element_by_xpath("//button[@type='button']")
agree_btn.click()

# grab current id
window_before = driver.window_handles[0]
# print(window_before)

textbox = driver.find_element_by_xpath("/html/body/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td/form/table/tbody/tr/td[2]/table/tbody/tr[4]/td/textarea")
textbox.send_keys(airfield)
# textbox.send_keys(Keys.ENTER)
time.sleep(0.5)

submit_btn = driver.find_element_by_xpath("/html/body/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td/form/table/tbody/tr/td[2]/table/tbody/tr[5]/td/input[1]")
submit_btn.click()
time.sleep(0.5)

window_after = driver.window_handles[1]

print("*** before switch")
driver.switch_to.window(window_after)
print("*** after switch")

# driver.switch_to.window_after
driver.implicitly_wait(2) # gives an implicit wait for 2 seconds

# # # find and click print button
# print_btn = driver.find_element_by_xpath("/html/body/form/div/table/tbody/tr[1]/td/table[1]/tbody/tr[2]/td[1]/input[1]")
# print_btn.click()
driver.execute_script("window.print();")
time.sleep(0.5)
pyautogui.hotkey("command", "p")
time.sleep(0.5)
pyautogui.write(airfield)
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(0.5)
# time.sleep(3)
print("*** before press")

# select 'save to pdf' by arrowing up 3x
# pyautogui.press("up")
# time.sleep(0.5)
# pyautogui.press("up")
# time.sleep(0.5)
# pyautogui.press("up")
# time.sleep(0.5)
# pyautogui.press("enter")


# find and click save button
# save_btn = driver.find_element_by_xpath("/html/body/form/div/table/tbody/tr[1]/td/table[1]/tbody/tr[2]/td[1]/input[2]")
# save_btn.click()
# time.sleep(0.5)
# pyautogui.press("enter")

print("*** after press")
#
# driver.switch_to_window(window_before)
time.sleep(0.5)

# driver.quit()


# driver.SwitchTo().Window(driver.WindowHandles.Last())

#
# actions = ActionChains(driver)
# # actions.send_keys(Keys.COMMAND, "p")
# actions.send_keys(Keys.ARROW_UP)
# actions.send_keys(Keys.ENTER)
# actions.perform()
