#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" python3

# <bitbar.title>CVS Vax</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>MajorDouble</bitbar.author>
# <bitbar.author.github>your-github-username</bitbar.author.github>
# <bitbar.desc>Checks CVS for COVID vaccine availability in Belleville IL.</bitbar.desc>
# <bitbar.image>http://www.hosted-somewhere/pluginimage</bitbar.image>
# <bitbar.dependencies>requests, beautiful soup</bitbar.dependencies>
# <bitbar.abouturl>http://url-to-about.com/</bitbar.abouturl>
# <bitbar.droptypes>Supported UTI's for dropping things on menu bar</droptypes.abouturl>
# <swiftbar.hideAbout>true</swiftbar.hideAbout>
# <swiftbar.hideRunInTerminal>true</swiftbar.hideRunInTerminal>
# <swiftbar.hideLastUpdated>false</swiftbar.hideLastUpdated>
# <swiftbar.hideDisablePlugin>false</swiftbar.hideDisablePlugin>
# <swiftbar.hideSwiftBar>false</swiftbar.hideSwiftBar>

import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver


# Walgreens source data website to scrape
url = 'https://www.walgreens.com/findcare/vaccination/covid-19/location-screening'

# payload ={
#     "credentials": "include",
#     "headers": {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0",
#         "Accept": "application/json, text/plain, */*",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Content-Type": "application/json; charset=utf-8",
#         "X-XSRF-TOKEN": "4RrdpwclwO4dTQ==.q34NgCRJ9J+YjgxAPUZqnzh8CnKCIy8l51gWe9foN5U="
#     },
#     "referrer": "https://www.walgreens.com/findcare/vaccination/covid-19/location-screening",
#     "body": "{\"serviceId\":\"99\",\"position\":{\"latitude\":38.4744782,\"longitude\":-89.99067339999999},\"appointmentAvailability\":{\"startDateTime\":\"2021-02-23\"},\"radius\":25}",
#     "method": "POST",
#     "mode": "cors"
# }

# Request results

driver = webdriver.Firefox()
# driver.post(url, params = payload)
# p_element = driver.find_element_by_id(id_='inputLocation')
print(driver.content)
# results = requests.post(url, params = payload)
# print(results.content)

# Results parsed by BS
# soup = BS(results.content, "html.parser" )
# print (soup.prettify)

# # Regex query to find local status
# belleville = re.search('BELLEVILLE.+?status":"(.+?)"', soup.text)
# asof = re.search('currentTime":"(.+?)"', soup.text)
#
# date_time_str = asof.group(1)
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%f')

# print('Date:', date_time_obj.date())
# print('Date-time:', date_time_obj)

#
# vaxout = ":worried:"
# vaxin = ":smile:"
# lastvax = ""
# vaxintime = ""
#
# if belleville.group(1) == "Fully Booked":
#   status = vaxout
# else:
#   status = vaxin
#   vaxintime = asof
#   lastvax = ":exclamation:"
#
#
#
# print (":syringe:" + status + lastvax +"| symbolize = false")
# # print (":bandage.fill:" + "| symbolize = true"+status)
# print ("---")
# print (status+" Belleville CVS: "+belleville.group(1))
#
# # print (" | symbolize = false")
# print('As Of:', date_time_obj.time())
# print (":exclamation:Last in: " + vaxintime)
#
#
# await fetch("https://www.walgreens.com/dthandler/?dtCookie=2%244EJAJN0E05NUEQ95TN90JI98HM293MB4%7C0eed2717dafcc06d%7C1;dtLatC=1;referer=https%3A%2F%2Fwww.walgreens.com%2Ffindcare%2Fvaccination%2Fcovid-19%2Flocation-screening;visitID=GKSVQSGVQMLTQRKGQPCIDGAANNOBMLKI-0;app=0eed2717dafcc06d;crc=697378566;end=1",
#
# {
#     "credentials": "include",
#     "headers": {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0",
#         "Accept": "*/*",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Content-Type": "text/plain;charset=UTF-8"
#     },
#     "referrer": "https://www.walgreens.com/findcare/vaccination/covid-19/location-screening",
#     "body": "$a=1%7C10%7C_event_%7C1614033635185%7C_wv_%7CAAI%7C1%7CfIS%7C8251%7CfID%7C4$svrid=2$rId=RID_563679044$rpId=-1642367519$domR=1614033628334$tvn=%2Ffindcare%2Fvaccination%2Fcovid-19%2Flocation-screening$tvt=1614033626930$md=mdcc1%2Cfnyfz54x3qn0stdlwl4dfvsc$url=https%3A%2F%2Fwww.walgreens.com%2Ffindcare%2Fvaccination%2Fcovid-19%2Flocation-screening$title=COVID-19%20Vaccination%20%7C%20Walgreens%20Find%20Care$latC=1$app=0eed2717dafcc06d$visitID=GKSVQSGVQMLTQRKGQPCIDGAANNOBMLKI-0$vs=2$fId=33627627_17$v=10209210209190404$vID=161403359217605M17T6MS0TOBEQ4S8LOLQ9DE8N4SF36$time=1614033637195",
#     "method": "POST",
#     "mode": "cors"
# }
#
# await fetch("https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability", {
#     "credentials": "include",
#     "headers": {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0",
#         "Accept": "application/json, text/plain, */*",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Content-Type": "application/json; charset=utf-8",
#         "X-XSRF-TOKEN": "4RrdpwclwO4dTQ==.q34NgCRJ9J+YjgxAPUZqnzh8CnKCIy8l51gWe9foN5U="
#     },
#     "referrer": "https://www.walgreens.com/findcare/vaccination/covid-19/location-screening",
#     "body": "{\"serviceId\":\"99\",\"position\":{\"latitude\":38.4744782,\"longitude\":-89.99067339999999},\"appointmentAvailability\":{\"startDateTime\":\"2021-02-23\"},\"radius\":25}",
#     "method": "POST",
#     "mode": "cors"
# });
