import pickle

def reset_pickle_file(filename):
    with open(filename, "wb") as file:
        pickle.dump({}, file)

# Usage:
reset_pickle_file("users_data.pickle")
