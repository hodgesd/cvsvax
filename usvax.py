import requests

wdata = requests.get("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.json")
w = wdata.json()

def function(json_object, name):
    return [obj for obj in json_object if obj['country']==name][0]['data']
    # return [obj for obj in w if obj['country']==Australia][0]['iso_code']

# def my_function():
#   print("Hello from a function")

# my_function()
us = function(w, 'United States')
usVacPct = us[-1]['people_fully_vaccinated_per_hundred']
usRawAll = us[-1]['people_fully_vaccinated']
usRawSome = us[-1]['total_vaccinations']
usRawOne = usRawSome - (usRawAll * 2)
usPop = 336008333.0
usOnePct = "{:.1%}".format(usRawOne / usPop)
# print ("IL Vax - Full: %s One: %s "  % (tVacPct, tOnePct))

print ("US Vax - Full: %s One: %s"  % (usVacPct, usOnePct))
