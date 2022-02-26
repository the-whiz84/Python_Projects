from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20, bg="aqua")

# Entry field
input_number = Entry(width=10, justify="center")
input_number.insert(END, string="0")
input_number.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles", padx=10, pady=10, bg="aqua")
miles_label.grid(column=2, row=0)

# Is Equal label
equal_label = Label(text="is equal to", padx=10, pady=10, bg="aqua")
equal_label.grid(column=0, row=1)

# Result label
result_label = Label(text="0", padx=10, pady=10, bg="aqua")
result_label.grid(column=1, row=1)

# KM label
km_label = Label(text="Km", padx=10, pady=10, bg="aqua")
km_label.grid(column=2, row=1)

# Calculate Button
def calculate():
    """Summary: Converts the number provided from miles to km and displays the result.
    """
    miles = input_number.get()
    km = int(miles) * 1.609344
    result_label.config(text=round(km, 2))

calc_button = Button(text="Convert", padx=10, pady=10, command=calculate, bg="white", activebackground="lime")
calc_button.grid(column=1, row=2)


window.mainloop()
