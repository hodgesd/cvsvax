import requests
import json

v = requests.get("https://idph.illinois.gov/DPHPublicInformation/api/COVIDExport/GetVaccineAdministration?countyName=Illinois")

data = v.json()
t = data[-1]
tVacPct = "{:.1%}".format(t['PctVaccinatedPopulation'])
tRawSome = t['AdministeredCount']
tRawAll = t['PersonsFullyVaccinated']
tRawOne = tRawSome - tRawAll
ILpop = 12741080.0
tOnePct = "{:.1%}".format(tRawOne / ILpop)

print ("IL - Full: %s One: %s"  % (tVacPct, tOnePct))
print ("US - Full: %s One: %s"  % (tVacPct, tOnePct))
