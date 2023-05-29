#41270118 Phomolo Legobye

import math

#Asking the user to enter the base and the exponent
base=int(input("Enter the base: "))
exponent=int(input("Enter the exponent: "))

Answer = math.pow(base,exponent)

#checking if base and exponent are equals to zero 
if exponent < 0:
    print("Error â€“ exponent cannot be negative")
elif exponent ==0 and base == 0:
    print("Error â€“ indefinite form (0^0)")
else:
    print(Answer)
