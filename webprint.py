import time
from selenium import webdriver
import os

class printing_browser(object):
    def __init__(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
        self.profile.set_preference("pdfjs.disabled", True)
        self.profile.set_preference("print.always_print_silent", True)
        self.profile.set_preference("print.show_print_progress", False)
        self.profile.set_preference("browser.download.show_plugins_in_list",False)
        self.driver = webdriver.Firefox(self.profile)
        time.sleep(5)

    def get_page_and_print(self, page):
        self.driver.get(page)
        time.sleep(7)
        self.driver.execute_script("window.print();")

if __name__ == "__main__":
    print("in main")
    browser_that_prints = printing_browser()
    browser_that_prints.get_page_and_print('http://www.google.com/')
