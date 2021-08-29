import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore, Back, Style

class Strip:
    def __init__(self,length,width,pcn,wbc,grvd):
        self.length=length
        self.width=width
        self.pcn=pcn
        self.wbc=wbc
        self.grvd=grvd

    def w(self):
        if self.width < 75:
            print(Back.RED + str(self.width)+"'"+Style.RESET_ALL, end=" ")
            pass
        elif self.width < 100:
            print(Back.YELLOW + str(self.width)+"'"+Style.RESET_ALL, end=" ")
    def l(self):
        if self.length < 5000:
            print(Back.RED + str(self.length)+"'"+Style.RESET_ALL, end="x")
            pass
        elif self.length <= 6000:
            print(Back.YELLOW + str(self.length)+"'"+Style.RESET_ALL, end="x")
        elif self.length >6000:
            print(str(self.length)+"'", end="x")
    def d(self):
        result = re.search(r"(\d+),", self.wbc)
        self.wbc = int(result.group(1))
        if self.wbc < 80:
            print(Back.RED+"D" + str(self.wbc)+Style.RESET_ALL)
            pass
        elif self.wbc < 96:
            print(Back.YELLOW+"D" + str(self.wbc)+Style.RESET_ALL)
        elif self.wbc >= 96:
            print("D" + str(self.wbc))
    def g(self):
        if self.grvd == "GRVD":
            print("GRVD", end=" ")
        elif self.grvd == "":
            print(Back.RED+"GRVD"+Style.RESET_ALL, end=" ")
        else:
            print(Back.YELLOW+self.grvd+Style.RESET_ALL, end=" ")
    def p(self):
        result = re.search(r"(.+)/(.+)/(.+)/(.+)", self.pcn)
        acn = int(result.group(1))
        x = result.group(2)
        y = result.group(3)
        z = result.group(4)
        if acn < 24:
            print(Back.RED+str(acn)+Style.RESET_ALL, end="/")
        elif acn >= 24:
            print(self.acn, end="/")

        print(x, end="/")

        if y=="Y":
            print(Back.YELLOW+y+Style.RESET_ALL, end="/")
        elif y=="Z":
            print(Back.RED+y+Style.RESET_ALL, end="/")

        print(z, end=" ")


# Prompt for airport input and build FAA url
airport = input("Airfield: ")
base = "https://nfdc.faa.gov/nfdcApps/services/ajv5/airportDisplay.jsp?airportId="
url=base+airport

# Get and parse current FAA data with soup
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")

icao = soup.find("span", {"style":"font-size: 24px; font-weight: 900;"}).text

name = soup.find('title').text

# runways = soup.find_all("div", {"class":"tab-pane active"})

runways = soup.find_all('div', {'id': re.compile(r'runway')})

for runway in runways:
    rwy = runway.find("span").text
    rw = re.sub(r"RUNWAY", "", rwy)

    dimension = runway.find_all("td")[1].text
    #remove whitespace
    dim = " ".join(dimension.split())
    result = re.search(r"(\d+) ft\. x (\d+) ", dim)
    length = result.group(1)
    width = result.group(2)
    pcn = soup.find("td", text="PCN").find_next_sibling("td").text
    p = " ".join(pcn.split())
    treatment = soup.find("td", text="Treatment").find_next_sibling("td").text
    doublewheel = soup.find("td", text="Double Wheel").find_next_sibling("td").text

    d_result = re.search(r"(\d+),", doublewheel)
    d = d_result.group(1)

    print(rw+":",length+"'","x",width+"'",p, "D"+d,treatment)

    # elevs = soup.find_all('di', {'id': re.compile(r'Elevation')})
    half = runway.find_all('div', {'id': re.compile(r'Base')})
    print(runway)


    # appr_elev = appr.find("td", text="Elevation").find_next_sibling("td").text
    # print ("")
    # print ("Approach end elevation: "+appr_elev)

atct = soup.find("td", text="Control Tower").find_next_sibling("td").text
atct = " ".join(atct.split())

if atct == "Airport traffic control tower":
    atct = "ATCT"
elif atct=="":
    atct = "No ATCT"
opr = soup.find("td", text="Tower Hours").find_next_sibling("td").text

arff = soup.find("td", text="Fire and Rescue").find_next_sibling("td").text

print ("ICAO:", icao,"-",name)
print ("A/FD:", atct, opr)
