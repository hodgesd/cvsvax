import re
import requests
from bs4 import BeautifulSoup

# Load FAA airfield paga
page = requests.get('https://nfdc.faa.gov/nfdcApps/services/ajv5/airportDisplay.jsp?airportId=rog')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
notams = View active <a href="(.+)"
print(soup.title.string)

# print(soup.find_all("div", class_="tab-content"))
mytabs = soup.find("ul", {"id": "myTabs"})
mytabs.find_all

print(mytabs)

# print(soup.span.prettify())

runway_name_list = soup.find(table_='table table-condensed table-borderless')
# runway_name_list_items = runway_name_list.find_all('a')

# for runway_name in runway_name_list_items:
#     print(runway_name.prettify())

# print(runway_name_list_items)
#
print(runway_name_list)
