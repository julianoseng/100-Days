import pandas


# with open('weather_data.csv', 'r') as data_file:
#     weather_data = data_file.readlines()
#

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


# data = pandas.read_csv('weather_data.csv')
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# # avg_temp = sum(temp_list)/len(temp_list)
# # print(avg_temp)
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
# # Get data in columns
# print(data['condition'])
# print(data.condition)

# # Get data in Row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# print((monday.temp * 1.8) + 32)

# # create dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')


sqrl_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey_sqrl_count = len(sqrl_data[sqrl_data["Primary Fur Color"] == 'Gray'])
red_sqrl_count = len(sqrl_data[sqrl_data["Primary Fur Color"] == 'Cinnamon'])
black_sqrl_count = len(sqrl_data[sqrl_data["Primary Fur Color"] == 'Black'])

fur_colors = sqrl_data['Primary Fur Color']
sqrl_data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_sqrl_count, red_sqrl_count, black_sqrl_count]
}


print(sqrl_data_dict)

df = pandas.DataFrame(sqrl_data_dict)
df.to_csv("squirrel_count.csv")
