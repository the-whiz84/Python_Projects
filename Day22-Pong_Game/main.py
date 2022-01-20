import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Wizard's Pong Game")
screen.tracer(0)
screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) <= 50 and ball.xcor() >= 320:
        ball.bounce_x()

    if ball.distance(l_paddle) <= 50 and ball.xcor() <= -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
