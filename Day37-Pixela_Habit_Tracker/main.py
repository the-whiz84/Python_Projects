import requests, webbrowser, os
from tkinter import *
from tkcalendar import *
from datetime import datetime as dt
from tkinter import messagebox
 
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "the-whiz"
GRAPH_ID = "graph1"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
URL = f"{GRAPH_ENDPOINT}.html"
TODAY = dt.now()
TOKEN = os.environ.get("PIXELA_TOKEN")

 
headers_data = {
    "X-USER-TOKEN": TOKEN
}

window = Tk()
window.title("Python Journey")
window.iconphoto(True, PhotoImage(file="images/python.png"))
window.resizable(width=False, height=False)
window.config(pady=20, padx=20, bg="white")
 
 
def open_browser():
    webbrowser.open(URL, new=1)
 
 
def format_date():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    cal.config(date_pattern="dd/MM/yyyy")
    return date
 
 
def add_pixel():
    endpoint = f"{GRAPH_ENDPOINT}"
    pixel_add = {
        "date": format_date(),
        "quantity": user_in.get(),
    }
    response = requests.post(url=endpoint, json=pixel_add, headers=headers_data)
    user_in.delete(0, END)
    if response.status_code == 200:
        messagebox.showinfo(message="Pixel added.")
    else:
        print(response.text)

 
def del_pixel():
    endpoint = f"{GRAPH_ENDPOINT}/{format_date()}"
    response = requests.delete(url=endpoint, headers=headers_data)
    messagebox.showinfo(message="Pixel deleted.")
    if response.status_code == 200:
        messagebox.showinfo(message="Pixel deleted.")
    else:
        print(response.text)
 

def change_pixel():
    endpoint = f"{GRAPH_ENDPOINT}/{format_date()}"
    pixel_update = {
        "quantity": user_in.get(),
    }
    response = requests.put(url=endpoint, json=pixel_update, headers=headers_data)
    user_in.delete(0, END)
    if response.status_code == 200:
        messagebox.showinfo(message="Pixel updated.")
    else:
        print(response.text)

 
cal = Calendar(window, selectmode="day", year=TODAY.year, month=TODAY.month, day=TODAY.day)
cal.grid(row=0, column=0, columnspan=4)

units = Label(text="Hours/Day:", highlightthickness=0)
units.grid(row=1, column=0, columnspan=2, pady=10, sticky="e")

user_in = Entry(width=10, highlightthickness=0)
user_in.grid(row=1, column=2, sticky="w")
 
add = Button(text="Add", command=add_pixel, highlightthickness=0)
add.grid(row=2, column=0, pady=10)

update = Button(text="Update", command=change_pixel, highlightthickness=0)
update.grid(row=2, column=1, pady=10, sticky="w")

delete = Button(text="Delete", command=del_pixel, highlightthickness=0)
delete.grid(row=2, column=2, pady=10, sticky="w")

link = Button(text="Show\nJourney", command=open_browser, highlightthickness=0)
link.grid(row=2, column=3)
 
window.mainloop()
