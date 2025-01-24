# Simple User Tutorial
from bisection import *

# Set left bound as a and right as b
aval = -1
bval = 2

# Declare the equation to be solved, for this example just y = x
equation = "-x+1"

# Call the bisection function
cval = bisection(aval, bval, equation)

# Print the solution, which as expected should be 0
print("The solution within these bounds is: ")
print(cval)
