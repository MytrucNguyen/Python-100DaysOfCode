import os
from sqlite3 import DataError
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

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# average 
# avg = sum(temp_list) / len(temp_list)
# print(avg)
print(data["temp"].mean())
max_temp = data.temp.max()

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp* 9/5 + 32
print(monday_temp_F)

# Creating from Scratch
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(DataError)
data.to_csv("new_data.csv")