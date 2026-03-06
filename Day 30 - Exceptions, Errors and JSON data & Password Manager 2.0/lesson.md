# Day 30 - Exceptions, Errors, JSON Data, and Password Manager 2.0

Today we're upgrading the password manager from Day 29. Instead of saving to a plain text file, we use JSON—a structured format that makes it easy to look up specific passwords later. We also learn how to handle errors gracefully with try/except blocks.

This is the first day where we systematically deal with things going wrong: missing files, wrong data formats, and edge cases.

## JSON basics

JSON (JavaScript Object Notation) stores data in a structure that looks like a Python dictionary:

```python
import json

# Writing to JSON
new_data = {
    website: {
        "email": email,
        "password": password,
    }
}
with open("data.json", "w") as data_file:
    json.dump(new_data, data_file, indent=4)
```

`json.dump()` writes a Python dictionary to a file in JSON format. The `indent=4` makes it readable when you open the file.

Reading it back:

```python
with open("data.json", "r") as data_file:
    data = json.load(data_file)
```

Now `data` is a Python dictionary you can look up by website name.

## Handling missing files

The problem with opening files is they might not exist yet. Instead of crashing, we catch the error:

```python
try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)
else:
    data.update(new_data)
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
```

If the file doesn't exist, we create it with the new data. If it does exist, we load it, update it with the new entry, and save it back.

## Looking up passwords

Now we can search for a specific website:

```python
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file present.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")
```

We try to read the file, handle the case where it doesn't exist, and then check if the specific website is in our data.

## Why this matters

Exception handling is what separates scripts that work in ideal conditions from scripts that work in the real world. File operations always have a chance of failing—permissions, deleted files, disk errors. Using try/except lets your program keep running and handle problems gracefully.

## Try it yourself

```bash
python "main_password_manager_2_0.py"
```

Add a few passwords, then search for one by name. Check the `data.json` file to see how the structured data looks.
