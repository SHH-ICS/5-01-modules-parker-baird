# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math

a = float(input("Enter the length of the first leg (a): "))
b = float(input("Enter the length of the second leg (b): "))
c = (a**2 + b**2)

print(f"The length of the hypotenuse (c) is: {c:.2f}")
