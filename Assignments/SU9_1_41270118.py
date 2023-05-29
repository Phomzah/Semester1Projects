#41270118 Phomolo Legobye

# This program takes two variables as input, performs some processing using if statement and loop,
# and displays the output neatly.

# Input
variable1 = int(input("Enter the first variable: "))
variable2 = int(input("Enter the second variable: "))

# Processing
if variable1 > variable2:
    for i in range(variable2, variable1 + 1):
        print(i,end=" ")
else:
    while variable1 <= variable2:
        print(variable1)
        variable1 += 1

# Output
print("Processing complete!")
