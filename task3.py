#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

print("Algebra Calculator!\n\nLet's solve for x in ax + b = c\n")


a = float(input("What is the value of a?"))
b = float(input("What is the value of b?"))
c = float(input("What is the value of c?"))

import math 

x = (c-b)/a
print(f"x is equal to {x}")