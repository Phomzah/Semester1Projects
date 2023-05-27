#HA Suliman, 46042202

#Importing math module
import math

#Heading1
print("Solving ax^2 + bx + c =0")

#Variables for a,b and c
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

print("")

#Heading2
print("ROOTS OF GIVEN QUADRATIC EQUATIONS ARE:")

#Calculations
x1 = (-1*b + math.sqrt(b**2 - 4*a*c))/2*a
x2 = (-1*b - math.sqrt(b**2 - 4*a*c))/2*a

#Output answer
print(f"x1: {x1}")
print(f"x2: {x2}")





