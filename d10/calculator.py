

def main(num1, num2, operator_symbol):
    


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
    "+":"add",
    "-":"subtract",
    "*":"multiply",
    "/":"divide"
}

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

for key in operations:
    print(key)

operation_symbol = input("Pick an operation symbol form the list above.: ")



print(f"{num1} {operation_symbol} {num2} = {answer})

