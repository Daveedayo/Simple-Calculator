import sys

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

print("Please select an operation: \n"
    "1. Addition\n"
    "2. Subtraction\n"
    "3. Multiplication\n"
    "4. Division\n"
)
try:
    selection = int(input("Choose an operation form (1 / 2 / 3 / 4): "))
except:
    print("Invalid input format")
    sys.exit()

try:
    number_1 = int(input("Enter first number(s): "))
    number_2 = int(input("Enter second number(s): "))
except:
    print("Invalid input format")
    sys.exit()

if selection == 1:
    print(f"{number_1} + {number_2} = {add(number_1, number_2)}")
elif selection == 2:
    print(f"{number_1} - {number_2} = {subtract(number_1, number_2)}")
elif selection == 3:
    print(f"{number_1} * {number_2} = {multiply(number_1, number_2)}")
elif selection == 4:
    print(f"{number_1} / {number_2} = {divide(number_1, number_2)}")
else:
    print("Invalid operator option!")
    sys.exit()