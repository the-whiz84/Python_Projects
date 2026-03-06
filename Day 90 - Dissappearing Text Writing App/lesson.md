# Day 90 - Inactivity Timers and Focused Writing UI Behavior

This project is simple on purpose. The app gives you a blank writing space, starts a countdown when you begin typing, and deletes everything if you stop for too long. That makes it a good lesson in inactivity tracking rather than in text editing itself.

The whole behavior lives inside one idea: reset the timer on every keypress and punish silence.

## 1. Gate the Writing Session Explicitly

The writing area starts disabled:

```python
self.text_area = tk.Text(
    self.root,
    font=("Helvetica", 16),
    wrap="word",
    bg="white",
    fg="black",
    state=tk.DISABLED,
)
```

The user must press `Start Writing` before the session begins. That is a good UX choice because it makes the state transition obvious: before the test starts, the timer is idle and the editor is locked.

The start handler flips the app into active mode:

```python
def start_writing(self):
    self.text_area.config(state=tk.NORMAL)
    self.text_area.focus()
    self.timer_running = True
    self.start_button.pack_forget()
    self.text_area.bind("<KeyPress>", self.on_key_press)
    self.last_keypress_time = time.time()
    self.countdown()
```

## 2. Reset the Countdown on Every Keystroke

The rule of the app is enforced through one event handler:

```python
def on_key_press(self, event=None):
    self.last_keypress_time = time.time()
    self.remaining_time = self.time_limit
    self.timer_label.config(
        text=f"Time left: {self.remaining_time} seconds", fg="white", bg="black"
    )
```

That is the key mechanic. The app does not care what you type. It only cares that you keep typing.

This is a useful pattern for any inactivity-based interface:

- record the last meaningful interaction
- measure elapsed time against it
- update the display continuously

## 3. Use `after()` to Build a Repeating UI Timer

Tkinter does not need threads here. The countdown is driven through `after()`:

```python
def countdown(self):
    if self.timer_running:
        current_time = time.time()
        self.remaining_time = self.time_limit - (
            current_time - self.last_keypress_time
        )
```

If the user stops typing for too long, the consequence is immediate:

```python
if self.remaining_time <= 0:
    self.remaining_time = 0
    self.timer_running = False
    self.text_area.delete(1.0, tk.END)
    self.timer_label.config(
        text="Text deleted! Start typing again.", fg="red", bg="black"
    )
```

If time remains, the method schedules itself again:

```python
self.root.after(1000, self.countdown)
```

That is a standard Tkinter timer pattern and a good one to remember for any GUI that needs periodic updates.

## 4. Make the Feedback Match the Pressure

The timer label changes color when the remaining time becomes dangerous:

```python
if self.remaining_time <= 3:
    self.timer_label.config(fg="red")
else:
    self.timer_label.config(fg="white")
```

This is a small touch, but it matters. The app is deliberately stressful, and the visual feedback supports that design.

The project also shows a message box when the text is deleted, then restores the `Start Writing` button so the user can begin again. That keeps the failure path clear instead of leaving the app in a confusing half-active state.

## How to Run the Dangerous Writing App

1. Tkinter is included with most standard Python installs.
2. Run the app:
   ```bash
   python main.py
   ```
3. Press `Start Writing`, begin typing, and verify:
   - the timer starts once writing begins
   - each keypress resets the countdown
   - the timer label turns red near the end
   - all text is deleted if you stop typing long enough

## Summary

Today, you built a UI around inactivity rather than around content. The project tracks the time since the last keypress, updates the countdown through Tkinter's event loop, and resets the session cleanly when the user stops. The idea is simple, but the timer pattern is reusable far beyond this writing app.
