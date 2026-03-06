# Day 87 - Breakout Game Mechanics and Arcade Loop Design

Breakout is a stronger architecture lesson than it first appears. The project combines a Tkinter menu with a Turtle-based game loop, tracks score and lives, changes ball speed based on progress, and even resets into a second screen of bricks after the first one is cleared.

That makes it a good example of how arcade rules turn into state transitions.

## 1. Separate the Menu Layer from the Game Loop

The entrypoint uses a menu window first:

```python
def start_game():
    game = Game()
    game.run()


if __name__ == "__main__":
    menu = Menu(start_game)
    menu.run()
```

That split is useful because the menu and the game have different jobs:

- `Menu` handles pre-game UI and rules
- `Game` owns the real-time loop

The menu also exposes the rule set clearly, including scoring by brick color, paddle shrink behavior, and the second screen.

## 2. Model Ball, Paddle, and Bricks as Separate Objects

The game breaks the moving parts into focused classes:

- `Ball`
- `Paddle`
- `Brick`

For example, the ball owns its motion vector:

```python
self.ball.dx = 0.5
self.ball.dy = -0.5
```

and its bounce behavior:

```python
def bounce_x(self):
    self.ball.dx *= -1

def bounce_y(self):
    self.ball.dy *= -1
```

That is the right separation. The game loop decides **when** a collision happened, but the ball object decides **how** a bounce changes its velocity.

The paddle stays focused on movement and size:

```python
def move_right(self):
    x = self.paddle.xcor()
    if x < 350:
        self.paddle.setx(x + 20)

def shrink(self):
    current_length = self.paddle.shapesize()[1]
    if current_length > 1:
        self.paddle.shapesize(stretch_wid=1, stretch_len=current_length - 1)
```

## 3. Turn Brick Collisions into Score and Difficulty Changes

The collision code does more than remove bricks. It also drives the scoring and difficulty system:

```python
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

    brick_color = brick.brick.color()[0]
    self.score += self.brick_points.get(brick_color, 0)
    self.update_score()
```

That is where the project becomes more arcade-like. The brick color matters, and certain rows also increase the ball speed:

```python
def increase_speed_on_bricks(self, brick_color):
    if brick_color == "orange" and not self.orange_brick_hit:
        self.ball.ball.dx *= 1.3
        self.ball.ball.dy *= 1.3
        self.orange_brick_hit = True
```

The notebook does not need a physics engine because the gameplay rules are encoded directly into these state transitions.

## 4. Use the Main Loop to Coordinate Lives, Screens, and Game Over

The `run()` method is the orchestration layer:

```python
while True:
    self.window.update()
    self.ball.move()
    self.check_collisions()
    self.ball.check_wall_collision()
    self.shrink_paddle_on_top_wall()
```

That loop continuously updates:

- ball movement
- paddle collisions
- brick collisions
- wall behavior
- score and life loss

The game also treats clearing the full wall as a state change:

```python
if len(self.bricks) == 0:
    self.reset_bricks()
```

And `reset_bricks()` either creates a second board or ends the game completely depending on the current screen count.

That makes the project more interesting than a single-screen demo. It introduces progression and stateful difficulty.

## How to Run the Breakout Game

1. The project uses the standard `turtle` and `tkinter` modules that come with Python.
2. Run the game:
   ```bash
   python main.py
   ```
3. In the menu:
   - read the rules
   - start the game
4. Verify the major behaviors:
   - left and right arrow keys move the paddle
   - brick hits increase score
   - orange and red rows speed the ball up
   - the paddle shrinks after the top wall condition
   - clearing the board resets into the next screen

## Summary

Today, you built an arcade loop around explicit rules rather than generic animation. The project separates the menu from gameplay, models the moving pieces with small classes, and uses collisions to drive score, speed, paddle size, and progression. Breakout works here because every gameplay rule has a clear home in the code.
