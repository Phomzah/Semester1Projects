
email = input("Enter your email: ")

c = 0
for x in email:
    c += 1
    if x == "@":
        sign = c
        print(f"Name = {email[:sign-1]}")
        print(f"Domain = {email[sign:]}")







