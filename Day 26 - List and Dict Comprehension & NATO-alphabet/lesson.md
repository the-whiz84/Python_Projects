# Day 26 - List/Dictionary Comprehensions and DataFrame-to-Dict Mapping

Comprehensions are one of Python's most powerful features for transforming data. Instead of building a list or dictionary with a loop, you can do it in a single line.

Today we also bridge between Pandas DataFrames and plain Python dictionaries—a common pattern when you need fast lookups instead of scanning through table rows.

## List comprehension

A list comprehension lets you build a new list from an existing sequence in one line:

```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
# squares is [1, 4, 9, 16, 25]
```

The pattern is `[expression for item in sequence]`. Whatever you put before the `for` gets evaluated for each item.

## Dictionary comprehension

Same idea, but for dictionaries. In the NATO alphabet project, we convert the CSV DataFrame into a dictionary where each letter maps to its phonetic code:

```python
phonetic_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}
```

This loops through every row in the DataFrame and builds a dictionary where the key is the letter column and the value is the code column. The result is something like `{"A": "Alfa", "B": "Bravo", ...}`.

## From DataFrame to dictionary

The `.iterrows()` method loops through a DataFrame one row at a time. Each iteration gives you the index and the row object, which lets you access columns as attributes:

```python
for index, row in alphabet_data.iterrows():
    print(row.letter, row.code)
```

The dictionary comprehension does this in one line and stores the result. Once you have a dictionary, looking up a letter is instant—no need to search through the DataFrame each time.

## Using the lookup

With the dictionary built, converting a word to NATO codes is straightforward:

```python
word_to_resolve = input("Provide a word: ").upper()
word_letters = [phonetic_dict[letter] for letter in word_to_resolve]
print(word_letters)
```

We convert the input to uppercase (since our dictionary has uppercase keys), then use a list comprehension to look up each letter's code.

## Try it yourself

```bash
python "main_nato_alphabet.py"
```

Type a word and see it converted to NATO phonetic alphabet codes.
