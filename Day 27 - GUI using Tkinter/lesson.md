# Day 27 - Tkinter Widgets, Callbacks, and Layout Managers
Day 27 introduces desktop GUI programming with Tkinter, including widget creation, event callbacks, and layout control with `pack` and `grid`.

## What You Learn
- Creating a Tkinter app window (`Tk`, title, size, padding).
- Building widgets (`Label`, `Button`, `Entry`).
- Handling user actions with callback functions (`command=...`).
- Reading input values from `Entry` and updating UI state.
- Laying out components with `pack()` and `grid()`.

## Day 27 Files
- `main.py`: Tkinter basics, callback binding, and notes on `*args`/`**kwargs`.
- `mile_to_km_converter.py`: practical conversion app using `grid` layout.
- `main2.py`, `other_tkinter_widgets.py`: additional layout/widget experiments.

## Real App Example (`mile_to_km_converter.py`)

```python
def convert():
    number_to_convert = float(miles_input.get())
    km_value = round(number_to_convert * 1.609)
    output_label.config(text=km_value)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)
```

This is the core event-driven pattern for Tkinter: user action -> callback -> UI update.

## Callback Example (`main.py`)

```python
def button_clicked():
    my_label.config(text=my_input.get())

my_button = tkinter.Button(text="Click Me", command=button_clicked)
```

The function is passed by reference (`button_clicked`), not called immediately.

## Common Pitfalls
- Button callback not firing: `command=button_clicked()` is wrong; use `command=button_clicked`.
- Layout conflicts: do not mix `pack` and `grid` in the same parent container.
- Conversion crash on empty input: guard `float(miles_input.get())` with validation.

## Run
```bash
python "mile_to_km_converter.py"
# or
python "main.py"
```
