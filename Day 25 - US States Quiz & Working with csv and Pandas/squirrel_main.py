import pandas

data = pandas.read_csv("squirrel_data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]

gray_squirrels_count = len(gray_squirrels)
black_squirrels_count = len(black_squirrels)
red_squirrels_count = len(red_squirrels)

to_learn = {
	"Fur Color": ["Gray", "Black", "Red"],
	"Count": [gray_squirrels_count, black_squirrels_count, red_squirrels_count]
}
df = pandas.DataFrame(to_learn)
print(df)
df.to_csv("Squirrel_Color_Count.csv")