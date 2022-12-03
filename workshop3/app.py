from donations_pkg import homepage, user


database = {"admin": "password123"}

donations = []

authorized_user = ""

homepage.show_homepage()

while True:

    option = input("\nChoose Option: ")


    if option == "1":
        username = input("\nUsername: ")
        password = input("\nPassword: ")
        authorized_user = user.login(database,username,password)
    elif option == "2":
        username = input("Username: ")
        password = input("\nPassword: ")
        authorized_user = user.register(database,username)
        if authorized_user != "":
            database[username] = password
    elif option == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = homepage.donate(authorized_user)
            donations.append(donation_string)
    elif option == "4":
        homepage.show_donations(donations)
    elif option == "5":
        print("Goodbye")
        exit()
    else:
        print("Invalid Option. Please choose 1-5.")

    if authorized_user == "":
        print("\nYou must be logged in to donate")
    else:
        print("\nLogged in as: ", username)