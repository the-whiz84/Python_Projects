from turtle import Turtle

STARTING_POSITION = (0, -380)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 380


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.setheading(90)
        self.fd(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.fd(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.fd(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False

