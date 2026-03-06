# 1. Using CSV module

# with open("weather_data.csv") as data:
# 	weather_info = data.readlines()
# 	print(weather_info)
# ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

# import csv

# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	for row in data:
# 		print(row)
# ['day', 'temp', 'condition']
# ['Monday', '12', 'Sunny']
# ['Tuesday', '14', 'Rain']
# ['Wednesday', '15', 'Rain']
# ['Thursday', '14', 'Cloudy']
# ['Friday', '21', 'Sunny']
# ['Saturday', '22', 'Sunny']
# ['Sunday', '24', 'Sunny']

# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	for row in data:
# 		print(row)

# Challenge - create a list with temperatures as integers
# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	temperatures = []
# 	for row in data:
# 		if row[1] != "temp":
# 			temperatures.append(int(row[1]))
# 	print(temperatures)

# This is quite a lot of code to get a single row of data. We can use the Pandas module to make things easier

# 2. Pandas module
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24
# Name: temp, dtype: int64

# print(type(data))
# <class 'pandas.core.frame.DataFrame'>
#
# print(type(data['temp']))
# <class 'pandas.core.series.Series'>

# data_dict = data.to_dict()
# print(data_dict)
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
#  'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
#  'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}
#  }

# temp_list = data["temp"].to_list()
# print(temp_list)
# [12, 14, 15, 14, 21, 22, 24]

# temp = 0
# for number in temp_list:
# 	temp += number
# average_temp = temp / len(temp_list)
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# 3. Built in Pandas methods

# Pandas has a built in method to get the average or mean of a Series
# average = data["temp"].mean()
# print(average)

# Challenge - get the maximum temp value using built in Pandas method
# print(data["temp"].max())

# 4. Extract data from columns

# print(data["condition"])
# 0     Sunny
# 1      Rain
# 2      Rain
# 3    Cloudy
# 4     Sunny
# 5     Sunny
# 6     Sunny
# Name: condition, dtype: object

# Alternative way to call each column is using its name
# print(data.condition)

# 5. Extract data from rows.
# print(data[data.day == "Monday"])
#       day  temp condition
# 0  Monday    12     Sunny

# Challenge - print out the row of data with the maximum temp
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])
#       day  temp condition
# 6  Sunday    24     Sunny

# print(data[data.temp == data.temp.max()])
#       day  temp condition
# 6  Sunday    24     Sunny

# We can extract a single value from a certain row
# max_temp = data[data.temp == data.temp.max()]
# print(max_temp.condition)
# 6    Sunny
# Name: condition, dtype: object

# Challenge - get and convert Monday temp to Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# f_temp = (monday_temp * 9/5) + 32
# print(f_temp)
# 53.6

# 6. Create a DataFrame from scratch
to_learn = {
	"students": ["Amy", "James", "Angela"],
	"scores": [76, 55, 65]
}
new_data = pandas.DataFrame(to_learn)
# print(new_data)
#   students  scores
# 0      Amy      76
# 1    James      55
# 2   Angela      65
new_data.to_csv("students_data.csv")
