import turtle


# Brick class
class Brick:
    def __init__(self, color, x, y):
        self.brick = turtle.Turtle()
        self.brick.speed(0)
        self.brick.shape("square")
        self.brick.color(color)
        self.brick.penup()
        self.brick.goto(x, y)
        self.brick.shapesize(stretch_wid=1, stretch_len=2)

    def destroy(self):
        self.brick.hideturtle()
