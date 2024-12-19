import random
from random import randint
from operator import truediv


def shell_game():
    global key
    shells = ['A', 'B', 'C']
    print("Welcome to the 'Shell Game'!")
    print("Rules: You must find under which of the three shells (A, B, or C) the key is hidden.")
    print("You have two attempts.")
    attempt =0
    while attempt <2 :
        key = random.choice(shells)
        guess = input("Guess the shell: ")
        if guess == key:
            print("You found the key!")
            return True
        else:
            print("Wrong guess!")
            attempt +=1
    if attempt == 2 :
        print("You lost!")
        print("The key was in: " + key)
        return False
#shell_game()
def rolling_dice():
    attempt=3

    while attempt>0:
        print("You have " + str(attempt) + " attempts remaining to guess the numbers.")
        input("Press Enter to roll the dice...")
        pdice = [randint(1, 6), randint(1, 6)]
        print("You rolled:", pdice)
        for f in pdice:
            if f == 6:
                print("Congratulations! You win")
                return True
        print("Not 6. You are moving to the next attempt")
        if attempt == 0:
            print("No one have one, its a draw, no key for you")
            return False
        gmdice = [randint(1, 6), randint(1, 6)]
        print("Game master rolled:", gmdice)
        for g in gmdice:
            if g == 6:
                print("The game master has won the game")
                return False
        attempt -= 1
rolling_dice()
