import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#019267"
YELLOW = "#F2FA5A"
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
reps = 0
timer = None

def count_down(count):
    """Create the countdown mechanism inside the canvas.
    Counts down by each second for the given interval (work, short break or long break).
    Adds a checkmark for each working interval completed.
    
    Args:
        count (int): Number of minutes to countdown from based on the Constants set.
    """
    count_min = math.floor(count / 60)
    count_sec = count % 60 
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)

def start_timer():
    """Add the Start Button functionality to start the countdown.
    Changes the countdown timer between Work interval and Break.
    Updates the Title label to show which interval is currently on.
    """
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
        focus_window("on")
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        focus_window("on")
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
        focus_window("off")

def reset_timer():
    """Add the Reset Button functionality to reset the countdown and all the text on the GUI.
    """
    global reps
    reps = 0
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")

def focus_window(option):
    """Enable the Tkinter window to show on top of other windows when minimized.

    Args:
        option (str): Set the function to 'on' or 'off'
    """
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "normal"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 16, "normal"), highlightthickness=0, borderwidth=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 16, "normal"), highlightthickness=0, borderwidth=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
