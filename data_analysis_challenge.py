# Data Analysis Challenge

from readrides import read_rides_as_dicts
from collections import Counter
records = read_rides_as_dicts('Data/ctabus.csv')
# route: Column 0. The bus route name.
# date: Column 1. A date string of the form MM/DD/YYYY
# daytype: Column 2. A day type code (U=Sunday/Holiday, A=Saturday, W=Weekday)
# rides: Column 3. Total number of riders (integer)

# How many bus routes exist in Chicago? i.e. How many unique buses are there?
unique_buses = { record["route"] for record in records }
print(unique_buses)

# How many people rode the number 22 bus on February 2, 2011? 
# What about any route on any date of your choosing?
date = input("Select date: ")
valids = [record for record in records if record["route"] == '22' and record["date"] == date]
sum = 0
for entry in valids:
    sum += int(entry["rides"])
print(sum)

# What is the total number of rides taken on each bus route?
totals = Counter()
for record in records:
    totals[record["route"]] += int(record["rides"])
print(totals)

# What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
total2001 = Counter()
records2001 = [ record for record in records if "2001" in record["date"] ]
for record in records2001:
    total2001[record["route"]] += int(record["rides"])

total2011 = Counter()
records2011 = [ record for record in records if "2011" in record["date"] ]
for record in records2011:
    total2011[record["route"]] += int(record["rides"])

# Some bus routes were added between 2001 and 2011
# Some bus routes were discontinued between 2001 and 2011
# So only keep the routes that existed since 2001 and lasted until at least 2011

commonRoutes = set(total2001.keys()).intersection(total2011.keys())
diff = {}
for route in commonRoutes:
    diff[route] = total2011[route] - total2001[route]

import heapq
largest = heapq.nlargest(5, diff, key=diff.get)

for route in largest:
    print(f"Route {route}: {diff[route]} increase")