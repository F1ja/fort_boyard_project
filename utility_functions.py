def  introduction():
    print("The player must complete challenges to earn keys and unlock the treasure room.")
    print("The aim is to collect three keys to access the treasure room.")
def compose_equipe():
    team = []
    nb_players = 0
    while nb_players < 1 or nb_players > 3:
        nb_players = int(input("How many players do you want to include in the team? (max 3): "))
        if nb_players < 1 or nb_players > 3:
            print("Invalid input. The team can have up to 3 players. Try again.")
    leader_found=False
    for i in range(nb_players):
        print(f"Enter details for Player {i + 1}:")
        name = input("Name: ")
        profession = input("Profession: ")
        if not leader_found:
            is_leader = input("Leader or Member: ")
        else:
            is_leader = input("There is already a leader in the team. Choose 'Member' :")
        if is_leader == 'Leader':
            leader_found = True
        player = {"name": name, "profession": profession, "role": is_leader}
        team.append(player)
    if not leader_found:
        print(f"No leader was selected. {team[0]['name']} is automatically assigned as the leader.")
        team[0]['role'] = 'Leader'
    return team
#compose_equipe()


def challenges_menu():
    while True:
        print("\n--- Challenges Menu ---")
        print("1. Mathematics challenge")
        print("2. Logic challenge")
        print("3. Chance challenge")
        print("4. Père Fouras' riddle")

        choice = int(input("Enter the number corresponding to your choice: "))
        if 1 > choice or choice > 4:
            print("Invalid choice. Please enter a number between 1 and 4.")
        else:
            print("You chose challenge", choice)
            return choice
        print("\n")
#challenges_menu()
#team = [
  #  {"name": "Jean Dupont", "profession": "Engineer", "role": "Leader"},
    #{"name": "Marie Martin", "profession": "Teacher", "role": "Member"},
    #{"name": "Paul Durand", "profession": "Doctor", "role": "Member"}]
team=compose_equipe()
def choose_player(team):
    """
    Allows the user to select a player from the team.

    Args:
        team (list): A list of dictionaries, each representing a player with their details.

    Returns:
        dict: The selected player's dictionary containing their information.
    """
    for position,player in enumerate(team):
        print(f"{position+1}.{player['name']} ({player['profession']}) - {player['role']}")
    choosed_player=int(input("Enter the player's number:"))
    while choosed_player<1 or choosed_player>len(team):
        print("Invalid player number. Please try again.")
    choosed_player=team[choosed_player-1]
    print(choosed_player['name'])
    print(choosed_player)
    return choosed_player
#choose_player(team)

def record_history(challenge_name, player,team, key_won):
    history = {
        'challenge_name': challenge_name,
        'player_name': player['name'],
        'player_profession': player['profession'],
        'is_leader': player['role'],
        'result': 'Win' if key_won > 0 else 'Loss',
        'keys_won': key_won
    }
    history_str = f"Challenge: {history['challenge_name']}\n"
    history_str += f"Player: {history['player_name']} ({history['player_profession']})\n"
    history_str += f"Role: {history['is_leader']}\n"
    history_str += f"Result: {history['result']}\n"
    history_str += f"Keys Won: {history['keys_won']}\n"
    history_str += "-" * 40 + "\n"

    with open('history.txt', 'a') as file:
        file.write(history_str)
#record_history("pere_fouras_challenge",team[0],team,3)
