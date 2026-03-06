# Day 29 - Password Manager

Today we're building a password manager that generates secure passwords and saves them to a local file. This combines the GUI skills from Days 27-28 with file I/O from Day 24.

The app has three main jobs: generate a random password, let the user enter website and account details, and save everything to a text file.

## Generating passwords

The password generator creates a random mix of letters, numbers, and symbols:

```python
def generate_password():
    letters = ['a', 'b', 'c', ..., 'z', 'A', ..., 'Z']
    numbers = ['0', '1', ..., '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(10, 12))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    passwd_entry.delete(0, END)
    passwd, f"{password_entry.insert(0}")
    pyperclip.copy(password)
```

We build a list of random characters, shuffle it so the types are mixed up, join them into a string, and then copy it to the clipboard with `pyperclip.copy()`. That last step saves the user from manually selecting and copying the password.

## Saving data

When the user clicks Add, we validate the input and append to the file:

```python
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = passwd_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}\nPassword: {password}\n Is it Ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"Website Name: {website} | Username: {username} | Password: {password}\n")
            website_entry.delete(0, END)
            passwd_entry.delete(0, END)
```

We use `messagebox.askokcancel()` to show a confirmation dialog. The "a" mode in `open()` appends to the file instead of overwriting it, so we keep a history of all saved passwords.

## Environment variables

Notice this line:

```python
username_entry.insert(0, os.environ.get("MY_EMAIL", ""))
```

We use an environment variable for the default email. If `MY_EMAIL` isn't set in your system, it defaults to an empty string instead of crashing.

## Try it yourself

```bash
python "main.py"
```

Generate a password, enter a website name, and click Add. Check the `data.txt` file afterward to see your saved credentials.
