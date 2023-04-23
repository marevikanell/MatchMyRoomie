from introduction_to_plat import save_users_data, users

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


def start_quest():
    username = input("Enter username: ")
    # Validate username and password
    if username in users:
        if username in users.keys():
            return username
        else:
            print("Username does not exist!")
            start_quest()


logged_in_user = start_quest()

if logged_in_user:
    user_answers = run_questionnaire(logged_in_user)
    print("Thank you for completing the questionnaire!")