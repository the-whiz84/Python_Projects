# Class Inheritance

# class Fish(Animal):
# 	def __init__(self):
# 		super __init__ ():

class Animal:
	def __init__(self):
		self.num_eyes = 2

	def breathe(self):
		print("Inhale exhale")

class Fish(Animal):
	def __init__(self):
		super().__init__()

	def swim(self):
		print("moving in water")

	def breathe(self):
		super().breathe()
		print("doing it underwater")


nemo = Fish()
# nemo.swim()
nemo.breathe()
# print(nemo.num_eyes)


# How to use slicing in lists and tuples
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

# to get only keys c, d, e we slice the list between positions 2 and 5. This is because 0 is before a and 5 is between e and f.

# To slice from a position to the end, we omit the second number
piano_keys[2:]
# This works both ways
piano_keys[:5]

# We can also set an increment
print(piano_keys[2:5])
print(piano_keys[2:5:2])
print(piano_keys[::2])
['c', 'd', 'e']
['c', 'e']
['a', 'c', 'e', 'g']

# We can also go backwards
print(piano_keys[::-1])
['g', 'f', 'e', 'd', 'c', 'b', 'a']

# THis also works for tuples
piano_tuple = ("do", "re", "mi", "fa", "sol", "la", "si")
print(piano_tuple[2:5])

# Detect collision with tail.
for segment in snake.snake_body:
	if segment == snake.head:
		pass
	elif snake.head.distance(segment) < 10:
		game_is_on = False
		scoreboard.game_over()

# We can change it now to
for segment in snake.snake_body:
	if snake.head.distance(snake.snake_body[1:segment]) < 10:
		game_is_on = False
		scoreboard.game_over()