# Day 22 - Real-Time Game Loop Design and Collision Response
Day 22 teaches how to coordinate multiple moving objects in a real-time loop while keeping controls, physics, and scoring in separate classes.

## What You Learn
- Building a smooth loop with `screen.tracer(0)` and `screen.update()`.
- Keyboard handling for two players on the same keyboard.
- Class-based game objects (`Paddle`, `Ball`, `Scoreboard`).
- Collision detection against walls and paddles.
- Dynamic game speed via `ball.move_speed`.

## Architecture of This Day
- `main.py`: orchestrates the loop, input bindings, and scoring conditions.
- `paddle.py`: paddle movement abstraction.
- `ball.py`: movement vector and bounce behavior.
- `scoreboard.py`: left/right score rendering and updates.

This separation is the core engineering lesson: each class handles one responsibility, and `main.py` coordinates them.

## Real Day Snippets
From `main.py` (loop + collision orchestration):

```python
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
```

From `ball.py` (difficulty ramp on paddle hit):

```python
def bounce_x(self):
    self.x_move *= -1
    self.move_speed *= 0.9
```

From `scoreboard.py` (state + redraw):

```python
def l_point(self):
    self.l_score += 1
    self.update_score()
```

## Common Bugs on This Day
- Ball passes through paddle: collision thresholds are too small or checked too late.
- Game feels choppy: missing `tracer(0)`/`update()` pairing or sleep value too large.
- Scores not updating visually: `clear()` must run before writing new values.

## Run
```bash
python "main.py"
```
