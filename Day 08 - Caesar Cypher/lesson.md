# Day 08 - Functions with Parameters and Caesar Cipher Logic

Today we're building a Caesar cipher program. It shifts letters forward or backward through the alphabet to encode or decode a message. The encryption idea is old, but it gives you a practical reason to write your own function, pass values into it, and reuse that function inside a loop.

## 1. Wrapping Logic Inside a Reusable Function

The center of the project is the `caesar()` function:

```python
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
```

This is the first day where the main logic is packaged into a reusable block instead of being written once from top to bottom. That matters because the program needs to do the same job repeatedly for different user inputs.

The parameters tell the function everything it needs:

- `original_text` is the message to transform
- `shift_amount` is how far to move each letter
- `encode_or_decode` decides whether the shift goes forward or backward

That is the larger lesson behind the cipher. Functions let you separate the job from the specific values used on each run.

## 2. Shifting Letters and Wrapping Around the Alphabet

The main transformation happens here:

```python
shifted_position = alphabet.index(letter) + shift_amount
shifted_position %= len(alphabet)
output_text += alphabet[shifted_position]
```

The first line finds the current letter position and adds the shift. The second line is the important one: `%=` wraps the index back into the valid alphabet range.

Without that step, shifting past `'z'` would push the index outside the list. With modulo, the cipher loops back to the beginning cleanly. That is why a shift can be small or large and still work correctly.

## 3. Preserving Characters That Should Not Change

The function also protects spaces and punctuation:

```python
for letter in original_text:
    if letter not in alphabet:
        output_text += letter
    else:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
```

This check makes the program more practical. A real message often contains spaces, numbers, or punctuation marks, and users expect those characters to stay readable.

That small `if` statement is doing quality-of-life work: the cipher transforms only what belongs to the alphabet and leaves everything else alone.

## 4. Reusing the Function in a Repeating Program Loop

Outside the function, the script runs inside a `while` loop:

```python
while not game_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
```

This is a strong pattern to learn early:

- collect fresh input
- pass it into a function
- let the function handle the core logic
- repeat until the user chooses to stop

It is a much cleaner design than rewriting the cipher logic directly inside the loop body every time.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Choose `encode` or `decode`, enter a message, and provide a shift value.
4. Test the program by encoding a message first, then decoding it with the same shift.

## Summary

Day 08 introduces user-defined functions through a real text transformation problem. You pass values into `caesar()`, use modulo arithmetic to wrap around the alphabet, preserve non-letter characters, and reuse the same function inside a loop that can run again and again. The cipher is the project, but the bigger lesson is how functions make logic reusable and easier to control.
