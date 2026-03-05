# Day 24 - File I/O, Context Managers, and Mail Merge Automation
Day 24 teaches how to read and write local files safely, then use string replacement to generate many personalized outputs from one template.

## What You Learn
- File reading patterns: `.read()` vs `.readlines()`.
- Safe file handling with `with open(...)` context managers.
- Cleaning raw text with `.strip()`.
- Template substitution with `.replace()`.
- Directory-aware output paths for generated files.

## Day 24 in This Folder
There are two learning tracks:
- `main.py`: basic file I/O operations (`append` and `write`).
- `main_mail_merge_project.py`: real automation pipeline for invitation letters.

## Mail Merge Flow
1. Load all names from `Input/Names/invited_names.txt`.
2. Load template from `Input/Letters/starting_letter.txt`.
3. Replace `[name]` with each cleaned name.
4. Save one letter per person under `Output/ReadyToSend/`.

```python
PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
```

## Practical Fix to Notice
In the output filename, this day currently uses `{name}` (which still contains `\n`). Use `{stripped_name}` in the filename too, otherwise generated files can include awkward trailing characters.

## Basic I/O Practice Snippet (`main.py`)

```python
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text")

with open("new_file.txt", mode="w") as file:
    file.write("\nNew text in a new file.")
```

## Common Pitfalls
- Wrong working directory: run from the Day 24 folder so relative `Input/...` paths resolve.
- Extra blank characters in names: always call `.strip()` before replacement/output naming.
- Accidentally overwriting outputs: `mode="w"` replaces file contents each run.

## Run
```bash
python "main_mail_merge_project.py"
# optional file I/O practice script
python "main.py"
```
