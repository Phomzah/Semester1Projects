#HA Suliman, 46042202

int = int(input("Enter a positive integer: "))
int -= 1
count = -1

#While loop to display the numbers
while count < int:
    if int > 0:
        count += 1
        print(count, end = " ")

print("")

mysum = -1
total = 0
x = True

#While loop to sum numbers
while mysum < int and x:
    if int > 0:
        mysum += 1
        total += mysum
        print(mysum, end = " ")
        if mysum == int:
            x = False
        else:
            print(end = "+ ")
    
print("=", total)   

print("")

#Addressing the fly-by problem
quit = input("Please press Enter to quit the program")
