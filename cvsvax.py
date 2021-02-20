import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.IL.json?vaccineinfo'
# agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0'}
header ={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Referer': 'https://www.cvs.com/immunizations/covid-19-vaccine',
'Connection': 'keep-alive'
}
page = requests.get(url, headers = header)
print (BS(page.content, 'lxml'))
