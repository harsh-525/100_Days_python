# data = []
# with open('weather_data.csv', mode='r') as file:
#     content = file.readlines()  # read each lines and store as a list
#
# for _ in content:
#     data.append(_.strip())
#
# print(data)

# inbuilt libraries
# import csv
#
# with open('weather_data.csv', mode='r') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#         print(row)
#
# print(data, temperatures)
# all the above to just get single col data

# comes panda

import pandas
data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data['temp'])
print(data)
# data_dict = data.to_dict()  # data frame sample conversion
# # print(data_dict)
# print(data['temp'].to_list())  # series sample conversion
# print(data['temp'].mean())
# print(data.condition)  # DF treats cols more like a obj
#
# how to get data in rows
print(data[data['day'] == 'Monday'])
#
# print(data[data.temp == data.temp.max()])  # which row has the highest temp

# monday_temp = int(data[data.day == 'Monday'].temp)
# print(monday_temp * 9/5 + 32)

# how to create a DataFrame from scratch
# data_dict = {
#     'name': ['a', 'b'],
#     'id': [25, 29]
# }
# a = pandas.DataFrame(data_dict)
# a.to_csv("practice_data")




