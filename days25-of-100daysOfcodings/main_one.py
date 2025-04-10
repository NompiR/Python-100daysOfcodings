import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_counts = len(data[data['Primary Fur Color'] == "Gray"])
red_squirrels_counts = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_counts = len(data[data['Primary Fur Color'] == "Black"])


print(grey_squirrels_counts)
print(red_squirrels_counts)
print(black_squirrels_counts)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_counts, red_squirrels_counts, black_squirrels_counts]
}

df = pd. DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
