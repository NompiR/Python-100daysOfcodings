"""with open("weather_data.csv") as weather:
    result_data = weather.readlines()
    print(result_data)
"""

"""import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)"""


import pandas

data = pandas.read_csv("weather_data.csv")
#print(data['temp'])
temp_lists = data['temp'].to_list()
"""temp_lists_len = len(temp_lists)
sum_of_lists = sum(temp_lists) / temp_lists_len
print(sum_of_lists)"""
"""max_temp = data['temp'].max()
print(data[data.temp == max_temp])"""

celsius = data[data.day == 'Monday'].temp[0]
fahrenheit =celsius * 9/5 + 32
print(fahrenheit)



#how to create a dataframe from scratch
data_dict = {
"students" : ['Amy', 'James', 'Joy'],
    "scores" : [76, 53, 90]
}
#data = pandas.DataFrame(data_dict)
datas = pandas.DataFrame({
    "students" : ['Amy', 'James', 'Joy'],
    "scores" : [76, 53, 90]
})
datas.to_csv("new_data.csv")
print(datas)
