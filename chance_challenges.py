import random
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
shell_game()
