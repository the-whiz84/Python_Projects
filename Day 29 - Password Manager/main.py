import pyperclip
import os
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

WHITE = "#F6F5F5"
BEIGE = "#F9E2AF"
TEAL = "#009FBD"
PURPLE = "#4A249D"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
			   'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_list = [choice(letters) for _ in range(randint(10, 12))]
	password_list += [choice(symbols) for _ in range(randint(2, 4))]
	password_list += [choice(numbers) for _ in range(randint(2, 4))]

	shuffle(password_list)

	password = "".join(password_list)

	passwd_entry.delete(0, END)
	passwd_entry.insert(0, f"{password}")
	pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
	website = website_entry.get()
	username = username_entry.get()
	password = passwd_entry.get()

	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
	else:
		is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}\nPassword: {password}\n "
															  f"Is it Ok to save?")
		if is_ok:
			with open("data.txt", "a") as file:
				file.write(f"Website Name: {website} | Username: {username} | Password: {password}\n")
			website_entry.delete(0, END)
			# username_entry.delete(0, END)
			passwd_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=TEAL)

canvas = Canvas(width=200, height=200, bg=TEAL, highlightthickness=0)
passwd_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=passwd_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg=TEAL, fg=WHITE, highlightthickness=0)
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", bg=TEAL, fg=WHITE, highlightthickness=0)
username_label.grid(row=2, column=0)

passwd_label = Label(text="Password:", bg=TEAL, fg=WHITE, highlightthickness=0)
passwd_label.grid(row=3, column=0)

website_entry = Entry(width=38, bg=TEAL, highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=38, bg=TEAL, highlightthickness=0)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, os.environ.get("MY_EMAIL", ""))

passwd_entry = Entry(width=21, bg=TEAL, highlightthickness=0)
passwd_entry.grid(row=3, column=1)

gen_passwd_button = Button(text="Generate Password", command=generate_password, highlightthickness=0, borderwidth=0)
gen_passwd_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save, width=35, highlightthickness=0, borderwidth=0)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
