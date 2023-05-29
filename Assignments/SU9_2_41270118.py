#41270118 Phomolo Legobye


# This program asks the user to enter an integer value,
# displays the multiplication table based on the user's input,
# and calculates the sum of the totals from the multiplication table and dislpays the sum.

# Input verification using a while loop
Input = True
while Input:
    value = int(input("Enter an integer value : "))
    if value > 1:
        Input = False
    else:
        print("Error input.Try again")

for i in range(1, 13):
    result = value * i
    print(f"{value} x {i} = {result}")

# Calculating the sum of the totals and displaying the sum
sum = sum(range(value, (value * 13) + 1, value))
print("\nThe sum is:", sum)
