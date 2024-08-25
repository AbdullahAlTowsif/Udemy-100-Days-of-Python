# with open("/Udemy/100 Days of Python/Day 25 CSV Data/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("/Udemy/100 Days of Python/Day 25 CSV Data/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temparature = []
#     for row in data:
#         if row[1] != "temp":
#             temparature.append(int(row[1]))
#     print(temparature)


import pandas

data = pandas.read_csv("/Udemy/100 Days of Python/Day 25 CSV Data/weather_data.csv")
# print(type(data))
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(len(temp_list))

# sum = 0
# for tem in temp_list:
#     sum = sum + tem
# avg = sum/(len(temp_list))
# print(avg)


# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in columns
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])



# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# Create a DataFrame for Scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("/Udemy/100 Days of Python/Day 25 CSV Data/new_data.csv")