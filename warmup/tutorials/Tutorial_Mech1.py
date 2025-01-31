# This tutorial solves an equation for deflection of a mass attached to two springs for a problem set up in Lecture 1 of ENG ME 700 (Spring 2025) at Boston University
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from warmup.src.bisection import bisection

# Bounds
aval = 0.0
bval = 2.0

# Equation to be solved using the bisection method
import math
import os

equation= "2 * (math.sqrt(1 + x**2) - 1) * (x / math.sqrt(1 + x**2)) - 0.25"

# Call the bisection method
cval = bisection(aval, bval, equation)

# Print the solution
print("The solution within these bounds is: ")
print(cval)
