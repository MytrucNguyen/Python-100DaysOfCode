import os
os.chdir(r"C:\Users\mytru\Documents\GitHub\Python-100DaysOfCode\Day_025\Notes\Reading_CSV")

import csv
import pandas
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []

    for row in data:
        if row[1] != "temp": 
            temperatures.append(int(row[1]))
    print(temperatures)

# python
data = pandas.read_csv("weather_data.csv")
print(data["temp"])