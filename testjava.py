import requests
from bs4 import BeautifulSoup
from selenium import webdriver

my_url = 'https://avi.im/stuff/js-or-no-js.html'

driver = webdriver.Firefox()
driver.get(my_url)
p_element = driver.find_element_by_id(id_='intro-text')
print(p_element.text)
# print(soup.find(id="intro-text"))


# Result:
# <p id="intro-text">No javascript support</p>
