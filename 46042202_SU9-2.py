#HA Suliman, 46042202

#Heading
print("Enter a number and you will be provided with a multiplication table from 1 to 12 of your number!")

print("")

#Asking the question until the conditions are met
t = True

while t:
    val = int(input("Enter a number: "))

    if val > 1:
        t = False
    else:
        print("Value must be greater than 1!")

print("")

#Formatting the table and printing the totals:
sum1 = 0
sum2 = 0

for x in range(1, 13):
    sum1 = x * val
    print(f"{x} x {val} = {sum1}")
    sum2 += sum1

print("")

print(f"Total = {sum2}")
        
