# Day 18 - Turtle Graphics, Color Systems, and Reusable Drawing Functions
Day 18 teaches how to control drawing state in `turtle` and build repeatable visual patterns with functions, loops, and random color generation.

## What Changes on This Day
You move from text-only programs to visual output. Instead of printing strings, you now control a drawing cursor (`Turtle`) on a 2D canvas.

## Concepts You Practice
- `turtle` screen lifecycle (`Screen()`, `exitonclick()`).
- Using helper functions to avoid duplicating drawing logic.
- RGB color mode with `turtle.colormode(255)`.
- Randomized visuals (`random.randint`, `random.choice`).
- Geometric iteration (angles, repeated turns, grid placement).

## Project Files and Their Roles
- `main_turtle_and_the_gui.py`: experiments and challenges (random walk, spirograph, shape patterns).
- `main.py`: Hirst-style dot painting grid using sampled color tuples.

## How the Hirst Dot Grid Works (`main.py`)
1. Set RGB mode so `(r, g, b)` tuples are valid.
2. Keep a curated `color_list` extracted from an image.
3. Define `draw_dots()` to draw one horizontal row.
4. Reposition turtle per row with `teleport()` and repeat 10 rows.

```python
def draw_dots():
    for item in range(10):
        color = random.choice(color_list)
        timmy.dot(20, color)
        timmy.forward(50)

for pos in range(10):
    y_pos += 50
    timmy.teleport(x_pos, y_pos)
    draw_dots()
```

## How the Spirograph Works (`main_turtle_and_the_gui.py`)
The drawing is created by repeating circles and rotating the heading a fixed gap each step.

```python
def spirograph(size_of_gap):
    for angle in range(int(360 / size_of_gap)):
        timmy.pencolor(random_color())
        timmy.circle(radius=100)
        timmy.setheading(timmy.heading() + size_of_gap)
```

This is a good example of turning a math idea (full 360-degree rotation) into code.

## Common Debug Issues on Day 18
- Colors look wrong: check `turtle.colormode(255)` is set before RGB tuples.
- Drawing starts off-screen: verify start coordinates (`x_pos`, `y_pos`).
- No window appears: ensure `Screen()` and `exitonclick()` run at the end.

## Run
```bash
python "main.py"
# or
python "main_turtle_and_the_gui.py"
```
