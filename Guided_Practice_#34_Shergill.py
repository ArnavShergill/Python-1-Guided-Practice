from formatting import *

print("\n---- Guided Practice #34 ----\n")

section("Importing Modules")
subsection("Importing the Whole Library")

#Import the whole math library
import math

#compute 2 to the power 3
print(math.pow(2, 3))

#Compute 5 to the power 2
print(math.pow(5, 2))

short_dash()
subsection("Importing the Whole Library and Renaming It")

import math as ml

#compute 2 to the power 3
print(ml.pow(2, 3))

#Compute 5 to the power 2
print(ml.pow(5, 2))

short_dash()
subsection("Importing only the pow function")

#import the pow function
from math import pow

#compute 2 to the power 3
print(pow(2, 3))

#Compute 5 to the power 2
print(pow(5, 2))

short_dash()
subsection("Importing the Fabs Function")

import math
x=-5
print(math.fabs(x))

import math as ml
y=12
print(ml.fabs(y))

from math import fabs
print(fabs(-5))

dash()
section("Using Math Functions")
subsection("Square Root")

from math import sqrt

#Compute the square root of 5
print(sqrt(5))

#Compute the square root of 30
print(sqrt(30))

short_dash()
subsection("Other Arithmetic Operators")

print("- Division -\n")
In = 5//2
Out = 2.5

print(In)
print(Out)

short_dash()
print("- Modulo Operator -\n")

In = 5%2
Out = 1

print(In)
print(Out)

short_dash()
print("- Exponent Operator -\n")

In = 2**3
Out = 8

print(In)
print(Out)
print()

In = 5**2
Out = 25

print(In)
print(Out)

dash()
section("More Math Functions")

import math

#calculate the sine of 30 degrees (in radians)
sin_30 = math.sin(math.radians(30))
print(sin_30) #Output: 0.5

#calculate the cosine of 45 degrees (in radians)
cos_45 = math.cos(math.radians(45))
print(cos_45) #Output: 0.7071067811865476

#calculate the tangent of 60 degrees (in radians)
tan_60 = math.tan(math.radians(60))
print(tan_60) #Output: 1.7320508075688767

dash()
