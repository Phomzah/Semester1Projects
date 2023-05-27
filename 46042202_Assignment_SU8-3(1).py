#HA Suliman, 46042202

import math as m

name = input("Enter your name: ")

print(f"Hello {name}!")

#Circle
print("")
circle = int(input("Enter the radius of your circle in cm: "))

#Triangle
print("")
Tri1 = int(input("Enter the 1st side of your triangle in cm: "))
Tri2 = int(input("Enter the 2nd side of your triangle in cm: "))
Tri3 = int(input("Enter the 3rd side of your triangle in cm: "))

#Square
print("")
square = int(input("Enter the length of the side of your square in cm: "))

#Rectangle
print("")
rectL = int(input("Enter the the length of your rectangle in cm: "))
rectW = int(input("Enter the width of your rectangle in cm: "))

#Perimeters
pcircle = round(float(2*m.pi*circle),2) 
ptri = round(float(Tri1 + Tri2 + Tri3))
psquare = round(float(4*square)) 
prect = round(float(2*(rectL + rectW))) 

print("")

print("%1s%15s%25s" % ("Shape", "Value(s)", "Perimeter"))

for x in range(4):
    if x == 0:
        print("Circle %11s%25s" % (f"r= {circle}cm", f"{str(pcircle)}cm"))
    if x == 1:
        print("Triangle %23s%9s" % (f"a= {Tri1}cm b= {Tri2}cm c= {Tri3}cm", f"{str(ptri)}cm"))
    if x == 2:
        print("Square %11s%23s" % (f"s= {square}cm", f"{str(psquare)}cm"))
    if x == 3:
        print("Rectangle %15s%16s" % (f"I= {rectL}cm W= {rectW}cm", f"{str(prect)}cm"))
    
     



    
