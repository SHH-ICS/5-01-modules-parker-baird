# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random

print("Enter two numbers to define a range:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

random_number = random.randint(num1, num2)
print(f"A random number between {num1} and {num2} is: {random_number}")