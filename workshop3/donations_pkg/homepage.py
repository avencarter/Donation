def show_homepage():
    print("      ===  DonateMe Homepage  ===      ")
    print("---------------------------------------")
    print("|1.  Login      |2.  Register         |")
    print("---------------------------------------")
    print("|3.  Donate     |4.  Show Donations   |")
    print("---------------------------------------")
    print("|             5.  Exit                |")
    print("---------------------------------------")

def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_string = "{} donated $1000.0".format(username)
    print("Thank you for the donation!")
    return donation_string

def show_donations(donations):
    print("\n--- All Donations ---")

    if donations == []:
        print("Currently there are no donations.")
    else:
        for x in donations:
            print(x)
