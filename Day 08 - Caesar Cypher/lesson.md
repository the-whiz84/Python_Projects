# Day 08 - Functions with Parameters and Caesar Cipher Logic

Today we're building a Caesar Cipher — an encryption program that shifts every letter in a message by a certain number of places down the alphabet.

Up until now, you've used built-in functions like `print()` and `len()`. But today, you get to build your own custom function. We're going to wrap the entire encryption and decryption logic inside a single, reusable block of code called `caesar()`.

## Passing data into functions

Here's the core function we use in `main.py`:

```python
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        # ... shifting logic ...
```

Notice the variables inside the parentheses: `original_text`, `shift_amount`, and `encode_or_decode`. These are **parameters**. They act like variables that are only available _inside_ the function.

When the user types their inputs, we pass those inputs into the function:

```python
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
```

By explicitly saying `original_text=text`, we are using **keyword arguments**. It tells Python exactly which parameter gets which piece of data. This is much safer than just passing `text, shift, direction` and hoping you got the order right.

## The shifting logic and the modulo operator

The tricky part of a Caesar Cipher is what happens when you reach the end of the alphabet. If you shift 'z' by 1, you need to loop back around to 'a'.

```python
shifted_position = alphabet.index(letter) + shift_amount
shifted_position %= len(alphabet)
output_text += alphabet[shifted_position]
```

This is where the modulo operator (`%`) comes in. `len(alphabet)` is 26.
If `shifted_position` becomes 26 (which is past the end of our list indices 0-25), `26 % 26` equals `0`, which loops perfectly back to 'a'. If the shift is huge, like 100, `100 % 26` is `22`, which drops us exactly at 'w'.

This little math trick saves us from having to write a messy `if shifted_position > 25:` check, and it safely handles massive shift numbers that the user might type to try and break the program.

## Keeping non-letters intact

What if the user types a space, a number, or a question mark?

```python
if letter not in alphabet:
    output_text += letter
```

We just add it to the output string as-is. Our function only shifts characters that actually exist in the `alphabet` list.

## Try it yourself

```bash
python "main.py"
```

Try encrypting a message with a normal shift like `5`. Then, take the garbled output, run the program again, choose `decode`, and pass in the same shift number. The math flips (`shift_amount *= -1`) and gives you back your original text!
