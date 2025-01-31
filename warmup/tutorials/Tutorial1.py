# Simple User Tutorial
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from warmup.src.bisection import bisection

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
