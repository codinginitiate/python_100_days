import os
os.system("clear")
from art import logo
print(logo)

# Calculator
#add
def add(n1, n2):
    return n1 + n2
#subtract
def subtract(n1, n2):
    return n1-n2
#multiply
def multiply(n1, n2):
    return n1 * n2
#divide
def divide(n1, n2):
    return n1 / n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    while True:
        try:
            num1 = int(input("What is the first number?: "))
            break
        except ValueError:
            continue

    for key in operations:
        print(key+" ", end ="")

    should_continue = True

    while should_continue:

        while True:
            try:
                operation_symbol = input("Pick an operation symbol form the list above.: ")
                if operation_symbol in operations:
                    break
            except ValueError:
                continue

        while True:
            try:
                num2 = int(input("What is the next number?: "))
                break
            except ValueError:
                continue

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}\n")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        elif
            should_continue = False
            calculator()

calculator()
