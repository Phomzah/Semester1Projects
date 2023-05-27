#Ha suliman, 46042202

int = int(input("Enter a positive integer: "))

#For loop to display the numbers backwards
for x in range(int - 1, 0 - 1, -1):
    print(x, end = " ")

print("")

#Addressing the fly-by problem
quit = input("Please press enter to quit the program")
