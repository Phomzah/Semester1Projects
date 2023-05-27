P = print

first = float(input("Enter the 1st number: "))
second = float(input("Enter the 2nd number: "))
operator = input("Enter an operator(+, -, *, /): ")
sum = 0

if second == 0 and operator == "/":
    P("Error - division by zero")
elif not operator in ['+', '-', '*', '/']:
    P("Error - invalid operator")
else:
    if operator == "+":
        sum = first + second
        P(sum)
    elif operator == "-":
        sum = first - second
        P(sum)
    elif operator == "*":
        sum = first * second
        P(sum)
    elif operator == "/":
        sum = first / second
        P(sum)
  






