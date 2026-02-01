import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which tutle will win the race? Choose your color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = -150
all_turtles = []

for pos in colors:
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(pos)
	new_turtle.penup()
	new_turtle.speed("fast")
	y_pos += 50
	new_turtle.goto(x=-230, y=y_pos)
	all_turtles.append(new_turtle)

if user_bet:
	is_race_on = True

while is_race_on:
	for turtle in all_turtles:
		if turtle.xcor() > 230:
			is_race_on = False
			winner = turtle.pencolor()
			if winner == user_bet:
				print(f"You've won! The {winner} turtle has won the race.")
			else:
				print(f"You've lost. The {winner} turtle has won the race.")
		distance = random.randint(0, 10)
		turtle.forward(distance)


screen.exitonclick()