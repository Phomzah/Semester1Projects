#Phomolo Legobye 41270118
import math

print("Cuboid calculator")

#Entering the base,length,height
base=int(input("Enter the base(cm): "))
length=int(input("Enter the length(cm): "))
height=int(input("Enter the height(cm): "))

#Calculating Area,volume,diagonal
Area = (base*length) + (length*height) + (base*height) + height* (math.sqrt(math.pow(length,2)) +(math.pow(base,2)))
Volume = (length*base*height)/2
Diagonal = 1/2*((math.pow(length,2))+(math.pow(height,2))+(math.pow(base,2)))
print("")
print("Area of the trianglar prism is " ,round (Area,4) ,"square cm")
print("Space diagonal of the triangular prism is ",round (Diagonal,3), "cm")
print("Volume of the triangular prism is",round (Volume,2) ,"cm")

#printing the base,length,height
print("")
print("**Triangluar prism dimensions:**")
print("base",float(round(base,1)), "cm" ,"  length", float(round(length,1)), "cm", "   height", float(round(height,1)),"cm")
