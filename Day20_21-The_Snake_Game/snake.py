from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        '''Initialize the Snake Class with all it's attributes and methods.'''
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head_mod()

    def create_snake(self):
        '''This method creates the Snake on screen from 3 different Turtle segments.'''
        for position in STARTING_POSITIONS:
            self.add_segment(position)
   
    def head_mod(self):
        self.head.color("cyan")
        self.head.shape("circle")
        self.head.shapesize(0.6, 0.8)

    def add_segment(self, position):
        '''Add a new segment to the snake's tail.'''
        new_segment = Turtle("square")
        new_segment.color("orange")
        new_segment.shapesize(0.5, 0.5)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def restart(self):
        for seg in self.segments:
            seg.goto(1500, 1500)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head_mod()

    def extend(self):
        '''Extend the snake's tail by a segment.'''
        self.add_segment(self.segments[-1].position())

    def move(self):
        '''The snake continues to move forward when initialized.'''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        '''Move snake UP.'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''Move snake DOWN.'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''Move snake LEFT'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''Move snake RIGHT.'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
