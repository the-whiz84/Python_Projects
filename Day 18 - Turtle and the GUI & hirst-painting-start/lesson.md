# Day 18 - Turtle Graphics, Color Systems, and Reusable Drawing Functions

Today is the day we leave the terminal behind and start drawing on screen. Up until now, every program you've written produced text output. Now we're controlling a little "turtle" that drags a pen around a canvas.

This folder has two parts. `main_turtle_and_the_gui.py` walks through several drawing challenges—the spirograph is the most satisfying one. `main.py` is the final project: a Hirst-style dot painting that samples colors and arranges them in a grid.

## Getting the turtle on screen

The first thing you need is the screen and the turtle object:

```python
timmy = Turtle()
timmy.shape("turtle")

screen = Screen()
screen.exitonclick()
```

That `exitonclick()` is the magic line that keeps the window open until you click it. Without it, the program runs, draws everything, and closes the window before you can even see what happened.

## RGB colors and why they matter

By default, turtle understands color names like "red" or "ForestGreen". But if you want specific colors from an image, you need RGB tuples. The trick is setting the color mode first:

```python
turtle.colormode(255)
```

After that, you can use tuples like `(255, 0, 0)` for red. In `main_turtle_and_the_gui.py`, we build a helper function to generate random colors:

```python
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple
```

Now every time we call `random_color()`, we get a fresh RGB tuple we can pass to `pencolor()`.

## The spirograph challenge

This is the most satisfying visual in the folder. A spirograph is just a circle drawn over and over, each time rotated by a small angle. When you do enough rotations, the patterns overlap into something beautiful:

```python
def spirograph(size_of_gap):
    for angle in range(int(360 / size_of_gap)):
        timmy.pencolor(random_color())
        timmy.circle(radius=100)
        timmy.setheading(timmy.heading() + size_of_gap)

spirograph(10)
```

The math here is simple: 360 degrees makes a full circle. If we rotate by 10 degrees each time, we need 36 iterations to come back around. That's what `int(360 / size_of_gap)` calculates for us. Call `spirograph(5)` for a denser pattern or `spirograph(45)` for something more open.

## The Hirst dot painting

In `main.py`, we take a curated list of colors extracted from an image and arrange them in a 10x10 grid. The turtle doesn't actually draw lines here—it just drops dots:

```python
def draw_dots():
    for item in range(10):
        color = random.choice(color_list)
        timmy.dot(20, color)
        timmy.forward(50)
```

Then we reposition the turtle after each row:

```python
for pos in range(10):
    y_pos += 50
    timmy.teleport(x_pos, y_pos)
    draw_dots()
```

`timmy.teleport()` moves the turtle without drawing anything. That's essential—we only want dots, not lines connecting them.

## Why this day matters

Today you're learning to think about coordinate systems and state. The turtle has a position, a heading, a pen up or down state, and a color. Every command you give changes one of those things. It's a gentle introduction to game development concepts before we build actual games.

## Try it yourself

```bash
python "main_turtle_and_the_gui.py"
```

Try changing the gap size in the spirograph. Then run the dot painting:

```bash
python "main.py"
```
