# Day 24 - File I/O, Context Managers, and Mail Merge Automation

Day 24 moves from in-memory programs into file automation. Instead of only handling values created during the current run, the script reads names from a file, reads a template letter from another file, customizes that template, and writes a separate output file for each person. That is a major shift because the program now works with data that exists before the script starts and leaves behind files after it ends.

## 1. Reading Files with Context Managers

The project reads input files using `with open(...)` blocks:

```python
with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
```

This is the safest default pattern for file access in Python. The context manager opens the file for you and closes it automatically when the block ends.

That matters more than it seems. Once programs start dealing with real files, resource cleanup becomes part of writing correct code, not just a technical detail.

## 2. Treating the Letter as a Reusable Template

The core automation works by reading the letter once and reusing it for every name:

```python
PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
```

This is an important design choice. The template stays unchanged in the source file, and each customized letter is produced from that original text. That means the program has a clear input artifact and a repeatable output process.

The actual replacement happens here:

```python
for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
```

`.replace()` turns the template into a personalized letter, and `.strip()` removes the newline characters that came from `readlines()`. Without `.strip()`, the generated filenames and letter content would include unwanted line breaks.

## 3. Writing Many Output Files from One Loop

Each personalized letter is written inside the same loop:

```python
with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
    completed_letter.write(new_letter)
```

This is the full mail merge pattern in miniature:

- read source data
- transform it
- write a new artifact for each record

That workflow appears everywhere in automation. The specific project is letters, but the same structure could be used for reports, invoices, configuration files, or batch-generated documents.

## 4. Why Relative Paths Matter in Real Projects

The script uses relative paths such as:

```python
"Input/Names/invited_names.txt"
```

That works only when the program is run from the correct project folder. It is a good early reminder that file-based programs depend not only on code, but also on where the code is executed from and how the directory structure is organized.

As projects grow, path handling becomes part of the program design.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main_mail_merge_project.py
```

3. Check the `Output/ReadyToSend/` directory after the script finishes.
4. Confirm that a separate `letter_for_<name>.txt` file was created for each person listed in `Input/Names/invited_names.txt`.

## Summary

Day 24 introduces file I/O through a practical automation task. You read structured input from files, use a template plus placeholder replacement to generate personalized content, and write multiple output files in a loop. The lesson is simple, but it marks an important transition from toy scripts to programs that work with real artifacts on disk.
