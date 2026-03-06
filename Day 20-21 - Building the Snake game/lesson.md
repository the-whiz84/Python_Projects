# Day 20-21 - Game Loops, OOP Composition, Inheritance, and Collision Logic

This is where it all comes together. We're building a real-time Snake game with proper class architecture—Snake, Food, and Scoreboard as separate classes. It's also where we first use inheritance, and it changes how you think about building on top of existing code.

The game runs in a loop that updates the screen after every movement. Each class has a clear job: the Snake knows how to move and grow, the Food knows how to randomize its position, and the Scoreboard knows the current score.

## Inheritance: building on top of Turtle

We've used `Turtle` to draw before. Now we subclass it to create specialized objects. In `food.py`, `Food` inherits from `Turtle`, which means it automatically gets all the Turtle capabilities (position, movement, shape) plus what we add:

```python
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid= 0.5, stretch_len= 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
```

The `super().__init__()` call is what hands control to the parent class `Turtle` so our `Food` object gets initialized with all the standard turtle properties. After that, we customize it—small red circle, always penup so it doesn't draw lines, and a `refresh()` method to jump to a new random spot.

The same pattern appears in `scoreboard.py`:

```python
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.write_score()
```

We don't need to see the scoreboard turtle itself, so we hide it with `hideturtle()`. But it can still write text to the screen, which is exactly what we need.

## How the snake moves

The trickiest part of snake movement is that every segment follows the one ahead of it. We can't just move all segments forward at once—segment 2 has to follow segment 1, segment 3 follows segment 2, and so on. The solution is to work backwards from the tail:

```python
def move(self):
    for seg_num in range(len(self.snake_body) - 1, 0, -1):
        new_x = self.snake_body[seg_num - 1].xcor()
        new_y = self.snake_body[seg_num - 1].ycor()
        self.snake_body[seg_num].goto(new_x, new_y)
    self.head.fd(MOVE_DISTANCE)
```

`range(len(self.snake_body) - 1, 0, -1)` gives us the indices in reverse order: 2, 1 (if we have three segments). Each segment moves to where the previous segment was. Only the head moves forward into new territory.

## Directional guardrails

One annoying bug happens if you can reverse direction instantly—you'd crash into your own body. We prevent this by checking the current heading before allowing a turn:

```python
def up(self):
    if self.head.heading() != DOWN:
        self.head.setheading(UP)
```

If the snake is currently going down (270 degrees), pressing Up gets ignored. Same logic applies to all four directions.

## The game loop

In `main.py`, the game runs inside a `while` loop with `screen.update()` and a small sleep to control frame rate. This is the heartbeat of any real-time game:

```python
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # check collisions...
```

When the snake eats food, we extend its body and increase the score. When it hits the wall or its own tail, the game ends.

## Try it yourself

```bash
python "main.py"
```

Use arrow keys to control the snake. Try to get the highest score without hitting the walls or your own tail.
