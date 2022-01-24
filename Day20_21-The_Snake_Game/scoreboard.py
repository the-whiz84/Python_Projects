from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Cantarell', 12, 'normal')

class Scoreboard(Turtle):
    '''Create a Class that inherits everything from the Turtle Class'''
    def __init__(self):
        '''Initialize the Scoreboard Class with all it's attributes and methods'''
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 460)
        self.get_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Write the current score on the screen. You can customize the alignment and font used.'''
        self.clear()
        self.write(arg=f"Score: {self.score}. High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        '''Increase the score by 1 each time the snake collides with the food.'''
        self.score += 1
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())

    def save_high_score(self):
        with open("data.txt", mode='w') as data:
            data.write(f"{self.high_score}")

    def refresh(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()
