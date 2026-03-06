from turtle import Turtle
FONT = ("Courier", 10, "normal")

class QuizGame(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.score = 0

	def add_state(self, name, x_cord, y_cord):
		self.goto(x_cord, y_cord)
		self.write(f"{name}", align="center", font=FONT)

	def increase_score(self):
		self.score += 1