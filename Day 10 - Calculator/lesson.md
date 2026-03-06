# Day 10 - Functions with Outputs and Reusable Operations

Today we're building a Calculator. It takes two numbers, lets you pick an operation (like `+` or `*`), and gives you the result. Then, it asks if you want to keep calculating with that result or start fresh.

This project introduces two incredibly powerful concepts: **functions returning values** and **treating functions like data**. We also touch on **recursion**, which is when a function calls itself.

## Functions that return things

Up until now, our custom functions mostly just did things (like printing text) and then ended. But a calculator needs to do math and hand the answer back to us.

```python
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2
```

That `return` keyword is the key. It means "when someone calls `add(2, 3)`, replace that function call with the number `5`."

## Storing functions inside dictionaries

Here's the coolest part of `main.py`. Instead of writing a massive if/elif chain to figure out which math operation to run, we store the functions themselves inside a dictionary.

```python
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
```

Notice that we wrote `add` and not `add()`. We aren't _running_ the function here; we are just storing the name of the function as a value. In Python, functions are "first-class objects," which means you can pass them around just like numbers or strings.

When the user types `*`, we can look it up in the dictionary and grab the function:

```python
calculation = operations[operation_symbol]
answer = calculation(num1, num2)
```

If `operation_symbol` was `*`, `calculation` becomes a reference to the `multiply` function. Then we just call it with `calculation(num1, num2)`. This is a super clean way to route user input to different actions.

## Recursion (A function calling itself)

Instead of just exiting the program when the user is done, we want to let them start a brand new calculation. To do this, we wrap the entire calculator logic inside `def calculator():`

```python
def calculator():
    # ... all the calculator logic ...

    if input(f"Type 'y' to continue... or type 'n' to start a new calculation: ") == "y":
        num1 = answer
    else:
        should_continue = False
        calculator()  # <--- Recursion!
```

When the user types 'n', we set `should_continue = False` to break out of the current `while` loop. Then we call `calculator()` from _inside_ `calculator()`. This launches a fresh, clean version of the program.

## Try it yourself

```bash
python "main.py"
```

Try chaining a few calculations together (e.g., 5 + 5 = 10, then \* 2 = 20), and then type 'n' to start over. Notice how the screen clears and the fresh calculator appears instantly.
