import turtle
import random


# Ball class
class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(50)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 0.5  # Initial speed
        self.ball.dy = -0.5  # Initial speed

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def bounce_x(self):
        self.ball.dx *= -1

    def bounce_y(self):
        self.ball.dy *= -1

    def check_wall_collision(self):
        if self.ball.xcor() > 390:
            self.ball.setx(390)
            self.bounce_x()
        if self.ball.xcor() < -390:
            self.ball.setx(-390)
            self.bounce_x()

        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.bounce_y()

    def reset_position(self):
        self.ball.goto(0, 0)
        self.ball.dx *= random.choice([-1, 1])
        self.ball.dy *= random.choice([-1, 1])
