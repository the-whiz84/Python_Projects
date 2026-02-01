from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

def convert():
	number_to_convert = float(miles_input.get())
	km_value = round(number_to_convert * 1.609)
	output_label.config(text=km_value)

miles_input = Entry(width=5)
miles_input.grid(row=0, column=1)
miles_input.insert(END, string="0")

miles_label = Label(text="Miles", font=("Century", 16, "normal"))
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", font=("Century", 16, "normal"))
equal_label.grid(row=1, column=0)

output_label = Label(text="0", font=("Century", 16, "normal"))
output_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Century", 16, "normal"))
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()
