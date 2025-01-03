import json
import random


def treasure_room():
    """
    Simulates the final challenge in a treasure room.

    The player is provided with a set of clues to guess the correct code word.
    The game uses data from a JSON file (`Data/TRClues.json`), which contains
    multiple shows with associated clues and the final code word.

    Gameplay:
        - A random year and show are selected from the dataset.
        - Three initial clues are presented to the player.
        - The player has 3 attempts to guess the code word.
        - After each incorrect attempt, one additional clue may be provided,
          if available.
        - If the player guesses correctly, the treasure room is unlocked.
        - If the player exhausts all attempts, the correct answer is revealed.

    Returns:
        bool: True if the player guesses the code word correctly,
              False otherwise.
    """
    # Load the JSON file with the treasure room data
    with open('Data/TRClues.json', 'r') as f:
        tv_game = json.load(f)

    # Select data related to "Fort Boyard" from the JSON
    tv_game = tv_game["Fort Boyard"]

    # Randomly pick a year and corresponding show
    year = random.choice(list(tv_game.keys()))
    show = random.choice(list(tv_game[year].values()))

    # Extract the clues and code word from the selected show
    clues = show['Clues']
    code_word = show['CODE-WORD']

    # Display the initial set of clues
    print("Clues:")
    for i in range(3):
        print(f"->{clues[i]}")

    # Initialize the number of attempts and correct answer flag
    attempts = 3
    answer_correct = False

    # Start the guessing loop
    while attempts > 0:
        # Ask the player for their guess
        answer = input("Enter your guess for the code word(in uppercase only): ").strip().lower()

        # Check if the answer matches the code word
        if answer == code_word.lower():
            answer_correct = True
            break
        else:
            # Reduce attempts if the guess is incorrect
            attempts -= 1
            if attempts > 0:
                print(f"Wrong answer! {attempts} attempts remaining.")

                # Provide an additional clue if possible
                if len(clues) > 3 + (3 - attempts):
                    print(f"Additional clue: {clues[3 + (3 - attempts)]}")
            else:
                # Inform the player that they are out of attempts
                print(f"Wrong answer! No attempts remaining.")
                print(f"The correct code word was: {code_word}")

    # Provide the final outcome of the game
    if answer_correct:
        print("Congratulations! You've opened the treasure room and won the game!")
        return True
    else:
        print("Sorry! You've failed to open the treasure room.")
        return False

# Uncomment the following line to play the game
# treasure_room()
