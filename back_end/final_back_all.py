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
def start():
    print("Please enter your username:")
    username = input().strip()
    while username not in users:
        print("Please enter a valid username:")
        username = input().strip()
    return username

# initialization of the questionnaire 
def do_quest():
    logged_in = start()
    if logged_in:
        users_answer = run_questionnaire(logged_in)
        print("Thank you for completing the questionnaire! We will notify you when we find your perfect match!")


# small function to calculate intersections after the creation of the sets 
def calculate_intersection(set1, set2):
    return len(set1.intersection(set2))

# matchmaking function between current user and all the other users in the databse 
def matchmaking(logged_in):
    # Get the data from the user that logged in from the dictionary
    current_user_data = users[logged_in]
    list_intersections=[]

    # Loop through each user in the dictionary and compare their answer set with the first user's answer set
    for username, user_data in users.items():
        # Check if the current user is not the first user
        if user_data != current_user_data:
            # Create a set of the first user's answers
            current_user_answers = set(current_user_data['answers'].values())
            # Create a set of the current user's answers
            user_answers = set(user_data['answers'].values())

            # Calculate the intersection between the first user's answers and the current user's answers
            intersection = calculate_intersection(current_user_answers, user_answers)
            list_intersections.append((intersection, username))

            # Print the result of the intersection calculation
            #print(f"Intersection between {username} and the first user: {intersection}")
    return list_intersections

def do_match():
    logged_in = start()
    if logged_in:
        matchmaking(logged_in)
        max_heap(logged_in)
        

# import necessary libraries for the max heap
from heapq_max import heapify_max, heappop_max
import heapq

def display_compatible_users_with_priority(heap, priority):
    compatible_users = []

    for i in range(len(heap)):
        if heap[i][0] == priority:
            compatible_users.append(heap[i])

    return compatible_users

def max_heap(logged_in):
    list_intersections = matchmaking(logged_in)  # Assuming this function returns a list of tuples
    heapq.heapify(list_intersections)  # heapq.heapify creates a min heap

    # Find the highest priority value by iterating through the min heap
    highest_priority = max(heap[0] for heap in list_intersections)
    
    # Get a list of all compatible users who have the same highest priority value
    compatible_users = display_compatible_users_with_priority(list_intersections, highest_priority)

    print("You are compatible with users having the highest priority value: ", compatible_users)


# edit your profile 

def edit_password():
    username = input("Please enter your username: ")
    if username in users:
        new_password = input("Please enter your new password:")
        users[username]["password"] = new_password
        save_users_data(users)
        print("Your password has been changed!")
    else:
        print("Incorrect username! Please retype your username")
        edit_password()
    
def re_do_questionnaire():
    do_quest()

# RUNNING THE PROGRAM:
    
def menu_1():
    print("Welcome to the Roommate Matching Program! Please select one of the following options:")
    print("1. Create an account")
    print("2. Log in")
    
    option = input().strip()
    while option not in ["1", "2"]:
        print("Please enter a valid option:")
        option = input().strip()
    if option == "1":
        create_acc()
        menu_2()
    elif option == "2":
        log_in()
        menu_2()

def menu_2():
    print("1. Edit your password")
    print("2. Do the questionnaire")
    print("3. Re-do the questionnaire")
    print("4. See your matches")
    print("5. Exit the program")
    
    option = input().strip()
    while option not in ["1", "2", "3", "4","5"]:
        print("Please enter a valid option:")
        option = input().strip()
    if option == "1":
        edit_password()
        menu_2()
    elif option == "2":
        do_quest()
        menu_2()
    elif option == "3":
        re_do_questionnaire()
        print("Your answers have been updated! You can check your new matches now!")
        menu_2()
    elif option == "4":
        do_match()
        menu_2()
    elif option == "5":
        print("Thank you for using the Roommate Matching Program! See you soon!")


menu_1()