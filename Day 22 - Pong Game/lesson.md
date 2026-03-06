# Day 22 - Real-Time Game Loop Design and Collision Response

Pong takes the game loop ideas from Snake and pushes them into a two-player setup. The project has two paddles, a moving ball, a scoreboard, and collision rules that affect both direction and difficulty. The lesson is really about coordination: several objects update independently, but the game still has to feel like one system.

## 1. The Ball and Its Movement

The `Ball` class inherits from `Turtle` just like our Food did in the Snake game. It tracks its own horizontal and vertical movement with `x_move` and `y_move`:

```python
def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)
```

When the ball hits the top or bottom wall, we reverse the vertical direction:

```python
def bounce_y(self):
    self.y_move *= -1
```

When it hits a paddle, we reverse horizontal direction and also make it slightly faster:

```python
def bounce_x(self):
    self.x_move *= -1
    self.move_speed *= 0.9
```

Multiplying `move_speed` by 0.9 makes the ball 10% faster each time it hits a paddle. That little detail is what makes the game get harder the longer a rally goes on.

## 2. Two Paddles, Two Key Sets

In Snake, one player controlled one snake. In Pong, we need two sets of keyboard bindings. The trick is that we create two separate `Paddle` objects and bind different keys to each:

```python
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
```

W and S control the left paddle, Up and Down arrows control the right. Both paddles use the same `Paddle` class—we just pass different starting positions.

## 3. Collision Detection

The main game loop checks for collisions in two places:

```python
if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
```

`ball.distance(r_paddle)` checks how close the ball is to the paddle. If it's within 50 pixels and in the right horizontal zone, we bounce. The conditions look complex because we need to check both paddles and make sure the ball is actually in the hitting zone, not just near the paddle.

When the ball goes past a paddle (x coordinate exceeds the screen width), the other player scores and the ball resets to the center.

## 4. Why This Matters

Pong demonstrates how to build a real-time game loop with multiple independent objects. Each class does one thing: the ball moves and bounces, the paddles move up and down, the scoreboard tracks points, and `main.py` orchestrates the timing and collision checks.

This same architecture—separate classes for separate responsibilities, coordinated in a central loop—applies to every game you'll build from here on.

The key architectural idea is that each class owns one responsibility:

- `Ball` handles movement and bouncing
- `Paddle` handles player movement
- `Scoreboard` handles points
- `main.py` coordinates collisions, resets, and timing

That structure is what keeps the real-time loop manageable.

## How to Run the Project

```bash
python "main.py"
```

Player 1 uses W and S, Player 2 uses Up and Down arrows. First to score wins—or play until you're bored.

## Summary

Day 22 turns the turtle projects into a proper two-player arcade game. You manage multiple moving objects in one loop, bind two control schemes to the same paddle class, detect collisions based on position and distance, and speed the ball up as rallies continue. The project is simple on the surface, but it teaches real-time coordination clearly.
