import numpy as np
from bisection import *

def test_bisection():
    # Positive Slope Test
    aval = -1
    bval = 1
    equation = "x"
    assert np.isclose(bisection(aval, bval, equation), 0.0, atol=1e-9)
    # Negative Slope Test
    aval = -1
    bval = 1
    equation = "-x"
    assert np.isclose(bisection(aval, bval, equation), 0.0, atol=1e-9)
    # Let bound is zero test
    aval = 0
    bval = 1
    equation = "x"
    assert np.isclose(bisection(aval, bval, equation), 0.0, atol=1e-9)
    # Right bound is zero test
    aval = -1
    bval = 0
    equation = "x"
    assert np.isclose(bisection(aval, bval, equation), 0.0, atol=1e-9)
    
