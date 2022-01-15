from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
# angle = 0


def move_forward():
    tim.fd(10)


def move_backward():
    tim.bk(10)


# def turn_right():
#     global angle
#     angle -= 10
#     tim.setheading(angle)
#Alternative ways to achieve the same:
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_left():
    tim.left(10)


def reset():
    tim.reset()
# #An alternative that is longer but keeps the turtle parameters like color and size
# def reset():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# tim.color("green")

screen.listen()

def etch_a_sketch():
    screen.onkey(fun=move_forward, key="w")
    screen.onkey(fun=move_backward, key="s")
    screen.onkey(fun=turn_left, key="a")
    screen.onkey(fun=turn_right, key="d")
    screen.onkey(fun=reset, key="c")

etch_a_sketch()

screen.exitonclick()