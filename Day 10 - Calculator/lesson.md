# Day 10 - Functions with Outputs and Reusable Operations
Day 10 teaches how to model operations as functions and dynamically call them through a mapping.

## Goal

Build a calculator that supports chained operations (`+`, `-`, `*`, `/`) and can restart for new sessions.

## Day-Specific Logic

`main.py` uses a function dictionary pattern:
- math functions (`add`, `substract`, `multiply`, `divide`)
- `operations` dict mapping symbols to functions
- dynamic execution via `calculation = operations[operation_symbol]`

It also uses recursion (`calculator()`) to restart the program after the user exits the current calculation chain.

## Code Reference

From `main.py`:

```python
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

calculation = operations[operation_symbol]
answer = calculation(num1, num2)

if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
    num1 = answer
else:
    should_continue = False
    calculator()
```

## Run

```bash
python "main.py"
```
