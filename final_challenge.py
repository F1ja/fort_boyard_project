import json
import random

def treasure_room():
    with open('Data/TRClues.json','r') as f:
        tv_game = json.load(f)
    tv_game = tv_game["Fort Boyard"]
    year = random.choice(list(tv_game.keys()))
    show = random.choice(list(tv_game[year].values()))
    clues = show['Clues']
    code_word = show['CODE-WORD']
    print("Clues:")
    for i in range(3):
        print(f"->{clues[i]}")
    attempts = 3
    answer_correct = False
    while attempts > 0:
        answer = input("Enter your guess for the code word(in uppercase only): ").strip().lower()
        if answer == code_word.lower():
            answer_correct = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong answer! {attempts} attempts remaining.")
                if len(clues) > 3 + (3 - attempts):
                    print(f"Additional clue: {clues[3 + (3 - attempts)]}")
            else:
                print(f"Wrong answer! No attempts remaining.")
                print(f"The correct code word was: {code_word}")
    if answer_correct:
        print("Congratulations! You've opened the treasure room and won the game!")
        return True
    else:
        print("Sorry! You've failed to open the treasure room.")
        return False
#treasure_room()