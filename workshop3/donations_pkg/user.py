def login(database, username, password):
    if username in database.keys() and password in database.values():
        print("\nWelcome,",  username, "!" )
        return username
    if username in database.keys() and password not in database.values():
        print("\nThe password you entered does not match our database.")
        return ""
    else:
        print("\nUsername does not match our database.")
        return ""

def register(database, username):
    if username in database.keys():
        print("\nUsername already exists.")
        return ""
    else:
        print(username, " has been registered.")
        return username