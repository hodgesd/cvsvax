import requests
from bs4 import BeautifulSoup

URL = "http://www.hkexnews.hk/sdw/search/searchsdw.aspx"

with requests.Session() as s:
    s.headers={"User-Agent":"Mozilla/5.0"}
    res = s.get(URL)
    soup = BeautifulSoup(res.text,"lxml")
    payload = {item['name']:item.get('value','') for item in soup.select("input[name]")}
    payload['__EVENTTARGET'] = 'btnSearch'
    payload['txtStockCode'] = '00001'
    payload['txtParticipantID'] = 'A00001'
    req = s.post(URL,data=payload,headers={"User-Agent":"Mozilla/5.0"})
    soup_obj = BeautifulSoup(req.text,"lxml")
    for items in soup_obj.select("#pnlResultSummary .ccass-search-datarow"):
        data = [item.get_text(strip=True) for item in items.select("div")]
        print(data)
