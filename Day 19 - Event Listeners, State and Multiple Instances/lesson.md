# Day 19 - Event Listeners, Keyboard Bindings, and Multi-Object State

Now that you've seen how to draw with turtle, it's time to make it interactive. Today is about responding to user input—when you press a key, something happens. This is a fundamental shift from running code top-to-bottom once to a program that waits around for the user to do something.

This folder has three demos. `etch_a_sketch.py` lets you drive the turtle with keyboard keys. `turtle_race.py` is a proper race with multiple turtles and a win condition. `main.py` is a simpler example of having several turtles on screen at once.

## How keyboard events work

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

## Multiple turtles and the race loop

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

This pattern—iterate over a list of objects, update each one, check a shared condition—is exactly what you'll see in games like Snake and Pong.

## Try it yourself

Drive the turtle around:

```bash
python "etch_a_sketch.py"
```

Then run the race and place a bet:

```bash
python "turtle_race.py"
```
