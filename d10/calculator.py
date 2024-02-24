import os
os.system("clear")
from art import logo
print(logo)

def main(num1, num2, operator_symbol):
    return operations[operator_symbol](num1, num2)

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

while True:
    try:
        num1 = int(input("What is the first number?: "))
        break
    except ValueError:
        continue


        for key in operations:
            print(key+" ", end ="")

        operation_symbol = input("\nPick an operation symbol form the list above.: ")
        if operation_symbol in operations[key]:
            break

    except ValueError

while True:
    try:
        num2 = int(input("What is the next number?: "))
        break
    except ValueError:
        continue

answer = main(num1, num2, operation_symbol)
print(f"{num1} {operation_symbol} {num2} = {answer}\n")
while True:
    if input(f"Type 'y' to continue calculating with {answer}: ") == 'y':
        pass
    else:
        break
    num1 = answer
    operation_symbol = input("\nPick an operation symbol form the list above.: ")
    print(num1)

    while True:
        try:
            num2 = int(input("What is the next number?: "))
            break
        except ValueError:
            continue
    print(num1, num2, operation_symbol)
    answer = main(num1, num2, operation_symbol)
    print(f"{num1} {operation_symbol} {num2} = {answer}\n")



if __name__=="__main__":
    main(num1, num2, operation_symbol)







