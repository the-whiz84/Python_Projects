# Day 27 - Tkinter Widgets, Callbacks, and Layout Managers

Day 27 introduces desktop GUI programming with Tkinter. That changes the mental model of the course quite a bit. Terminal scripts start, run top to bottom, and exit. A GUI app creates a window, waits for user actions, and responds through callbacks. The mileage converter is small, but it teaches the basic structure behind almost every Tkinter app that follows.

## 1. Creating a Window and Starting the Event Loop

Every Tkinter program begins by creating a window:

```python
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)
```

This sets up the application container. The important line comes at the end:

```python
window.mainloop()
```

`mainloop()` starts Tkinter’s event loop. From that point on, the program waits for clicks, text entry, or other user actions. That is the core shift of the day: the app does not keep running through your code automatically. It sits idle until the user does something.

## 2. Building the Interface from Widgets

The converter uses a few standard widgets:

```python
miles_input = Entry(width=5)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)
```

Each widget has a clear role:

- `Entry` collects text input
- `Label` shows information
- `Button` triggers an action

The `grid()` method places those widgets into rows and columns. That is important because layout is part of GUI design. The interface is not only what widgets you create, but where you place them and how they relate visually.

## 3. Connecting User Actions to Callback Functions

The button works because it is connected to a callback:

```python
def convert():
    number_to_convert = float(miles_input.get())
    km_value = round(number_to_convert * 1.609)
    output_label.config(text=km_value)
```

Then the button references that function:

```python
button = Button(text="Calculate", command=convert)
```

This is one of the most important GUI patterns in the course:

- read input from a widget
- compute a result
- update another widget

The key detail is that `command=convert` passes the function itself. If you wrote `convert()`, the function would run immediately when the app starts instead of waiting for the button click.

## 4. Why This Day Matters for the Next GUI Projects

The folder also contains supporting files like `main.py`, `main2.py`, and `other_tkinter_widgets.py`, which introduce more widgets and layout tools. But the real foundation is already visible in the converter:

- create a window
- add widgets
- arrange them with a layout manager
- connect actions to callbacks
- let the event loop drive the app

Once that model makes sense, later projects like the password manager, flashcards, and Pomodoro timer feel much less magical.

## How to Run the Project

1. Open a terminal in this folder.
2. Run the mileage converter:

```bash
python mile_to_km_converter.py
```

3. Enter a mile value and click `Calculate`.
4. Confirm that the callback reads the input, converts it, and updates the result label in the window.

## Summary

Day 27 introduces the event-driven model behind desktop GUI applications. You create a Tkinter window, place widgets with a layout manager, connect button clicks to callback functions, and keep the app alive with `mainloop()`. The mileage converter is simple, but it establishes the full structure that later GUI apps build on.
