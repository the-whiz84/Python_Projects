import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=1600, height=1000)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

is_race_on = False
y_axis = -350
n = 0


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.shapesize(2, 2, 7)
    new_turtle.penup()
    y_axis += 100
    new_turtle.goto(x=-780, y=y_axis)
    n += 1
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 750:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle won the race.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
