import random
from random import randint

shells= ['A', 'B', 'C']
welcome_mess = "Welcome to the 'Shell Game'!"
rules_mess = "Rules: You must find under which of the three shells (A, B, or C) the key is hidden."
invalid_mess = "Invalid choice. Please guess one of the following: A, B, or C."
attempts_mess = "You have {} attempts remaining to guess the numbers."


def roll_dice():
    return [randint(1, 6), randint(1, 6)]


def shell_game():
    print(welcome_mess)
    print(rules_mess)
    print("You have two attempts.")

    key = random.choice(shells)
    attempts = 2

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
    attempts = 3
    while attempts > 0:
        print(attempts_mess.format(attempts))
        input("Press Enter to roll the dice...")

        player_dice = roll_dice()
        print("You rolled:", player_dice)
        if 6 in player_dice:
            print("Congratulations! You win")
            return True

        print("Not 6. You are moving to the next attempt")

        gm_dice = roll_dice()
        print("Game master rolled:", gm_dice)
        if 6 in gm_dice:
            print("The game master has won the game")
            return False

        attempts -= 1
    print("No one won, it's a draw, no key for you")
    return False


challenges = {
    "Shell Game": shell_game,
    "Rolling Dice": rolling_dice
}


def chance_challenge():
    print("Available challenges are:")
    for challenge_name in challenges.keys():
        print(f"- {challenge_name}")

    chosen_challenge = random.choice(list(challenges))
    print(f" {chosen_challenge} has been choosen")

    if challenges[chosen_challenge]():
        print("You win a key!")
    else:
        print("You lost!")


chance_challenge()
