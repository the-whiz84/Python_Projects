# Day 23 - Object Movement, Collision Detection, and Difficulty Scaling

This is a Frogger-style game where your turtle needs to cross a busy road. Cars move across the screen at different speeds, and every time you reach the other side, the game gets harder.

The architecture should feel familiar now—we've got separate classes for the player, the cars, and the scoreboard. But this time, there's a new challenge: managing many cars that spawn randomly and increasing difficulty after each level.

## The player and finish line

The `Player` class is straightforward. Your turtle starts at the bottom, moves forward when you press Up, and checks if it reached the top:

```python
def is_at_finish(self):
    if self.ycor() == FINISH_LINE_Y:
        return True
    else:
        return False
```

If the turtle makes it to y=280, we reset it to the start and increase the difficulty.

## Car spawning and movement

In `CarManager`, we keep a list of all active cars. Each frame, we might create a new car—but only with a 1-in-6 chance:

```python
def create_car(self):
    random_chance = random.randint(1, 6)
    if random_chance == 1:
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        y_cor = random.randint(-250, 250)
        new_car.goto(300, y_cor)
        self.all_cars.append(new_car)
```

That randomness is what makes the game interesting. If cars spawned every frame or on a fixed schedule, you'd memorize the pattern. With random spawning, each crossing feels different.

Moving the cars is simple—we loop through all of them and move each one backward (since they're coming from the right side of the screen):

```python
def move_cars(self):
    for car in self.all_cars:
        car.backward(self.car_speed)
```

## Collision detection

In the main loop, we check if the player is too close to any car:

```python
for car in car_manager.all_cars:
    if car.distance(player) < 20:
        game_is_on = False
        scoreboard.game_over()
```

The `distance()` method returns how far apart two turtles are. If it's less than 20 pixels, the car hit the player and the game ends.

## Difficulty scaling

Every time the player crosses successfully, we speed up the cars:

```python
if player.is_at_finish():
    player.go_to_start()
    car_manager.increase_speed()
    scoreboard.increase_level()
```

The `increase_speed()` method adds to `car_speed`, so each level makes the cars move faster. This is the classic difficulty curve: complete the objective, and the next round is harder.

## Try it yourself

```bash
python "main.py"
```

Use the Up arrow to move forward. Time your crossings carefully—once you reach the top, the cars get faster.
