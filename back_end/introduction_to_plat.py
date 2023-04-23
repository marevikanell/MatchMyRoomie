import pickle

# Load users data from file, or create an empty dictionary if the file does not exist
def load_users_data():
    try:
        with open("users_data.pickle", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

# Save users data to a file
def save_users_data(users_data):
    with open("users_data.pickle", "wb") as file:
        pickle.dump(users_data, file)

users = load_users_data()

def create_acc():
    while True:
        username = input("Enter username: ")
        if username in users.keys():
            print("Username already exists!")
        else:
            password = input("Enter password: ")
            users[username] ={"password": password, "answers": {}}
            save_users_data(users)
            print("Account created successfully!")
            print("You can now log in to your account.")
            break

def log_in():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Validate username and password
    if username in users:
        if password == users[username]["password"]:
            print("You have successfully logged in!")
        else:
            print("Incorrect password! Please retype your username & password.")
            log_in()
    else:
        print("Username does not exist!")
        log_in()


print(users)


