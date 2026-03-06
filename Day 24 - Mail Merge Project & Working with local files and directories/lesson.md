# Day 24 - File I/O, Context Managers, and Mail Merge Automation

Today we're stepping away from games and into file automation. The goal is simple: we have a list of names and a letter template, and we want to generate a personalized letter for every name in the list.

This is the first day where we read and write actual files on your hard drive, not just variables in memory.

## Reading files with context managers

The safest way to open a file in Python is with a `with` block, also called a context manager. It makes sure the file gets closed properly even if something goes wrong:

```python
with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
```

`readlines()` gives us a list where each line from the file becomes one string in the list. If the file has 5 names, we get a list of 5 strings.

## The mail merge logic

Here's the full flow in `main_mail_merge_project.py`:

```python
PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
```

Notice the `.strip()` call. When you read lines from a file, each line includes a newline character `\n` at the end. If you use the name directly without stripping it, your output files would have awkward trailing newlines in their names. `.strip()` removes those extra whitespace characters.

The `.replace()` method does the actual work—it finds every `[name]` in the template and swaps it with the actual name.

## Writing to new files

The inner `with open(...)` block creates a brand new file for each letter. The `mode="w"` means we're opening it in write mode, which creates the file if it doesn't exist or overwrites it if it does.

Each letter gets saved as `letter_for_John.txt`, `letter_for_Sarah.txt`, and so on in the `Output/ReadyToSend/` directory.

## Directory awareness

One thing to watch: these relative paths (`Input/Names/...`) only work if you run the script from the Day 24 folder. If you're in a different directory, Python won't find the files. This is why running scripts from their project folder matters.

## Try it yourself

```bash
python "main_mail_merge_project.py"
```

Check the `Output/ReadyToSend/` folder afterward—you'll see a personalized letter for each name in the input file.
