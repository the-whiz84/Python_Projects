# PART 1 - How to extract RGB values from images
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('Day18-The_Hirst_Painting/image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

from data import rgb_colors

# PART 2 - Drawing the Dots
# The turtle must draw a grid of 10 dots horizontally and 10 dots vertically
# Dots size is 20, space between dots is 50
import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fast")
colormode(255)

x = -225
y = -225

def draw_dots(y_coordinate):
    timmy.penup()
    timmy.setpos(x, y)
    timmy.pendown()
    for _ in range(10):
        color = random.choice(rgb_colors)
        timmy.dot(20, color)
        timmy.penup()
        timmy.fd(50)


for _ in range(10):
    draw_dots(y)
    y += 50
    timmy.setpos(x, y)


screen = Screen()
screen.exitonclick()
