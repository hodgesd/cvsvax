# imports
import json
import requests

# Add record to Airtable database.

icaos = ['STL', 'MDW', 'PBI']
airURL = 'https://api.airtable.com/v0/appA3FkMFarowhqUc/EHI%20Trip%20Log'
airHeaders = {
  'Authorization': 'Bearer keyaEXqTnN3W2LhwO',
  'Content-Type': 'application/json'}
payload = {'fields': {
  'Departure': '2021-03-01',
  'ICAO': ['STL', 'MDW', 'PBI'],
  'Return Date': '2021-03-02'}}
r = requests.post(airURL, headers=airHeaders, data=json.dumps(payload))
print (r)
