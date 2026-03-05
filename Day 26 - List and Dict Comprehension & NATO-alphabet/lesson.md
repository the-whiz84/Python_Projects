# Day 26 - List/Dictionary Comprehensions and DataFrame-to-Dict Mapping
Day 26 teaches how to transform data compactly with comprehensions and how to bridge pandas rows into fast lookup dictionaries.

## What You Learn
- List comprehension syntax for transforming sequences.
- Dictionary comprehension syntax for key/value construction.
- Iterating DataFrames with `iterrows()`.
- Converting tabular data into lookup maps (letter -> NATO code).

## Real Project Focus
`main_nato_alphabet.py` is the core practical script:
1. Load NATO CSV into a DataFrame.
2. Build a phonetic dictionary with dictionary comprehension.
3. Convert user input into a list of code words with list comprehension.

```python
phonetic_dict = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}

word_to_resolve = input("Provide a word: ").upper()
word_letters = [phonetic_dict[letter] for letter in word_to_resolve]
print(word_letters)
```

## Why This Pattern Matters
A dictionary lookup (`phonetic_dict[letter]`) is much cleaner and faster than scanning the whole DataFrame for every letter. This is a common optimization in data-heavy scripts.

## About `main.py`
This file contains comprehension learning notes and pandas examples. It also includes a typo in the final example (`interrows` instead of `iterrows`) and placeholder field names (`row.new_key`). Treat it as tutorial scratch code, not production logic.

## Common Pitfalls
- `KeyError` for spaces/numbers: sanitize input or filter unsupported characters.
- Forgetting `.upper()` leads to missing lowercase keys in `phonetic_dict`.
- Using `interrows` instead of `iterrows` raises `AttributeError`.

## Run
```bash
python "main_nato_alphabet.py"
```
