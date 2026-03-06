# Day 28 - Pomodoro Timer Logic and Tkinter Scheduling

Day 28 takes the Tkinter basics from the previous lesson and applies them to a timer-driven app. The Pomodoro project is more than a GUI with buttons and labels. It introduces scheduled callbacks, repeated state transitions, and reset behavior, which makes it one of the first desktop apps in the course that has to manage time as part of its logic.

## 1. Using `after()` to Build a Countdown Without Freezing the Window

The countdown is powered by this function:

```python
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
```

`window.after(1000, count_down, count - 1)` is the main idea of the lesson. It tells Tkinter to wait one second, then call the same function again with a smaller number.

That matters because the UI stays responsive. A normal `time.sleep()` loop would freeze the window and make the app feel broken. `after()` lets Tkinter keep handling button clicks and screen updates while the countdown continues.

## 2. Modeling Work and Break Cycles with a Repetition Counter

The session logic lives in `start_timer()`:

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

The `reps` variable turns the timer into a cycle:

- odd reps are work sessions
- even reps are short breaks
- every eighth rep is a long break

This is a strong example of using one simple state variable to control a larger workflow. The app does not need separate counters for work rounds and break rounds because `reps` already encodes that sequence.

## 3. Resetting Scheduled Work Correctly

The reset function is just as important as the countdown:

```python
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
```

`after_cancel(timer)` is the crucial line. Without it, the previously scheduled callback would still fire even after the user pressed Reset.

This is one of the more practical lessons in GUI programming: once you schedule future work, you also need a clean way to cancel it.

## 4. Using Visual Feedback to Show Progress

The app also updates the interface to show completed work sessions:

```python
marks = ""
work_sessions = math.floor(reps/2)
for _ in range(work_sessions):
    marks += "✔"
check_label.config(text=marks)
```

That checkmark row is simple, but it makes the app feel much more understandable to the user. The timer is no longer just counting down. It is communicating where the user is in the Pomodoro cycle.

The canvas setup reinforces that same idea visually by layering timer text over the tomato image:

```python
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
```

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Click `Start` and confirm that the timer updates once per second without freezing the window.
4. Click `Reset` and verify that the countdown stops, the timer display returns to `00:00`, and the session markers clear.

## Summary

Day 28 turns Tkinter widgets into a time-based application. You use `after()` to schedule repeated callbacks, use a repetition counter to alternate between work and break sessions, cancel pending callbacks during reset, and provide visual feedback with labels and checkmarks. It is an important lesson because it shows how GUI apps manage state over time, not just on button clicks.
