# Day 30 - Exceptions, Errors, JSON Data, and Password Manager 2.0

Day 30 upgrades the password manager from a plain text logger into a small structured data app. It also introduces exception handling in a realistic setting. The lesson matters because it shows two things at once: how to store data in a format you can search later, and how to keep the program usable when files or keys are missing.

## 1. Why JSON Is Better Than Plain Text for This App

The new password manager stores entries as nested dictionaries:

```python
new_data = {
    website: {
        "email": email,
        "password": password,
    }
}
```

That structure maps naturally to JSON. Instead of writing one long line per entry, the app can store data in a format that preserves keys and values explicitly.

Writing the file looks like this:

```python
with open("data.json", "w") as data_file:
    json.dump(new_data, data_file, indent=4)
```

The `indent=4` argument is not required for correctness, but it makes the saved file readable. That matters because JSON is often both machine-readable and human-inspectable.

## 2. Using `try` / `except` / `else` to Handle File State Cleanly

The save workflow is built around exception handling:

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

This is a very practical example of why exception handling exists. The program has two valid situations:

- the file does not exist yet
- the file exists and should be updated

Instead of checking everything manually ahead of time, the code tries the normal read path first and handles the missing-file case only when needed.

That makes the program clearer because the main path stays focused on the common case.

## 3. Turning Stored Data into Searchable Records

Once the data lives in JSON, the app can search by website:

```python
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
```

Then it looks for the site key:

```python
if website in data:
    messagebox.showinfo(
        title=website,
        message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}"
    )
```

This is the real upgrade over Day 29. The app is no longer just saving entries. It is storing them in a structure that supports retrieval.

That change is what makes JSON worth introducing here. A storage format becomes valuable when it supports the next feature you want to build.

## 4. Keeping the GUI Workflow Clean Even When Errors Happen

The save function still preserves the interface flow from Day 29:

- collect the current form values
- validate required fields
- attempt to load existing data
- create or update the JSON file
- clear the relevant input fields

The final cleanup happens in `finally`:

```python
finally:
    website_entry.delete(0, END)
    passwd_entry.delete(0, END)
```

That keeps the UI consistent regardless of whether the file already existed or had to be created. It is a good reminder that error handling is not only about preventing crashes. It is also about keeping the user experience predictable.

## How to Run the Project

1. Open a terminal in this folder.
2. Run the upgraded manager:

```bash
python main_password_manager_2_0.py
```

3. Add a few website entries and confirm that `data.json` is created or updated.
4. Use the search feature to look up a saved website and verify that the stored email and password are shown in the dialog.

## Summary

Day 30 turns the password manager into a structured data application. JSON gives the app a searchable storage format, and exception handling makes the file workflow safe when `data.json` does not exist yet. The bigger lesson is that storage design and error handling are closely connected once programs start persisting real data.
