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

def run_questionnaire():
    questionnaire = [
        {"question": "Name:", "question_type": "open-ended"},
        {"question": "Age:", "question_type": "open-ended"},
        {"question": "Gender:", "question_type": "multiple-choice", "options": ["Male", "Female", "Non-binary", "Other", "Prefer not to say"]},
        # Add more questions following this format
    ]

    user_answers = {}

    for idx, question_data in enumerate(questionnaire):
        print(f"{idx + 1}. ", end="")
        answer = get_user_input(question_data)
        user_answers[idx + 1] = answer

    return user_answers

# Run the questionnaire and store the user's answers
user_answers = run_questionnaire()

print("Your answers:")
for question_number, answer in user_answers.items():
    print(f"{question_number}. {answer}")








