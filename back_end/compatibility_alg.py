from sets_result import matchmaking
from heapq_max import heapify_max, heappop_max



def max_heap():

    list_intersections = matchmaking()
    # Heapify the intersections_list to create a max heap
    heapify_max(list_intersections)
    print(list_intersections)
    
    # Print the most compatibe user 
    print("The most compatible user is: ", heappop_max(list_intersections))

max_heap()


















##GPT
from heapq import _heapify_max as heapify_max
from heapq import _heappop_max as heappop_max

def max_heap():
    list_intersections = matchmaking()
    # Heapify the intersections_list to create a max heap
    heapify_max(list_intersections)
    print(list_intersections)

    # Find the most compatible users
    most_compatible_users = []
    highest_score = list_intersections[0][0]

    while list_intersections and list_intersections[0][0] == highest_score:
        most_compatible_user = heappop_max(list_intersections)
        most_compatible_users.append(most_compatible_user)

    # Print the most compatible users
    if len(most_compatible_users) == 1:
        print("The most compatible user is:", most_compatible_users[0])
    else:
        print("The most compatible users are:")
        for user in most_compatible_users:
            print(user)

max_heap()
##GPT