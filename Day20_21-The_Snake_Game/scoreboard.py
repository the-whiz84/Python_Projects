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
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Write the current score on the screen. You can customize the alignment and font used.'''
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        '''Increase the score by 1 each time the snake collides with the food.'''
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        '''Signal when it is game over and display the message on the screen.'''
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
