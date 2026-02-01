
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

color_list = [(23, 16, 94), (232, 43, 6), (153, 14, 30), (41, 181, 158), (127, 253, 206), (237, 71, 166), (209, 179, 208), (246, 218, 21),
              (40, 133, 242), (244, 247, 253), (246, 218, 5), (207, 148, 178), (126, 155, 204), (106, 189, 174), (224, 134, 117), (81, 87, 136),
              (150, 64, 75), (209, 87, 66), (49, 44, 100), (244, 168, 154), (175, 184, 222), (111, 9, 23), (179, 30, 10)]


def draw_dots():
    for item in range(10):
        color = random.choice(color_list)
        timmy.dot(20, color)
        timmy.forward(50)


timmy = Turtle()
timmy.penup()
timmy.hideturtle()
timmy.speed("fast")
x_pos = -250
y_pos = -250
timmy.teleport(x_pos, y_pos)

for pos in range(10):
    y_pos += 50
    timmy.teleport(x_pos, y_pos)
    draw_dots()


screen = Screen()
screen.exitonclick()
