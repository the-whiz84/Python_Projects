# Improve the snake game by saving and keeping high score in a file
from importlib.resources import contents

# file = open("my_file.txt")
#
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
# 	contents = file.read()
# 	print(contents)

with open("my_file.txt", mode="a") as file:
	file.write("\nNew text")

with open("new_file.txt", mode="w") as file:
	file.write("\nNew text in a new file.")