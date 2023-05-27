#HA Suliman, 46042202

q = True

while q:
    choice = input("""a) Find the next leap year
b) Login system
Choose a or b: """)
    if choice == "a":
        #Leap year project 

        year = int(input("Enter the year you are in: "))

        print("")

        #When it is a leap year then %4 = 0 :

        l = year % 4

        if l == 0:
            print(f"{year} is a leap year!")
        else:
            for x in range(4):         
                l = year % 4
                if l == 0:
                    print(f"{year} is the next leap year!")
                year += 1
    elif choice == "b":
        username1 = input("Enter your username: ")
        password1 = input("Enter your password: ")

        print("")

        print("####################")
        print("       Login")
        print("####################")

        print()

        username2 = input("Username: ")
        password2 = input("Password: ")

        if username2 != username1:
            print("Incorrect Usernme!")
        elif password2 != password1:
            print("Incorrect Password!")
        else:
            print(f"Welcome {username2}")

    quit = input("Enter q to quit: ")

    if quit == "q":
        q = False



