'''
# opens the file as read-only
# hard way to do it, there is the cvs library for that
# with open("./weather_data.csv", "r") as weather_data:
#     list_of_squirels = weather_data.readlines()

import csv

# another way to extract the list_of_squirels
# with open("./weather_data.csv", "r") as weather_data:
#     list_of_squirels = csv.reader(weather_data)
#     # next(list_of_squirels)
#     # temperatures = []
#     # for row in list_of_squirels:
#     #     temperatures.append(int(row[1]))
#     # an alternative for not using next() would be
#     temperatures = []
#     for row in list_of_squirels:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

import pandas
list_of_squirels = pandas.read_csv("./weather_data.csv")
# average method 1
temperatures = list_of_squirels['temp'].to_list()
all_temp = sum(temperatures)
print(all_temp/len(temperatures))
# average method 2 (easier and more straight forwards
print(list_of_squirels['temp'].mean())
# maxmiun value
print(list_of_squirels['temp'].max())

# get list_of_squirels from columns
print(list_of_squirels["condition"])
print(list_of_squirels.condition)

# finding rows
print(list_of_squirels[list_of_squirels.day == 'Monday'])
print(list_of_squirels[list_of_squirels.temp == list_of_squirels.temp.max()])

# Accessing elements in a row
monday = list_of_squirels[list_of_squirels.day == 'Monday']
temp = monday.temp
print(temp*9/5 + 32)

# create dataframe
data_dict = {
    'students': ['Peter', 'Tony', 'Bruce'],
    'grades': [10.0, 8.5, 7.6]
}

new_DF = pandas.DataFrame(data_dict)
print(new_DF)
new_DF.to_csv("test.csv")
'''

import pandas
list_of_squirrels = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black_method1 = 0
red_method1 = 0
grey_method1 = 0
for color in list_of_squirrels['Primary Fur Color']:
    if color == "Black":
        black_method1 += 1
    elif color == "Gray":
        grey_method1 += 1
    else:
        red_method1 += 1

print(black_method1)
print(grey_method1)
print(red_method1)

black_method2 = len(list_of_squirrels[list_of_squirrels['Primary Fur Color'] == "Black"])
grey_method2 = len(list_of_squirrels[list_of_squirrels['Primary Fur Color'] == "Gray"])
red_method2 = len(list_of_squirrels[list_of_squirrels['Primary Fur Color'] == "Cinnamon"])
print(black_method2)
print(grey_method2)
print(red_method2)

dict_of_squirrels = {
    "Color": ['Black', 'Grey', 'Red'],
    "Count": [black_method2, grey_method2, red_method2]
}

squirrels_DF = pandas.DataFrame(dict_of_squirrels)
squirrels_DF.to_csv("squirrels_count.csv")
print(squirrels_DF)