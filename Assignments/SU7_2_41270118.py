#41270118 Phomolo Legobye


#Asking the user to enter two numbers and an operator
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
operator=input("Enter an operator: ")

if operator == "+" or operator == "-" or operator == "*" or operator == "/":
    print("")
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/" and num1 != 0 and num2 != 0:
        print(num1 / num2)
    else:
        print("Error â€“ division by zero")
else:
    print("Error â€“ invalid operator")



