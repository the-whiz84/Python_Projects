import turtle


# Paddle class
class Paddle:
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -250)

    def move_right(self):
        x = self.paddle.xcor()
        if x < 350:  # Move right if not at the edge
            self.paddle.setx(x + 20)

    def move_left(self):
        x = self.paddle.xcor()
        if x > -350:  # Move left if not at the edge
            self.paddle.setx(x - 20)

    def shrink(self):
        current_length = self.paddle.shapesize()[1]
        if current_length > 1:  # Ensure it doesn't shrink too much
            self.paddle.shapesize(stretch_wid=1, stretch_len=current_length - 1)

    def reset_position(self):
        self.paddle.goto(0, -250)
