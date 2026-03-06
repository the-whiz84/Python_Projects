# Day 27 - Tkinter Widgets, Callbacks, and Layout Managers

So far, all our programs have run in the terminal. Today we're building actual desktop applications with a Graphical User Interface, using Tkinter—Python's built-in GUI library.

The mileage converter in `mile_to_km_converter.py` is a complete tiny app: you type a number, click a button, and it shows the converted result. This introduces the core patterns of GUI programming.

## Creating the window

Every Tkinter app starts with a window object:

```python
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)
```

`padx` and `pady` add space around everything inside the window so it doesn't feel cramped.

## Input, labels, and buttons

The widgets you need are Entry (text box), Label (text display), and Button:

```python
miles_input = Entry(width=5)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()
```

The `grid()` method places widgets in rows and columns. It's one of two main layout systems in Tkinter (the other is `pack`, which stacks widgets vertically).

## Callbacks: connecting actions

The key to any interactive GUI is the callback function. When the button is clicked, Tkinter calls the function you passed to `command`:

```python
def convert():
    number_to_convert = float(miles_input.get())
    km_value = round(number_to_convert * 1.609)
    output_label.config(text=km_value)
```

Notice we pass the function itself (`command=convert`), not call it (`command=convert()`). If you add parentheses, the function runs immediately when the app starts, not when you click.

`.get()` retrieves what's typed in the Entry field. `.config(text=...)` updates the Label to show the new result.

## Why this matters

This is the foundation for every GUI app you'll build. Whether it's a password manager, a Pomodoro timer, or a weather dashboard, the pattern is always the same: create widgets, lay them out, connect buttons to functions that read input and update the display.

## Try it yourself

```bash
python "mile_to_km_converter.py"
```

Type a number of miles and click Calculate. Try changing the conversion formula to go the other direction, or add a new button that clears the input.
