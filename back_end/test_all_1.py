import pickle

# Load users data from file, or create an empty dictionary if the file does not exist
def load_users_data():
    try:
        with open("users_data.pickle", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

# Save users data to a pickle
def save_users_data(users_data):
    with open("users_data.pickle", "wb") as file:
        pickle.dump(users_data, file)

users = load_users_data()


# create account for the platform function:
def create_acc():
    while True:
        username = input("Enter username: ")
        if username in users.keys(): #if a user alreayd exists with the same name
            print("Username already exists!")
        else:
            password = input("Enter password: ")
            users[username] ={"password": password, "answers": {}}
            save_users_data(users)
            print("Account created successfully! You can now log in to your account.")
            break

# log into account function:
def log_in():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Validate username and password
    if username in users:
        if password == users[username]["password"]:
            print("You have successfully logged in!")
        else:
            print("Incorrect password! Please retype your username & password.")
            log_in() #recursion if the password is incorrect
    else:
        print("Username does not exist!")
        log_in() #recursion if the username does not exist


# function to determine the input and type of the questions 

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

# questionnaire function:
def run_questionnaire(username):
    questionnaire = [
    {"question": "Name:", "question_type": "open-ended"},
    {"question": "Age:", "question_type": "open-ended"},
    {"question": "Gender:", "question_type": "multiple-choice", "options": ["Male", "Female", "Non-binary", "Other", "Prefer not to say"]},
    {"question": "Education level:", "question_type": "multiple-choice", "options": ["High school", "GED", "Some college", "Associate degree", "Bachelor's degree", "Master's degree", "PhD", "Other"]},
    {"question": "Are you a smoker?", "question_type": "multiple-choice", "options": ["Yes", "No"]},
    {"question": "Do you consume alcohol?", "question_type": "multiple-choice", "options": ["Never", "Socially", "Regularly"]},
    {"question": "Do you have any pets? ", "question_type": "multiple-choice", "options": ["Yes", "No"]},
    {"question": "How would you describe your cleanliness habits?", "question_type": "multiple-choice", "options": ["Neat", "Moderate", "Messy"]},
    {"question": "Are you an early bird or a night owl?", "question_type": "multiple-choice", "options": ["Early bird", "Night owl", "Both", "Depends on the day"]},
    {"question": "How often do you have guests or friends over?", "question_type": "multiple-choice", "options": ["Rarely", "Occasionally", "Frequently"]},
    {"question": "Do you prefer a quiet or a lively living environment?", "question_type": "multiple-choice", "options": ["Quiet", "Lively", "Depends on my mood"]},
    {"question": "How important is privacy to you?", "question_type": "multiple-choice", "options": ["Not important", "Little important", "Important", "Very important"]},
    {"question": "What are your hobbies and interests?", "question_type": "multiple-choice", "options": ["Reading", "Watching TV", "Exercise", "Traveling", "Music", "Other"]},
    {"question": "Do you play any musical instruments?", "question_type": "multiple-choice", "options": ["Yes", "No"]},
    {"question": "How do you usually spend your weekends or free time?", "question_type": "multiple-choice", "options": ["Studying", "Chilling with friends", "Going out", "Exercising", "Movie night", "Other"]}, 
    {"question": "What is your preferred move-in date?", "question_type": "multiple-choice", "options": ["June", "August", "September", "January"]},
    {"question": "What is your ideal lease duration?", "question_type": "multiple-choice", "options": ["Month-to-month", "3-6 months", "6-12 months", "12+ months"]},
    {"question": "What is your budget for rent and utilities?", "question_type": "multiple-choice", "options": ["200-500", "500-700", "700-900","900-1200","1200-1500","1500+"]},
    {"question": "What is your preferred location or neighborhood?", "question_type": "multiple-choice", "options": ["Sol", "Chueca", "Malasana", "Salamanca", "La Latina", "Lavapies", "Arguelles", "Chamberi", "Retiro", "Chamartin", "Tetuan"]},
    {"question": "Do you prefer living with people of the same gender or are you open to a mixed-gender living situation?", "question_type": "multiple-choice", "options": ["Same gender", "Mixed gender", "No preference"]},
    {"question": "What type of accommodation are you looking for?", "question_type": "multiple-choice", "options": ["Apartment", "House", "Shared room", "Private room"]},
]


    for idx, question_data in enumerate(questionnaire):
        print(f"{idx + 1}. ", end="")
        answer = get_user_input(question_data)
        users[username]["answers"][idx + 1] = answer

    save_users_data(users)

# initialization of questionnaire based on the username so it saves the answers to the respective person
def start_quest():
    print("Welcome to the questionnaire! Please answer the following questions to help us find your perfect match!")
    print("Please enter your username:")
    username = input().strip()
    while username not in users:
        print("Please enter a valid username:")
        username = input().strip()
    return username

# initialization of the questionnaire 
def do_quest():
    logged_in = start_quest()
    if logged_in:
        users_answer = run_questionnaire(logged_in)
        print("Thank you for completing the questionnaire! We will notify you when we find your perfect match!")


# small function to calculate intersections after the creation of the sets 
def calculate_intersection(set1, set2):
    return len(set1.intersection(set2))

# matchmaking function between current user and all the other users in the databse 
def matchmaking():
    # Get the first user's data from the dictionary
    first_user_data = next(iter(users.values()))
    list_intersections=[]

    # Loop through each user in the dictionary and compare their answer set with the first user's answer set
    for username, user_data in users.items():
        # Check if the current user is not the first user
        if user_data != first_user_data:
            # Create a set of the first user's answers
            first_user_answers = set(first_user_data['answers'].values())
            # Create a set of the current user's answers
            user_answers = set(user_data['answers'].values())

            # Calculate the intersection between the first user's answers and the current user's answers
            intersection = calculate_intersection(first_user_answers, user_answers)
            list_intersections.append((intersection, username))

            # Print the result of the intersection calculation
            #print(f"Intersection between {username} and the first user: {intersection}")
    return list_intersections


# import necessary libraries for the max heap
from heapq_max import heapify_max, heappop_max

def max_heap(): 

    list_intersections = matchmaking()
    # Heapify the intersections_list to create a max heap
    heapify_max(list_intersections)
    print(list_intersections)
    
    # Print the most compatibe user 
    print("The most compatible user is: ", heappop_max(list_intersections))


# RUNNING THE PROGRAM:

# if you do not have an account yet and need to create and do the questionnaire:
def acc_and_test_not_completed():
    create_acc()
    log_in()
    matchmaking()
    max_heap()


# if you have an account but you have not done the questionnaire:
def test_not_completed():
    log_in()
    do_quest()
    matchmaking()
    max_heap()


# if you already have an acc and have done the questionnaire:
def test_completed():
    log_in()
    matchmaking()
    max_heap()

