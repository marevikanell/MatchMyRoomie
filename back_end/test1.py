

users = {}

# sign in - create account 
def create_acc():

    username = input("Enter username: ")
    password = input("Enter password: ")

    #check if the account already exists
    if username in users.keys():
        print("Username already exists!")

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

# Existing create_acc() and log_in() functions

def get_user_input(question_data):
    question = question_data["question"]
    question_type = question_data["question_type"]

    print(f"{question}")

    if question_type == "open-ended":
        answer = input().strip()

        # Check if the input is empty and prompt the user to enter a valid input
        while not answer:
            print("Please enter a valid input:")
            answer = input().strip()

    elif question_type == "multiple-choice":
        options = question_data["options"]
        for i, option in enumerate(options):
            print(f"  {i + 1}. {option}")

        # Get user's input and convert it to the corresponding option
        answer_idx = int(input()) - 1

        # Validate the user's input
        while answer_idx < 0 or answer_idx >= len(options):
            print("Please enter a valid option number:")
            answer_idx = int(input()) - 1

        answer = options[answer_idx]

    return answer

# Update the run_questionnaire function to accept a username argument
def run_questionnaire(username):
    questionnaire = [
        {"question": "Name:", "question_type": "open-ended"},
        {"question": "Age:", "question_type": "open-ended"},
        {"question": "Gender:", "question_type": "multiple-choice", "options": ["Male", "Female", "Non-binary", "Other", "Prefer not to say"]},
        # Your questionnaire questions
    ]

    user_answers = {}

    for idx, question_data in enumerate(questionnaire):
        print(f"{idx + 1}. ", end="")
        answer = get_user_input(question_data)
        user_answers[idx + 1] = answer

    # Return a dictionary with the username and their answers
    return {"username": username, "answers": user_answers}

# List to store personalized dictionaries
all_user_answers = []


#############################################

# Example usage

# 1. Create an account
create_acc()

# 2. Log in
log_in()

# 3. Run the questionnaire for the logged-in user
logged_in_username = "example"  # Replace with the actual logged-in username
current_user_answers = run_questionnaire(logged_in_username)

# 4. Add the user's answers to the list of all_user_answers
all_user_answers.append(current_user_answers)

# 5. Display the saved answers for all users
for user_data in all_user_answers:
    username = user_data["username"]
    user_answers = user_data["answers"]
    print(f"{username}'s answers:")
    for question_number, answer in user_answers.items():
        print(f"  {question_number}. {answer}")
    print()  # Add an empty line between users