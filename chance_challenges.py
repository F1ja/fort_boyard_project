import random
from random import randint

# Global variables for messages and shell options
shells = ['A', 'B', 'C']
welcome_mess = "Welcome to the 'Shell Game'!"
rules_mess = "Rules: You must find under which of the three shells (A, B, or C) the key is hidden."
invalid_mess = "Invalid choice. Please guess one of the following: A, B, or C."
attempts_mess = "You have {} attempts remaining to guess the numbers."

def roll_dice():
    """
    Simulates rolling two dice.
    Returns a list containing the result of two dice rolls.
    """
    return [randint(1, 6), randint(1, 6)]

def shell_game():
    """
    Chance-based game where the player must guess the shell hiding a key.
    The player has two attempts to guess correctly.
    
    Returns:
        True if the player finds the key, False otherwise.
    """
    print(welcome_mess)
    print(rules_mess)
    print("You have two attempts.")

    # Randomly place the key under one of the shells
    key = random.choice(shells)
    attempts = 2

    # Allow the player to make guesses
    for attempt in range(attempts):
        guess = input("Guess the shell: ").upper()
        if guess not in shells:
            print(invalid_mess)
            continue
        if guess == key:
            print("You found the key!")
            return True
        else:
            print("Wrong guess!")
    print("You lost! The key was in:", key)
    return False

def rolling_dice():
    """
    Chance-based dice game where the player rolls two dice.
    The goal is to roll a 6 in up to three attempts. If the player fails,
    the game master also rolls the dice, potentially beating the player.
    
    Returns:
        True if the player rolls a 6 before losing, False if the game master wins or no one wins.
    """
    attempts = 3
    while attempts > 0:
        print(attempts_mess.format(attempts))
        input("Press Enter to roll the dice...")

        # Player rolls the dice
        player_dice = roll_dice()
        print("You rolled:", player_dice)
        if 6 in player_dice:
            print("Congratulations! You win!")
            return True

        print("No 6. You are moving to the next attempt.")

        # Game master rolls the dice
        gm_dice = roll_dice()
        print("Game master rolled:", gm_dice)
        if 6 in gm_dice:
            print("The game master has won the game!")
            return False

        attempts -= 1
    print("No one won, it's a draw. No key for you.")
    return False

# Dictionary of available challenges
challenges = {
    "Shell Game": shell_game,
    "Rolling Dice": rolling_dice
}

def chance_challenge():
    """
    Main function to select and execute a random chance-based challenge.
    The player can win a key if they succeed in the chosen challenge.
    """
    print("Available challenges are:")
    for challenge_name in challenges.keys():
        print(f"- {challenge_name}")

    # Randomly choose a challenge
    chosen_challenge = random.choice(list(challenges))
    print(f"{chosen_challenge} has been chosen!")

    # Execute the chosen challenge
    if challenges[chosen_challenge]():
        print("You win a key!")
    else:
        print("You lost!")

# Start the challenge
chance_challenge()