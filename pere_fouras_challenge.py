import json
from random import randint


def load_riddles(file):
    """
    Load riddles from a JSON file.

    Args:
        file (str): The path to the JSON file containing riddles.

    Returns:
        list: A list of riddles as dictionaries with 'question' and 'answer' keys.
    """
    with open(file, 'r') as f:
        riddles = json.load(f)
    return riddles


def pere_fouras_riddles():
    """
    Simulates a riddle game where the player must guess the answer.

    The game randomly selects a riddle from a JSON file and allows the player
    three attempts to guess the correct answer. Feedback is given based on
    the player's input and remaining attempts.

    Returns:
        bool: True if the player guesses the correct answer, False otherwise.
    """
    riddles_storage = load_riddles('Data/PFRiddles.json')  # Fetch riddles from the storage
    riddles_dictionnary = {}
    nb_of_atttemps = 3  # Maximum number of attempts allowed
    selected_riddle = randint(0, len(riddles_storage) - 1)  # Randomly select a riddle

    # Display the selected riddle's question
    print(f"Here is the riddle: {riddles_storage[selected_riddle]['question']}")

    while nb_of_atttemps > 0:
        if nb_of_atttemps != 1:
            # Inform the user about the remaining attempts (not the last one)
            print(f"You have {nb_of_atttemps} attempts remaining to guess the riddle.")

        # Collect the player's answer
        answer = input("Enter your answer: ")
        answer = answer.lower()  # Normalize user's input to lowercase
        print(f"Your answer is {answer}.")

        # Normalize the correct answer from JSON for case-insensitive comparison
        solution = riddles_storage[selected_riddle]['answer']
        solution = solution.lower()

        if answer == solution:
            # The player guessed correctly
            print("Correct! You win a key!")
            return True
        else:
            # Player's answer is incorrect
            if nb_of_atttemps == 2:
                # Special message on the second-to-last attempt
                print("Hahaha! Last chance unfortunate!")
            else:
                # Generic failure message
                print(f"Incorrect! You lose a key! ")

            # Decrease the number of attempts remaining
            nb_of_atttemps -= 1

    # Player has no remaining attempts and failed the riddle
    print(
        f"Oh oh oh, how predictable. The riddle was too hard for you. Nobody can guess my riddles! The answer was {riddles_storage[selected_riddle]['answer']}")
    return False


load_riddles('Data/PFRiddles.json')
# pere_fouras_riddles()
