##Opening a csv and importing the data
##One way, however, data is in an awkward format and would be difficult to work with. Another way is to import a librabry that specilizes in csv

# with open("weather_data.csv") as w_data:
#     data = w_data.readlines()
#     print(data)
    
# import csv

# with open("weather_data.csv") as w_data:
#     data = csv.reader(w_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
# print(temperatures)

# Working with pandas
import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

##One way to cal average
# total_temp = 0

# for temp in temp_list:
#     total_temp += temp

# avg_temp = total_temp/len(temp_list)
# print(avg_temp)

# #Methods for average and max
# print(data["temp"].mean())
# print(data["temp"].max())

# #Get Data in Columns
# print(data["condition"])
# print(data.condition)

# #Get Data in Rows
# print(data[data.day == "Monday"])

# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp_c = int(monday.temp) 
# monday_temp_f = monday_temp_c * 9/5 + 32
# print(monday_temp_f)

# #Create a dataframe from scratch
# data_dict = {
#     "students": ["M", "N", "O"],
#     "scores": [76, 56, 65]    
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#Create a CSV to summmarize the color for the squirrel census
black_count = 0
cinnamon_count = 0
gray_count = 0

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_fur_colors = squirrel_data["Primary Fur Color"].to_list()

for color in squirrel_fur_colors:
    if color == "Black":
        black_count += 1
    elif color == "Cinnamon":
        cinnamon_count += 1
    elif color == "Gray":
        gray_count += 1
        
print(f"Black {black_count}")
print(f"Cinnamon {cinnamon_count}")
print(f"Gray {gray_count}")

squirrel_data_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [black_count, cinnamon_count, gray_count]
}

squirrel_data_frame = pandas.DataFrame(squirrel_data_dict)
squirrel_data_frame.to_csv("Squirrel Fur Data Summary.csv")