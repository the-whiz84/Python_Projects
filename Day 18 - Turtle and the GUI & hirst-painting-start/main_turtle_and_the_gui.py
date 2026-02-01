import turtle
from turtle import Turtle, Screen
import random
# from random import random

# import turtle
# from turtle import Turtle

# tim = turtle.Turtle()
# tim = Turtle()

# from random import *
# from turtle import *

# import turtle as t
# tim = t.Turtle()
# import heroes
# print(heroes.gen())

timmy = Turtle()
timmy.shape("turtle")
# timmy.color("ForestGreen")



# r = random.randint(0, 255)
# g = random.randint(0, 255)
# b = random.randint(0, 255)
# timmy.color(r, g, b)
# timmy.forward(200)
# Challenge 1 -  Draw a square
# for _ in range(4):
# 	timmy.forward(100)
# 	timmy.right(90)

# Challenge 2 - Draw a dotted line 20 times
# for i in range(20):
# 	timmy.forward(10)
# 	timmy.penup()
# 	timmy.forward(10)
# 	timmy.pendown()

# Challenge 3 - Draw different shapes in random colors from triangle to decagon

# for item in range(3, 11):
# 	r = random.randint(0, 255)
# 	g = random.randint(0, 255)
# 	b = random.randint(0, 255)
# 	angle = 360 / item
# 	timmy.pencolor((r, g, b))
# 	for i in range(item):
# 		timmy.right(angle)
# 		timmy.forward(100)

# Challenge 4 - Draw a random walk
turtle.colormode(255)


def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color_tuple = (r, g, b)
	return color_tuple


def random_walk():
	angle = random.choice(directions)
	timmy.pensize(20)
	timmy.hideturtle()
	timmy.forward(40)
	timmy.setheading(angle)


directions = [0, 90, 180, 270]
timmy.speed("fast")

# for i in range(200):
# 	timmy.pencolor(random_color())
# 	random_walk()

# Python Tuples

# my_tuple = (1, 3, 8)
# print(my_tuple[0])

# Tuples are immutable, unlike lists. You cannot change the value or remove a value

# Challenge 5 - Draw a spirograph

def spirograph(size_of_gap):
	for angle in range(int(360 / size_of_gap)):
		timmy.pencolor(random_color())
		timmy.circle(radius=100)
		timmy.setheading(timmy.heading() + size_of_gap)

spirograph(10)

screen = Screen()
screen.exitonclick()
