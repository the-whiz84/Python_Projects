from turtle import Turtle, Screen

# tim = Turtle()

# def move_forwards():
# 	tim.forward(10)
#
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)

timmy = Turtle()
tommy = Turtle()
barry = Turtle()

timmy.color("green")
tommy.color("purple")
barry.color("red")

timmy.forward(100)
tommy.backward(100)
barry.left(90)
barry.forward(100)



screen = Screen()

screen.exitonclick()