# This tutorial allows the user to input their own bounds and equation in the terminal
from bisection import *

# Set left bound as a and right as b
aval = float(input("Enter the left bound: "))
bval = float(input("Enter the right bound: "))

# Declare the equation to be solved, for this example just y = x
equation = input("Enter the equation to be solved in proper Python syntax: ")

# Call the bisection function
cval = bisection(aval, bval, equation)

# Print the solution, which as expected should be 0
print("The solution within these bounds is: ")
print(cval)