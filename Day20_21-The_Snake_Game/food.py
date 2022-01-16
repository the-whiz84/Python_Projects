import random
from turtle import Turtle


class Food(Turtle):
    '''From the super Class Turtle create a Food Class for the Snake to eat.'''
    def __init__(self):
        '''Initialize the Food Class with it's attributes and methods'''
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        '''The refresh method will place the food randomly within the screen boundaries'''
        random_x = random.randint(-480, 480)
        random_y = random.randint(-480, 480)
        self.goto(random_x, random_y)
