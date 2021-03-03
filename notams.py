import requests
from bs4 import BeautifulSoup as BS
# import re

url = 'https://www.notams.faa.gov/dinsQueryWeb/queryRetrievalMapAction.do'

# agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0'}

header ={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Content-Type': 'application/x-www-form-urlencoded',
'Referer': 'https://www.notams.faa.gov/dinsQueryWeb/',
'Upgrade-Insecure-Requests': '1',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0'
}

data ={
'reportType=Report&retrieveLocId=kstl+kiad&actionType=notamRetrievalByICAOs&submit=View+NOTAMs'
}

# payload = {header,data}

payload2 = {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0"
    },
    "referrer": "https://www.notams.faa.gov/dinsQueryWeb/",
    "body": "reportType=Report&retrieveLocId=kstl+kiad&actionType=notamRetrievalByICAOs&submit=View+NOTAMs",
    "method": "POST",
    "mode": "cors"
}

results = requests.post(url, params=payload2)
soup = BS(results.content, "html.parser")
print(soup.prettify())
# belleville = re.search('BELLEVILLE.+?status":"(.+?)"', soup.text)
# print (belleville.group(1))

# await fetch("https://www.notams.faa.gov/dinsQueryWeb/queryRetrievalMapAction.do", {
#     "credentials": "include",
#     "headers": {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Upgrade-Insecure-Requests": "1",
#         "Cache-Control": "max-age=0"
#     },
#     "referrer": "https://www.notams.faa.gov/dinsQueryWeb/",
#     "body": "reportType=Report&retrieveLocId=kstl+kiad&actionType=notamRetrievalByICAOs&submit=View+NOTAMs",
#     "method": "POST",
#     "mode": "cors"
# });
#
#
