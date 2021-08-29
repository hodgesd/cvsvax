from colorama import Fore, Back, Style
import re

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

width = 80
length = 6000
pcn = "21/F/Z/C"
wbc = "30,600"
grvd = "GRVD"

r = Strip(length, width, pcn, wbc, grvd)
r.l()
r.w()
r.g()
r.p()
r.d()
