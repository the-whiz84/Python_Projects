# Day 10 - Functions with Outputs and Reusable Operations

Today we're building a calculator that can keep working with the previous result or restart from scratch. The project is useful because it turns functions into reusable tools instead of one-off code blocks. It also shows a cleaner way to route user input to behavior by storing function references in a dictionary.

## 1. Returning Values from Functions

The basic arithmetic operations are defined as separate functions:

```python
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2
```

The important change here is `return`. Earlier projects often printed a result directly. In this calculator, the program needs to get the computed value back so it can reuse it later in the workflow.

That is what return values are for: they let one part of the program hand a result to another part without printing and stopping there.

## 2. Treating Functions as Dictionary Values

The strongest design choice in the project is the `operations` dictionary:

```python
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
```

Notice that the dictionary stores function names without parentheses. That means the functions are being stored as values, not executed immediately.

Later, the program looks up the user's chosen symbol:

```python
calculation = operations[operation_symbol]
answer = calculation(num1, num2)
```

This is a clean alternative to a long `if` / `elif` chain. The symbol selects the correct function, and the program calls that function only after it has been retrieved from the dictionary.

## 3. Reusing the Previous Answer in a Loop

The calculator keeps running inside a `while` loop:

```python
should_continue = True
while should_continue:
    operation_symbol = input("Choose the operation: ")
    num2 = float(input("What's the next number? "))

    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)
```

This loop is what makes the calculator feel interactive instead of one-and-done. After each result, the user can keep calculating with `answer` as the new first number.

That is a practical state-management step. The program is not just doing math. It is deciding whether to preserve the current calculation chain or reset it.

## 4. Restarting with Recursion

When the user chooses to start over, the function calls itself:

```python
if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
    num1 = answer
else:
    should_continue = False
    calculator()
```

This is recursion: a function calling itself. In this project, recursion is used to restart the calculator with a fresh state after the current loop ends.

It is not the only way to structure the reset, but it clearly demonstrates that a function can launch a new copy of the same workflow.

## How to Run the Project

1. Open a terminal in this folder.
2. Run:

```bash
python main.py
```

3. Choose an operation, enter numbers, and confirm that the result prints correctly.
4. Type `y` to keep calculating with the current answer, then type `n` to restart the calculator from the beginning.

## Summary

Day 10 shows how functions become more useful once they return values instead of only printing them. The calculator stores function references in a dictionary, selects the right operation from user input, and keeps state through a calculation loop. It is also a first look at recursion through a simple restart pattern.
