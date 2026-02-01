import tkinter
from tkinter import Button

# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=600, height=400)
#
# # Label
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")

# In the pack pop up we see no arguments provided, only these **kw which stands for kwargs

# 1. Advanced Arguments - are used to specigy a wide range of inputs.

# Keyword Arguments
# def my_function(a, b, c):
# 	# Do this with a
# 	# Then do this with b
# 	# Finally, do this with c
# my_function(c=3, a=1, b=2)
#
# # Arguments with default values
# def my_function(a=1, b=2, c=3):
# 	# Do this with a
# 	# Then do this with b
# 	# Finally, do this with c
#
# my_function() #or
# my_function(b=5)

# 2. *args - Many positional arguments.

# def add (n1, n2):
# 	return n1 + n2
#
# add(n1=5, n2=3)
# # Unlimited positional arguments
#
# def add(*args):
# 	for n in args:
# 		print(n)
# add(1, 3, 5, 7)
# The * collects all of the arguments in a tuple


# 3. **kwargs - Many keywords arguments

# def calculate(**kwargs):
	# print(kwargs)
	# for key, value in kwargs.items():
	# 	print(key)
	# 	print(value)
	# print(kwargs["add"])


# ** turns the keyword arguments into a dictionary


# 4. Button, Entry and setting Component Options
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=600, height=400)

# 4.1 Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Label Text" #or
# my_label.config(text="New Label Text")

# 4.2 Button

# def button_clicked():
# 	print("I got clicked")
#
# my_button = tkinter.Button(text="Click Me", command=button_clicked)
# my_button.pack()

# Challenge - Make the label text say "Button got Clicked" whenever we press the button
my_label.config(text="New Label Text")

# def button_clicked():
# 	my_label["text"] = "Button got Clicked"
#
# my_button = tkinter.Button(text="Click Me", command=button_clicked)
# my_button.pack()


# 4.3 Entry

# my_input = tkinter.Entry(width=10)
# my_input.pack()

# input_text = my_input.get()
# print(input_text)
# Nothing will be printed as the code is run before we are typing

# Challenge - Make the label text show the input text when button is clicked

def button_clicked():
	my_label.config(text=my_input.get())

my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.pack()

my_input = tkinter.Entry(width=10)
my_input.pack()


# 5. Other Tkinter Widgets: Radio buttons, Scales, Check buttons and more

# See other_tkinter_widgets file


# 6. Tkinter Layout Managers: pack(), place() and grid()

# See main2.py













window.mainloop()