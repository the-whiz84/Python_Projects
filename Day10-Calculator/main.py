#Calculator
from art import logo
#Add
def add(n1, n2):
    return n1 + n2
#Substract
def substract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

#Dictionary with the operations
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What is the first number? "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Choose the operation: ")

        num2 = float(input("What's the next number? "))

        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

#If instead of exiting we want to user to start a new calculation we can use Recursion by enclosing everything in a function and calling it at the end to go back from the Start
calculator()

    



