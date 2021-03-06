import os
from calculator_art import logo
clear = lambda: os.system('cls')
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What is the first number?: "))


    for symbol in operations:
        print(symbol)
    '''
    if operation_symbol == "+":
        answer = add(num1, num2)
    elif operation_symbol == "-":
        answer = subtract(num1, num2)
    elif operation_symbol == "*":
        answer = multiply(num1, num2)
    elif operation_symbol == "/":
        answer = divide(num1, num2)
    else:
        print("invalid option")
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    '''
    while should_continue:
      operation_symbol = input("what is the next operation?: ")
      num2 = float(input("What is the next number?: "))
      calculation_function = operations[operation_symbol]
      answer = calculation_function(num1 , num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")

      if input(f"type y to continue calculatiing with {answer} or type n to start a new calculation: ") == "y":
            num1 = answer
      else:
            should_continue = False
            clear()
            calculator()
        
calculator()