import random
from random import randint
def shell_game():
    shells = ['A', 'B', 'C']
    print("Welcome to the 'Shell Game'!")
    print("Rules: You must find under which of the three shells (A, B, or C) the key is hidden.")
    print("You have two attempts.")
    attempt = 0
    while attempt < 2:
        key = random.choice(shells)  # Rendre 'key' local
        guess = input("Guess the shell: ").upper()
        if guess not in shells:
            print("Invalid choice. Please guess one of the following: A, B, or C.")
            continue
        if guess == key:
            print("You found the key!")
            return True
        else:
            print("Wrong guess!")
            attempt += 1
    print("You lost!")
    print("The key was in:", key)
    return False
#shell_game()
def rolling_dice():
    attempt = 3
    while attempt > 0:
        print("You have " + str(attempt) + " attempts remaining to guess the numbers.")
        input("Press Enter to roll the dice...")
        pdice = [randint(1, 6), randint(1, 6)]
        print("You rolled:", pdice)
        for f in pdice:
            if f == 6:
                print("Congratulations! You win")
                return True
        print("Not 6. You are moving to the next attempt")
        gmdice = [randint(1, 6), randint(1, 6)]
        print("Game master rolled:", gmdice)
        for g in gmdice:
            if g == 6:
                print("The game master has won the game")
                return False
        attempt -= 1
    print("No one won, it's a draw, no key for you")
    return False
challenges={
    "Shell Game":shell_game,
    "Rolling Dice":rolling_dice}
def chance_challenge():
    print("Available challenges are:")
    for challenge in challenges.keys():
        print(f"- {challenge}")
    challenge_name = random.choice(list(challenges))
    print(f"You have chosen {challenge_name}")
    if challenges[challenge_name]():
        print("You win a key!")
    else:
        print("You lost!")
chance_challenge()
