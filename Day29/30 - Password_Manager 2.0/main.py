from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip

WHITE = "#F6F5F5"
BEIGE = "#F9E2AF"
TEAL = "#009FBD"
PURPLE = "#4A249D"

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
    """Save the Website, Username and Password in a data.json file in the same folder. Entries are case sensitive.

    If one of the fields is empty, a pop-up window will show an error. After clicking Add a pop-up confirmation box will appear before saving to file.
    If there is already an entry for the website, a popup window will ask if you want to overwrite the existing entry.

    WARNING! All data is saved in clear text in the file!
    """
    password = password_entry.get()
    username = username_entry.get()
    website = website_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="OOPS", message="Please fill in all the fields before clicking Add")

    else:
        try:
            with open("data.json", "r") as save_file:
                data = json.load(save_file)
                if website in data:
                    update = messagebox.askyesno("Warning", f"There is already a password saved for {website}.\nWould you like to overwrite?")
                    if update:
                        pass
                    else:
                        return

        except FileNotFoundError:
            with open("data.json", "w") as save_file:
                json.dump(new_data, save_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as save_file:
                json.dump(data, save_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH WEBSITE ------------------------------- #

def find_password():
    """Search for a website entry in data.json file and show the username and password in a popup window.
    If there is no entry with the given name, an error message will be displayed.
    If you try to search for an entry before data.json was generated, an error message will be displayed.

    Search is case sensitive.
    """
    website_name = website_entry.get()

    if len(website_name) == 0:
        messagebox.showerror(title="Error", message="Please enter a valid website name to search.")

    else:
        try:
            with open("data.json", "r") as save_file:
                data = json.load(save_file)

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found.")

        else:
            if website_name in data:
                password = data[website_name]["password"]
                username = data[website_name]["email"]
                messagebox.showinfo(title=website_name, message=f"Username: {username}\nPassword: {password}")
            
            else:
                messagebox.showerror(title="Error", message=f"No details for {website_name} exist.")
        
        finally:
            website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=TEAL )

canvas = Canvas(width=200, height=200, bg=TEAL , highlightthickness=0)
passwd_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=passwd_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg=TEAL, fg=WHITE, highlightthickness=0)
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", bg=TEAL, fg=WHITE, highlightthickness=0)
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=TEAL, fg=WHITE, highlightthickness=0)
password_label.grid(row=3, column=0)

website_entry = Entry(bg=TEAL, highlightthickness=0)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

username_entry = Entry(bg=TEAL, highlightthickness=0)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0, "example@mailinator.com")

password_entry = Entry(bg=TEAL, highlightthickness=0)
password_entry.grid(row=3, column=1, sticky="EW")

gen_pass_button = Button(text="Generate Password", highlightthickness=0, borderwidth=0, command=generate_password)
gen_pass_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=38, command=save, highlightthickness=0, borderwidth=0)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", highlightthickness=0, borderwidth=0, command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

window.mainloop()
