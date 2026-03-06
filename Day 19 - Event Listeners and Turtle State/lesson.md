# Day 19 - Event Listeners and Turtle State

Day 19 makes turtle programs interactive. Instead of running top to bottom once and exiting, the app opens a window, waits for user input, and reacts to key presses in real time. The folder also introduces multi-object state through the turtle race, where several turtles are updated inside the same loop.

## 1. How Keyboard Events Work

In `etch_a_sketch.py`, we register functions to respond to specific keys. The critical part is calling `screen.listen()` first, then binding each key to a function:

```python
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear_screen)
```

One common mistake: people write `screen.onkey(key="w", fun=move_forwards())` with parentheses after the function name. That calls the function immediately instead of passing the function itself. Leave off the parentheses—the screen will call it when the key is pressed.

Each movement function is tiny because the event loop handles calling it over and over:

```python
def move_forwards():
    tim.forward(10)
```

Every time you press W, the turtle moves forward 10 pixels.

## 2. Multiple Turtles and the Race Loop

In `turtle_race.py`, we create six turtles and line them up at the starting position:

```python
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = -150
all_turtles = []

for pos in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(pos)
    new_turtle.penup()
    y_pos += 50
    new_turtle.goto(x=-230, y=y_pos)
    all_turtles.append(new_turtle)
```

We keep all the turtles in a list. When the race starts, the loop checks every single turtle in that list on each iteration:

```python
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
        distance = random.randint(0, 10)
        turtle.forward(distance)
```

The moment any turtle crosses the finish line (x > 230), we flip the flag to stop the loop and announce the winner.

This pattern of iterating over a list of objects, updating each one, and checking a shared stop condition is a foundation for later game projects.

## 3. Why This Day Matters

The `etch_a_sketch.py` file teaches event-driven programming. The race project teaches how to manage multiple objects at once. Together, they show that graphical programs are often built around two loops:

- an event loop that waits for user input
- an update loop that changes object state over time

Once those ideas are in place, game logic starts to feel much less mysterious.

## How to Run the Projects

Drive the turtle around:

```bash
python "etch_a_sketch.py"
```

Then run the race and place a bet:

```bash
python "turtle_race.py"
```

## Summary

Day 19 introduces event-driven interaction with `screen.listen()` and `screen.onkey()`, then extends turtle work into multi-object state through a simple race simulation. The lesson is important because it shifts your programs from static drawing into interactive behavior and repeated object updates.
