from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=100)
my_label.grid(row=0, column = 0)
my_label.config(padx=20,pady=20)

#Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
# button.place(x=200, y=300)
button.grid(row=1, column=1)

new_button = Button(text="New Button Click", command=button_clicked)
new_button.grid(row=0, column=2)

#Entry
input = Entry(width=10)
print(input.get())
# input.pack()
# input.place(x=300, y=100)
input.grid(row=2, column=3)


# Pack() arranges all elements next to each other starting from the center by default

# Place() requires x and y coordinates and can be arranges anywhere in the window
# The (0, 0) position is top left unlike the Turtle window and only has positive values

# Grid() will transform the window in a specified grid of rows and columns.
# This makes it the preferred method as it is relative to other components on the screen.

# You cannot mix up pack() and grid() in the same program.
# _tkinter.TclError: cannot use geometry manager pack inside . which already has slaves managed by grid

# Challenge - Add a new button positioned like this:
# label at 0,0
# new button at 0,2
# button at 1,1
# entry at 2,3



window.mainloop()