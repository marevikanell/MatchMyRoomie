from introduction_to_plat import users

# Define a function to calculate the intersection between two sets
def calculate_intersection(set1, set2):
    return len(set1.intersection(set2))

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

         


if __name__=='__main__':
    matchmaking()
    


