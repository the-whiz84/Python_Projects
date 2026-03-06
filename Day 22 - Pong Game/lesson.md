# Day 22 - Real-Time Game Loop Design and Collision Response

Pong is the classic two-player game, and building it teaches you how to coordinate multiple moving objects at once. We've got a ball that bounces off walls and paddles, two players controlling separate paddles, and a scoreboard that tracks both sides.

This builds directly on what we did with Snake, but now we're tracking two paddles instead of one snake, and the ball bounces in two dimensions instead of moving in one direction.

## The ball and its movement

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

## Two paddles, two key sets

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

## Collision detection

The main game loop checks for collisions in two places:

```python
if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
```

`ball.distance(r_paddle)` checks how close the ball is to the paddle. If it's within 50 pixels and in the right horizontal zone, we bounce. The conditions look complex because we need to check both paddles and make sure the ball is actually in the hitting zone, not just near the paddle.

When the ball goes past a paddle (x coordinate exceeds the screen width), the other player scores and the ball resets to the center.

## Why this matters

Pong demonstrates how to build a real-time game loop with multiple independent objects. Each class does one thing: the ball moves and bounces, the paddles move up and down, the scoreboard tracks points, and `main.py` orchestrates the timing and collision checks.

This same architecture—separate classes for separate responsibilities, coordinated in a central loop—applies to every game you'll build from here on.

## Try it yourself

```bash
python "main.py"
```

Player 1 uses W and S, Player 2 uses Up and Down arrows. First to score wins—or play until you're bored.
