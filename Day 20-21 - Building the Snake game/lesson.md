# Day 20-21 - Game Loops, OOP Composition, Inheritance, and Collision Logic
Days 20-21 combine a real-time game loop with class-based architecture so you can coordinate movement, growth, scoring, and collisions in one coherent design.

## What You Learn
- Building a frame loop with `screen.update()` + `time.sleep(...)`.
- Splitting game concerns into classes (`Snake`, `Food`, `Scoreboard`).
- Using inheritance (`Food(Turtle)`, `Scoreboard(Turtle)`) and `super().__init__()`.
- Updating list-based body segments from tail to head.
- Detecting collisions with food, walls, and snake tail.

## Historical Notes Recovered from Git
The deleted `lesson.py` for this day emphasized:
- class inheritance
- `super().__init__()` to initialize parent behavior
- list slicing techniques

Those ideas are visible in the final game: inheritance is used directly in `food.py` and `scoreboard.py`, and slicing appears in tail-collision checks.

## Current Project Architecture
- `main.py`: game loop orchestration and collision rules.
- `snake.py`: snake creation, movement, directional guardrails, and growth.
- `food.py`: random food placement via a `Turtle` subclass.
- `scoreboard.py`: score rendering and game-over message.

## Real Day Snippets
From `snake.py` (tail-to-head body movement):

```python
def move(self):
    for seg_num in range(len(self.snake_body) - 1, 0, -1):
        new_x = self.snake_body[seg_num - 1].xcor()
        new_y = self.snake_body[seg_num - 1].ycor()
        self.snake_body[seg_num].goto(new_x, new_y)
    self.head.fd(MOVE_DISTANCE)
```

From `food.py` (inheritance + parent constructor):

```python
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
```

From `main.py` (tail collision using slicing):

```python
for segment in snake.snake_body[1:]:
    if snake.head.distance(segment) < 10:
        game_is_on = False
        scoreboard.game_over()
```

## Common Pitfalls
- Snake reverses into itself: directional methods must block opposite heading.
- Tail movement looks broken: segment updates must iterate from end to start.
- Flickering visuals: `screen.tracer(0)` and explicit `screen.update()` must be paired.

## Run
```bash
python "main.py"
```
