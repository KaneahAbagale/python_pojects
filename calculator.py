#Calculator

# Create the various functions
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divid
def divide(n1, n2):
    return n1 / n2

# Create a dictionary that saves has the Key as the symbol of the operation and the value as the name of the functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Inputs to collect numbers from users and which operations they want
num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for symbol in operations:
    print(symbol)   
operation_symbol = input("Pick a symbol from the line above: ")

# Input symbol saved an used as a key in the dictionary
# for symbol in operations:

calculation_function = operations[operation_symbol]               
answer = calculation_function(num1, num2) 

print(f"{num1} {operation_symbol} {num2} = {answer}")