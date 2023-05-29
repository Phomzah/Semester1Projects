#41270118 Phomolo Legobye

import math

#Asking the user to enter value a,b,c
print("Solving ax^2 + bx + c =0")
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))

#Calculating x1 and x2
x1 = (-b + (math.sqrt(math.pow(b,2) - (4*a*c))))/2*a
x2 = (-b - (math.sqrt(math.pow(b,2) - (4*a*c))))/2*a

#Printing x1 and x2      
print("ROOTS OF GIVEN QUADRATIC EQUATIONS ARE:")
print("x1: " , x1)
print("x2: " , x2)


    
