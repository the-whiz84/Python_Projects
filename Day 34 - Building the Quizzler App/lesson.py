# Python Typing - Type Hints and Arrows ->

# 1. Type Hints

def greeting(name: str) -> str:
	return "hello" + name

# age: int
# name: str
# height: float
# is_human: bool
# We can set the type of a variable before assigning a value to it

# age = 12
# name = "Radu"

# We can also specify a DataType inside a function
def police_check(age: int):
	if age > 18:
		can_drive = True
	else:
		can_drive = False
	return can_drive

# print(police_check(16))
# False
if police_check(19):
	print("You may continue")
else:
	print("Go to jail!")


# You can also specify the DataType of the output of a function:
def police_check(age: int) -> bool:
	if age > 18:
		can_drive = True
	else:
		can_drive = False
	return can_drive