# Day 08 - Functions with Parameters and Caesar Cipher Logic
Day 08 focuses on passing parameters into reusable functions and transforming text deterministically.

## Goal

Implement Caesar cipher encode/decode with:
- function-based logic
- configurable shift amount
- support for non-alphabet characters
- repeatable encrypt/decrypt loop

## Day-Specific Logic

The `caesar()` function receives all behavior through parameters:
- `original_text`
- `shift_amount`
- `encode_or_decode`

For decoding, the script flips shift direction (`shift_amount *= -1`).
For wrapping, it uses modulo with alphabet length.

## Code Reference

From `main.py`:

```python
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
```

## Run

```bash
python "main.py"
```
