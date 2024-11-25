# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random

def Q2RandomRange():
    print("Enter two numbers to define a range:")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    start, end = (num1, num2) if num1 < num2 else (num2, num1)
    random_number = random.randint(start, end)
    print(f"A random number between {start} and {end} is: {random_number}")