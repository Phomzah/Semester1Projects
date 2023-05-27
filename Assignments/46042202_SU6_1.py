#HA Suliman, 46042202

#Import math module first
import math

#Heading
print("Cuboid Calculator")

print("")

#Base, length and height variables
b = float(input("Enter the base (cm): "))
l = float(input("Enter the length (cm): "))
h = float(input("Enter the height (cm): "))

print("")

#Calculations
area = b*l + l*h + b*h + h*math.sqrt(l**2 + b**2)
diagonal = math.sqrt(l**2 + b**2 + h**2)
volume = (l*b*h)/2

#Output
area= round(area,4)
print("Area of the triangular prism is ", area, " square cm")
print(f"Space diagonal of the triangular prism is {round(diagonal,3)} cm")
print("Volume of the triangular prism is ",(round(volume,2)), " cm")

print("")

#Displaying dimentions
print("**Triangular prism dimensions:**")
print(f"base = {round(b,1)} cm   length = {round(l,1)} cm    height = {round(h,1)} cm")





