# sign up and log in simulation console app.
# sign up: Writes datas to the text file as -> username hashed_password
# log in:  Reads datas from the text file. If there is a match both username and hashed_password, you will logged in successfully.

#  https://github.com/emretekin8/Signup---Login-System

import hashlib

# hashing password
def hash(password):
    plaintext = password.encode()
    d = hashlib.sha256(plaintext)

    hash = d.hexdigest()
    return hash
    

# controls for unique username
def getUsername():
    f = 'database.txt'
    with open(f) as f_obj:
        db = f_obj.read()

    username = input("Username:")
    while username in db:
        print("This username is already taken!")
        username = input("Username:")

    return username


# sign up
def signup():
    f = open("database.txt", "a")

    username = getUsername()
    password = input("Password:")
    

    f.write(username + " " + str(hash(password)) + "\n")
    f.close()
    print("Signed up!")

    f = open("database.txt", "r")
    print(f.read())


# log in
def login():  

    logged = False

    f = 'database.txt'

    with open(f) as f_obj:
        db = f_obj.read()

    username = input("Username:")

    while logged == False:

        if username in db:
            password = input("Password:")
            if username + " " + hash(password) in db:
                print("Logged in!")
                logged = True
            else:
                print("Wrong password!")
                break
        
        else:
            print( "User not found: " + username)
            username = input("Username:")



def main():
    print("-------------Welcome-------------")

    while True:
        print("\n")
        print("a. Sign up")
        print("b. Log in")
        print('c. Exit')
        key = input() # log in or sign up

        if key == "a":
            signup()
        elif key == "b":
            login()
        elif key == "c":
            break
        else:
            print("Press a,b or c")
            key = input()

  

main()