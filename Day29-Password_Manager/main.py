from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generate a random password using 8-10 letters, 2-4 symbols and 2-4 numbers.

    Insert the generated password in the password field and copy it to clipboard.
    """
    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SYMBOLS = ['a', 'b', 'c', 'd', '!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_list += [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_list += [choice(NUMBERS) for _ in range(randint(2, 4))]

    shuffle(password_list)
    random_password = "".join(password_list)
    password_entry.delete(0, END)

    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """Save the Website, Username and Password in a data.txt file in the same folder.

    If one of the fields is empty, a pop-up window will show an error. After clicking Add a pop-up confirmation box will appear before saving to file.

    WARNING! All data is saved in clear text in the file!
    """
    password = password_entry.get()
    username = username_entry.get()
    website = website_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="OOPS", message="Please fill in all the fields before clicking Add")
    else: 
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as save_file:
                save_file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=30, bg="teal")

canvas = Canvas(width=200, height=200, bg="teal", highlightthickness=0)
passwd_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=passwd_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="teal", fg="white", font=("Consolas", 12, "bold"))
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", bg="teal", fg="white", font=("Consolas", 12, "bold"))
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="teal", fg="white", font=("Consolas", 12, "bold"))
password_label.grid(row=3, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

username_entry = Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0, "example@mailinator.com")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

gen_pass_button = Button(text="Generate Password", highlightthickness=1, fg="red", font=("Consolas", 8, "bold"), command=generate_password)
gen_pass_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, fg="red", font=("Consolas", 10, "bold"), command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
