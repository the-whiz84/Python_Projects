from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
angle = 0


def move_forward():
    tim.fd(10)


def move_backward():
    tim.bk(10)


def rotate_clockwise():
    global angle
    angle -= 10
    tim.setheading(angle)


def rotate_counter_clockwise():
    global angle
    angle += 10
    tim.setheading(angle)


def reset():
    tim.reset()


screen.listen()

def etch_a_sketch():
    screen.onkey(fun=move_forward, key="w")
    screen.onkey(fun=move_backward, key="s")
    screen.onkey(fun=rotate_counter_clockwise, key="a")
    screen.onkey(fun=rotate_clockwise, key="d")
    screen.onkey(fun=reset, key="c")

etch_a_sketch()

screen.exitonclick()