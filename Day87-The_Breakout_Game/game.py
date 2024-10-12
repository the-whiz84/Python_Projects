import turtle
from paddle import Paddle
from ball import Ball
from brick import Brick


# Game class
class Game:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Breakout Game")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        self.ball = Ball()
        self.paddle = Paddle()

        self.bricks = []
        self.create_bricks()

        self.score = 0
        self.lives = 3
        self.hits_off_paddle = 0  # Track number of paddle hits
        self.orange_brick_hit = False
        self.red_brick_hit = False
        self.top_wall_reached = False  # If the red row has been passed
        self.current_screen = 1  # Track the current screen

        # Points for each brick color
        self.brick_points = {"yellow": 1, "green": 3, "orange": 5, "red": 7}

        # Display score and lives
        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(-350, 260)
        self.update_score()

        # Bind keys
        self.window.listen()
        self.window.onkeypress(self.paddle.move_right, "Right")
        self.window.onkeypress(self.paddle.move_left, "Left")

    def create_bricks(self):
        brick_colors = [
            "red",
            "red",
            "orange",
            "orange",
            "green",
            "green",
            "yellow",
            "yellow",
        ]
        for row, color in enumerate(brick_colors):
            for i in range(-350, 400, 50):
                brick = Brick(color, i, 250 - (row * 30))
                self.bricks.append(brick)

    def reset_bricks(self):
        """Reset bricks after clearing the first screen."""
        if self.current_screen == 1:
            self.current_screen += 1  # Move to the second screen
            self.bricks.clear()  # Clear the old bricks
            self.create_bricks()  # Create the second set of bricks

            # Reset paddle and ball for the new screen
            self.paddle.reset_position()
            self.ball.reset_position()
            self.orange_brick_hit = False  # Reset hit status for bricks
            self.red_brick_hit = False
            self.hits_off_paddle = 0  # Reset hits count
            self.top_wall_reached = False  # Reset top wall reached status
        else:
            self.game_over()

    def game_over(self):
        self.score_display.goto(0, 0)
        self.score_display.write(
            "Game Over", align="center", font=("Courier", 24, "normal")
        )
        self.score_display.goto(0, -30)  # Position for replay prompt
        self.score_display.write(
            "Press 'Space' to Exit", align="center", font=("Courier", 18, "normal")
        )

        # Wait for spacebar to exit
        self.window.onkeypress(self.exit_game, "space")
        self.window.listen()

    def exit_game(self):
        turtle.bye()  # Close the turtle graphics window

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(
            f"Score: {self.score}   Lives: {self.lives}",
            align="left",
            font=("Courier", 18, "normal"),
        )

    def check_collisions(self):
        # Ball and paddle collision
        if (self.ball.ball.ycor() > -240 and self.ball.ball.ycor() < -230) and (
            self.ball.ball.xcor() > self.paddle.paddle.xcor() - 50
            and self.ball.ball.xcor() < self.paddle.paddle.xcor() + 50
        ):
            self.ball.ball.sety(-230)
            self.ball.bounce_y()
            self.hits_off_paddle += 1
            self.check_ball_speed()

        # Ball and brick collision
        for brick in self.bricks:
            if (
                self.ball.ball.xcor() > brick.brick.xcor() - 25
                and self.ball.ball.xcor() < brick.brick.xcor() + 25
            ) and (
                self.ball.ball.ycor() > brick.brick.ycor() - 10
                and self.ball.ball.ycor() < brick.brick.ycor() + 10
            ):
                self.ball.bounce_y()
                brick.destroy()
                self.bricks.remove(brick)

                # Increment score based on brick color
                brick_color = brick.brick.color()[0]
                self.score += self.brick_points.get(brick_color, 0)
                self.update_score()  # Update the score display

                self.increase_speed_on_bricks(brick_color)

    def check_ball_speed(self):
        # Incremental speed increase after hitting paddle 4 and 12 times
        if self.hits_off_paddle in [4, 12]:
            self.ball.ball.dx *= 1.3
            self.ball.ball.dy *= 1.3
            self.hits_off_paddle += 1  # Ensure it doesn't increment again

    def increase_speed_on_bricks(self, brick_color):
        if brick_color == "orange" and not self.orange_brick_hit:
            self.ball.ball.dx *= 1.3
            self.ball.ball.dy *= 1.3
            self.orange_brick_hit = True
        elif brick_color == "red" and not self.red_brick_hit:
            self.ball.ball.dx *= 1.3
            self.ball.ball.dy *= 1.3
            self.red_brick_hit = True

    def shrink_paddle_on_top_wall(self):
        if self.ball.ball.ycor() > 280 and not self.top_wall_reached:
            self.paddle.shrink()
            self.top_wall_reached = True

    def run(self):
        while True:
            self.window.update()

            # Move the ball
            self.ball.move()

            # Check collisions
            self.check_collisions()

            # Border collisions and paddle shrink
            self.ball.check_wall_collision()
            self.shrink_paddle_on_top_wall()

            # Lose life when missing the paddle
            if self.ball.ball.ycor() < -290:
                self.lives -= 1
                self.update_score()
                self.ball.reset_position()
                if self.lives == 0:
                    self.game_over()
                    break

            # Check if all bricks are cleared and reset for a second screen
            if len(self.bricks) == 0:
                self.reset_bricks()
