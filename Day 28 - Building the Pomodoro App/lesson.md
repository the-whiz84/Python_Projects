# Day 28 - Pomodoro Timer Logic and Tkinter Scheduling

The Pomodoro Technique is a time management method: you work for 25 minutes, take a short break, and repeat. After four work sessions, you take a longer break. Today we're building a visual timer that follows this exact pattern.

This builds directly on what we learned in Day 27 with Tkinter, but now we're using `window.after()` to schedule events in the future—essential for any timer or countdown app.

## The timer logic

The core function counts down from a given number of seconds:

```python
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
```

`window.after(1000, count_down, count - 1)` is the key line. It tells Tkinter: "wait 1000 milliseconds (1 second), then call `count_down` again with the new value." This creates the countdown effect without blocking the UI.

## Work and break scheduling

The `start_timer()` function decides what to do based on how many sessions you've completed:

```python
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
```

Every even rep (2, 4, 6) is a short break. Every 8th rep is a long break. Everything else is a work session. We use modulo (`%`) to cycle through these states.

## Visual feedback

When a work session completes, we add a checkmark to show progress:

```python
marks = ""
work_sessions = math.floor(reps/2)
for _ in range(work_sessions):
    marks += "✔"
check_label.config(text=marks)
```

The number of checkmarks equals completed work sessions, so after four work sessions (8 total reps), the user sees four checkmarks.

## The UI setup

We use a Canvas widget to display the tomato image and the countdown text on top of it:

```python
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
```

Canvas lets you layer text on images, which is perfect for this kind of timer display.

## Try it yourself

```bash
python "main.py"
```

Click Start to begin a work session. The timer counts down from 1 minute (we use 1 minute instead of 25 for testing purposes). When it hits zero, it automatically starts the next session. Click Reset to start over.
