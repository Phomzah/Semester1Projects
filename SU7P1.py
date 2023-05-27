P = print

age = int(input("Enter your age: "))
gender = input("What is your gender(M / F): ")

if age >= 18 and gender in ['M', 'F']:
    print("You are eligible to vote")
elif age < 18:
    print("You are not eligible to vote. You must be 18 or above.")
else:
    print("Invalid gender. Please enter 'M' for male or 'F' for female.")
    


