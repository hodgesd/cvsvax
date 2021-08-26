import requests
from bs4 import BeautifulSoup as BS
import re

url = 'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.IL.json?vaccineinfo'
# agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0'}
header ={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Referer': 'https://www.cvs.com/immunizations/covid-19-vaccine',
'Connection': 'keep-alive'
}
results = requests.get(url, headers = header)
soup = BS(results.content, "html.parser" )


belleville = re.search('BELLEVILLE.+?status":"(.+?)"', soup.text)
print (belleville.group(1))

vaxout = "nope"
vaxin = "yep"

if belleville.group(1) == "Fully Booked":
  status = vaxout
else:
  status = vaxin

print (status)

# print(x.group())# 
print (soup.prettify, 'lxml')

# print (BS(results.content, 'lxml'))
