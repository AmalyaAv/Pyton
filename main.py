access = False
while not access:
    username = input("Enter your username")
    password = input("Enter your password")
    if username == "Amaliya" and password == "12345":
        print("Access granted")
        access = True
    elif username == "Amaliya":
        print("Access denied, Wrong password")
    else:
        print("Access denied, Wrong username")
print("End of program")
