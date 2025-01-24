from bisection import *

# This tutorial is adapted from a fluid mechanics problem (see Readme file)

# Bounds
aval = 0.0
bval = 5.0

# Equation to be solved using the bisection method
equation = "1.94*1.4*(math.pi/4)*x**2*30*30*math.cos(math.pi/6)*1-6650"

# Call the bisection method
cval = bisection(aval, bval, equation)

# Print the solution
print("The solution within these bounds is: ")
print(cval)