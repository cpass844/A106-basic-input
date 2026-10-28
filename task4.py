#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
print("Surface area of a cone calculator\n\nEnter values in M")

import math 
r = float(input("What is the radius?"))
h = float(input("What is the height?"))
l = math.sqrt((h**2)+(r**2))
tsa = (math.pi*r**2+math.pi*r*l)

print(f"The Total Surface area is {tsa}")