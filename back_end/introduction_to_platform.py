

# Load users data from file or create an empty dictionary if the file does not exist
def load_users_data():
    try:
        with open("users_data.txt", "r") as file:
            users_data = {}
            for line in file:
                username, password = line.strip().split(":")
                users_data[username] = password
            return users_data
    except FileNotFoundError:
        return {}

# Save users data to a file
def save_users_data(users_data):
    with open("users_data.txt", "w") as file:
        for username, password in users_data.items():
            file.write(f"{username}:{password}\n")

users = load_users_data()

def create_acc():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if the account already exists
    if username in users.keys():
        print("Username already exists!")
    else:
        users[username] = password  # add username and password to dictionary
        save_users_data(users)  # save updated users data to a file
        print("Account created successfully!")
        print("You can now log in to your account.")


create_acc()