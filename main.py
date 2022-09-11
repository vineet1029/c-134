import csv
import pandas as pd

rows = []

with open("star_with_gravity.csv","r") as f :
  csvR = csv.reader(f)
  for row in csvR :
    rows.append(row)

header = rows[0]
planetData = rows[1:]

header[0] = "Index"

distance = []

for data in planetData :
    if float(data[2]) < 100 :
        distance.append(data)

print(len(distance))

gravity = []
for data in planetData :
    if float(data[5]) < 150 or float(data[5]) > 350:
        gravity.append(data)

print(len(gravity))

final_list = []
for data in distance :
    if data in gravity:
        final_list.append(data)


with open("Pro-134(f).csv","a+") as f :
    csvW = csv.writer(f)
    csvW.writerow(header)
    csvW.writerows(final_list)
