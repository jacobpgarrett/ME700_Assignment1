# Libraries Included
import math

# Function to solve the equation
def eqsolve(x, equation):
    y = eval(equation)
    return y

# Bisection Method
def bisection(aval, bval, equation):
    # Define the tolerance and set an arbitrary value for c
    tol = 10e-9
    c = 10*tol

    # Error Checking

    if aval > bval:
        raise SyntaxError("The lower bound must be less than the upper bound")
    if eqsolve(aval, equation) > 0 and eqsolve(bval, equation) > 0:
        raise SyntaxError("Bisection Method cannot compute solution within these bounds")
    if eqsolve(aval, equation) < 0 and eqsolve(bval, equation) < 0:
        raise SyntaxError("Bisection Method cannot compute solution within these bounds")
    
    # What to do if one of the bounds is a solution
    if eqsolve(aval, equation) == 0:
        return aval
    if eqsolve(bval, equation) == 0:
        return bval

    # Determine how the function crosses the x axis
    if (eqsolve(aval, equation) > 0) and (eqsolve(bval, equation) < 0):
        slope = -1
    if (eqsolve(aval, equation) < 0) and (eqsolve(bval, equation) > 0):
        slope = 1

    # Bisection Method
    if slope == 1:
        while abs(c) > tol:
            a = eqsolve(aval, equation)
            b = eqsolve(bval, equation)
            cval = (aval+bval)/2
            c = eqsolve(cval, equation)
            if c <= 0:
                aval = cval
            else:
                bval = cval
    else:
        while abs(c) > tol:
            a = eqsolve(aval, equation)
            b = eqsolve(bval, equation)
            cval = (aval+bval)/2
            c = eqsolve(cval, equation)
            if c >= 0:
                aval = cval
            else:
                bval = cval
    
    # Return Solution to Equation        
    return cval

