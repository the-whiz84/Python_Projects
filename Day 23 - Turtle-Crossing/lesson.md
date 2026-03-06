# Day 23 - Object Movement, Collision Detection, and Difficulty Scaling

Day 23 turns the turtle games into a lane-based obstacle game in the style of Frogger. The player moves upward one step at a time, cars stream across the screen, and each successful crossing increases the difficulty. The interesting part of this project is not just movement. It is how randomness, collision checks, and level progression combine to make a game feel alive instead of predictable.

## 1. Keeping the Player Rules Simple

The `Player` class is deliberately small. It starts at the bottom, moves when the Up key is pressed, and checks whether it reached the finish line:

```python
def is_at_finish(self):
    if self.ycor() == FINISH_LINE_Y:
        return True
    else:
        return False
```

That simplicity is a good design choice. The player object does not need to know about cars, levels, or game-over rules. Its job is just to represent the turtle and report whether it reached the top.

This is the same responsibility pattern you saw in Snake and Pong: each class should own one clear part of the game logic.

## 2. Using Random Car Spawns to Avoid Predictable Patterns

The `CarManager` creates cars with a random chance on each frame:

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

This is a smart way to create variety without complicated scheduling logic. Cars do not appear on every frame, and they do not always appear in the same lane. That randomness makes each attempt feel different.

It also teaches an important game-design point: predictable systems are easier to code, but a small amount of randomness often makes a game feel much more natural.

## 3. Updating Many Objects Through One Manager

Once cars exist, the manager moves all of them:

```python
def move_cars(self):
    for car in self.all_cars:
        car.backward(self.car_speed)
```

This is a common pattern in simple games:

- store many similar objects in a list
- iterate through the list on each frame
- apply the same update rule to every object

That pattern matters because the main loop stays readable. `main.py` does not need to know how each car moves individually. It just asks the manager to update the whole group.

## 4. Scaling Difficulty with Speed Instead of New Rules

The level-up logic is short, but it is one of the strongest design decisions in the project:

```python
if player.is_at_finish():
    player.go_to_start()
    car_manager.increase_speed()
    scoreboard.increase_level()
```

The game does not introduce a new mechanic on each level. It keeps the rules exactly the same and only changes one variable: car speed.

That is a good difficulty curve for a small arcade game. The player already understands the controls and the objective, so increasing speed is enough to raise the tension without forcing them to learn a second system.

The collision loop completes that design:

```python
for car in car_manager.all_cars:
    if car.distance(player) < 20:
        game_is_on = False
        scoreboard.game_over()
```

The rule is simple and easy to understand: if a car gets close enough, the run is over.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Use the Up arrow to move the player toward the top of the screen.
4. Verify that each successful crossing increases the level and makes the cars move faster on the next round.

## Summary

Day 23 combines simple player controls with randomly spawned obstacles and a clean difficulty curve. The player logic stays focused, the `CarManager` owns all car updates, collisions end the run immediately, and speed increases make each level more demanding without changing the core rules. It is a strong example of how small mechanics can still produce a satisfying game loop.
