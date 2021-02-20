from pathlib import Path
import re
import json
import requests

# needs: optional TCM regex, airtable add record, drafts planning note template, create travel appointment, optional notification to robin


tripFile = open('/Users/derrickhodges/trip_notification.txt')
tripContent = tripFile.read()
print(tripContent)

legRegex = re.compile(r'0{5,}(\d+)\s+(N\d{2}EL)\s+(\D+)\s(\d+:\d+)\s+(\D+)\s+(\d+:\d+)\s+(\d+:\d+)\s+(\d)\s+(\D{2,3})\s*,\s(\D{2,3})')

leg = legRegex.search('000000002092	N57EL	STL 13:00	MDW 13:43	00:43	2	SDT, DDH')

destination = leg.group(5)
tail = leg.group(2)
PIC = leg.group(9)
SIC = leg.group(10)

print('PFR ' + tail + " "+destination)
print('PIC: '+PIC)
print('SIC: '+SIC)

legs = legRegex.findall(tripContent)
print (legs[0][4])
print (legs)

icaoRegex = re.compile(r'L.(\w{3,4})\s\d+[^00]:\d+[00].\D')


dateRegex = re.compile(r'Subject: Crew Notifications for .{6}(\d{2}/\d{2}/\d{4}) (through (\d{2}/\d{2}/\d{4}))?')
dates = dateRegex.search(tripContent)
deptdate = dates.group(1)

returndate = dates.group(3)
if returndate is None:
    returndate = deptdate
# print (deptdate.group(2), deptdate.group(3))
print (deptdate, returndate)

icaos = icaoRegex.findall(tripContent)
print (icaos)

# Add record to Airtable database.
airURL = 'https://api.airtable.com/v0/appA3FkMFarowhqUc/EHI%20Trip%20Log'
airHeaders = {
  'Authorization': 'Bearer keyaEXqTnN3W2LhwO',
  'Content-Type': 'application/json'}
payload = {'fields': {
  'Departure': deptdate,
  'Return Date': returndate}}
r = requests.post(airURL, headers=airHeaders, data=json.dumps(payload))

