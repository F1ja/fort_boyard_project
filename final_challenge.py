#import random
#import json
def load_clues(file):
    with open('TRClues.json', 'r') as file:
        data = json.load(file)
        return data

#CLUES_FILE =load_clues('TRClues.json')
#
#print(CLUES_FILE['Fort Boyard']['2015']['Show 01']['Clues'])
#a=random.choice(CLUES_FILE['Fort Boyard'])
#print(a)
import json
import random
def treasure_room():
    tv_game = load_clues('TRClues.json')
    fort_boyard_data = tv_game["Fort Boyard"]
    list_of_years = list(fort_boyard_data.keys())
    random_year = random.choice(list(fort_boyard_data.keys()))
    random_show = random.choice(list(fort_boyard_data[tv_game].keys()))
    clues = fort_boyard_data[tv_game][random_show]["Clues"]
    print(f"Année : {tv_game}")
    print(f"Show : {random_show}")
    print("Clues :")
    print(clues)
treasure_room()