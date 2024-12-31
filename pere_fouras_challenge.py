import json
from random import randint
def load_riddles(file):
    with open(file, 'r') as f:
        riddles=json.load(f)
    return riddles
def pere_fouras_riddles():
    riddles_storage=load_riddles('Data/PFRiddles.json')
    riddles_dictionnary={}
    nb_of_atttemps=3
    selected_riddle=randint(0,len(riddles_storage)-1)
    print(f"Here is the riddle: {riddles_storage[selected_riddle]['question']}")

    while nb_of_atttemps>0:
        if nb_of_atttemps!=1:
            print(f"You have {nb_of_atttemps} attempts remaining to guess the riddle.")
        answer=input("Enter your answer: ")
        answer=answer.lower()
        print(f"Your answer is {answer}.")
        solution=riddles_storage[selected_riddle]['answer']
        solution=solution.lower()
        if answer==solution:
            print("Correct! You win a key!")
            return True
        else:
            if nb_of_atttemps==2:
                print("Hahaha! Last chance unfortunate!")
            else:
                print(f"Incorrect! You lose a key! the answer was {riddles_storage[selected_riddle]['answer']}")
            nb_of_atttemps-=1
    print("Oh oh oh, how predictable. The riddle was too hard for you. Nobody can guess my riddles!")
    return False


load_riddles('Data/PFRiddles.json')
pere_fouras_riddles()