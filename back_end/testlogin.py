# create empty dictionary
users = {}

# sign in - create account 
def create_acc():
    username = input("Enter username: ")
    password = input("Enter password: ")
     # check if the account already exists
    while True:
        if username in users: 
            print("Username already exists!")
            break
        else:
            users[username] = password # add username and password to dictionary    
            print("Account created successfully!")
            print("You can now log in to your account.")
   
    

# log in - existing account
def log_in():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users:
        if users[username] == password:
            print("You have successfully logged in!")
        else:
            print("Incorrect password!")
    else:
        print("Username does not exist!")


create_acc()