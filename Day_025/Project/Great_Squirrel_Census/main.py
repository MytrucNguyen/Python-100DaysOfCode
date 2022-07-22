import csv
import pandas
import os
os.chdir(r"C:\Users\mytru\Documents\GitHub\Python-100DaysOfCode\Day_025\Project\Great_Squirrel_Census")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
print(gray)

cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon)

black = len(data[data["Primary Fur Color"] == "Black"])
print(black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", 'Black'],
    "Count": [gray , cinnamon, black],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")