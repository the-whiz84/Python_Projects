# Day 23 - Object Movement, Collision Detection, and Difficulty Scaling
Day 23 teaches how to manage moving obstacles, detect player collisions, and progressively increase game difficulty over levels.

## Core Concepts in This Project
- Frame loop with regular updates (`time.sleep(0.1)` + `screen.update()`).
- Separate classes for player, obstacle system, and HUD.
- Probabilistic spawning of cars to avoid predictable patterns.
- Distance-based collision checks between player and obstacles.
- Difficulty ramp by increasing car speed after each successful crossing.

## How the Files Work Together
- `player.py`: turtle avatar movement, finish-line detection, and reset position.
- `car_manager.py`: creates cars, stores them in `all_cars`, and moves them per frame.
- `scoreboard.py`: tracks level and displays game-over text.
- `main.py`: main loop orchestration and win/lose logic.

## Real Day Snippets
From `car_manager.py` (controlled random spawn):

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

From `main.py` (collision + level progression):

```python
for car in car_manager.all_cars:
    if car.distance(player) < 20:
        game_is_on = False
        scoreboard.game_over()

if player.is_at_finish():
    player.go_to_start()
    car_manager.increase_speed()
    scoreboard.increase_level()
```

## Important Design Note
`CarManager` owns obstacle state. `Player` never creates or removes cars. That boundary keeps each class easier to reason about and debug.

## Common Pitfalls
- Finish line never triggers: comparing with `==` can be fragile; `>=` is often safer.
- Car list grows forever: consider recycling/removing off-screen cars in extensions.
- Collision feels unfair: tune `distance` threshold or car sizes.

## Run
```bash
python "main.py"
```
