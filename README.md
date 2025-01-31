# ME 700 Assignment 1
This assignment serves as an introduction to Python, Github, and good coding practices for mechanical computation.  This assignment is split into 3 parts: a warmup interacting with the bisection method, a first part that works with Newton's Method, and a second part incorporating an elastoplastic material model.

## Setup
To install this package, begin by activating miniconda

```bash
module load miniconda
```

Then, set up a mamba environment
```bash
mamba create --name bisection-env python=3.12
```

And then activate said environment:
```bash
mamba activate bisection-env
```

Double-check that the correct version of Python is installed
```bash
python --version
```

Ensure that pip is using the most up-to-date version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```

Then, navigate to the correct directory (warmup, Part 1, Part 2)

## Using warmup tutorials
To load each tutorial, type:
```bash
python #(Name of Tutorial)
```
Fill in the name of tutorial with one of the five, either Tutorial1.py or Tutorial2.py for simple examples of the bisection method, Tutorial3.py for an example where you can input different values for the bisection to occur, and Tutorial_Mech1.py or Tutorial_Mech2.py for examples derived from mechanics problems.

## Warmup Mechanics Tutorial 1
The problem shown in the first mechanics tutorial is taken from ME 700 Lecture 1.  The problem involves a mass supported by two horizontal springs, with a load being applied to the mass orthogonal to the orientation of the springs.  A schematic of the figure as shown in the class notes is shown below:

![Problem 1 Figure](https://github.com/user-attachments/assets/2e835ce1-83ca-4815-b219-d9f37304a917)

As we showed in class, the problem reduces to the equation shown below.  The equation is solved for values of l = 1 m, k = 1 N/m, and F = 0.25 N.  The value for w, the deflection in the vertical direction, is solved for using the bisection method and the values listed.

![Problem 1 Equation](https://github.com/user-attachments/assets/edd7a2a1-2f87-4d9b-a24a-17399df4e328)

## Warmup Mechanics Tutorial 2
The problem shown in the second tutorial for the assignment warmup is adapted from problem 5.51 in Fundamentals of Fluid Dynamics by Munson, Young, & Okisshi 8th Edition.  The version used for the tutorial is as follows:

The hydraulic dredge in the figure below is used to dredge sand from the river bottom.  Estimate the propeller's diameter that holds the boat stationary with a thrust of 6650 lbf, assuming the specific gravity of the sand-water mixture to be 1.2.

![Problem Figure](https://github.com/user-attachments/assets/e9e1ab7c-9ea2-4c5d-93c7-72831561b89e)

The equation that is solved for in this example is the following:

![Problem Equation](https://github.com/user-attachments/assets/2df42bea-024b-4939-a4a9-dad2f1a3368e)

## Generative AI Use

In this assignment, the only forms of Generative AI that were used were vsCode Copilot, which assisted in completing code and ensuring correct Python syntax, and Google Gemini, which was a result when looking up specific Python functions and library implementation.

## Contributing
Pull Requests are welcome

## License
[MIT](https://choosealicense.com/licenses/mit/)
