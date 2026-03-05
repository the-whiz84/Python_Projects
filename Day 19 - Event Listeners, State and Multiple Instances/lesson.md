# Day 19 - Event Listeners, Keyboard Bindings, and Multi-Object State
Day 19 teaches how interactive programs react to user input and how to manage state when several objects are moving at once.

## Why This Day Matters
This is your first event-driven day. Instead of running top-to-bottom once, the program waits for actions (key presses or race events) and updates state continuously.

## Concepts You Learn
- Registering keyboard callbacks with `screen.onkey(...)`.
- Enabling input listening with `screen.listen()`.
- Separating behavior into small movement functions.
- Managing many objects in a list (`all_turtles`) and updating each one per loop.
- Stopping loops based on state changes (`is_race_on = False`).

## Files and Learning Purpose
- `etch_a_sketch.py`: key-driven movement and reset behavior.
- `turtle_race.py`: multiple turtle instances, random motion, and winner detection.
- `main.py`: simple multi-instance demo (three turtles with independent movement).

## Event Binding Example (`etch_a_sketch.py`)
Each key maps to one function, which makes control flow explicit and easy to debug.

```python
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear_screen)
```

## Multi-Instance Race State (`turtle_race.py`)
The race loop iterates over all turtle objects and updates each one with random distance.

```python
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
        distance = random.randint(0, 10)
        turtle.forward(distance)
```

This pattern appears in many games: one loop, many entities, shared win condition.

## Common Pitfalls
- Keys do nothing: `screen.listen()` is missing or called too late.
- Callbacks crash: `onkey` received `fun=move_forwards()` instead of `fun=move_forwards`.
- Race never ends: finish-line threshold and turtle starting positions are inconsistent.

## Run
```bash
python "etch_a_sketch.py"
# or
python "turtle_race.py"
# or
python "main.py"
```
