#41270118 Phomolo Legobye

#Asking the user to enter the age and gender
age=int(input("Enter the age: "))
gender=input("Enter the gender: ")

#checking if age is above 18 and gender is M or W
if age >= 18 and gender == "M" or gender == "F":
    print("You are eligible to vote")
elif age < 18:
    print("You are not eligible to vote")
elif gender != "M" or gender != "F":
    print("Invalid gender")

