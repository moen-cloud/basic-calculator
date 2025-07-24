# Simple Calculator Program

# Ask the user to input the first number
num1 = float(input("Enter the first number: "))

# Ask the user to input the second number
num2 = float(input("Enter the second number: "))

operation = input("Enter an operation (+, -): ")

# Perform the operation

if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")


elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

else:
    print("Invalid operation. Please enter one of +, -")
    