from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 200)
        self.write(self.l_score, align="center", font=("Courier", 24, "normal"))
        self.goto(50, 200)
        self.write(self.r_score, align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Courier", 36, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
