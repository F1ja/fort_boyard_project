def  introduction():
    print("The player must complete challenges to earn keys and unlock the treasure room.")
    print("The aim is to collect three keys to access the treasure room.")
#introduction()
def compose_equipe():
    team = []
    nb_players = 0
    nb_players = input("How many players do you want to include in the team? (max 3): ")
    while nb_players not in ["1", "2", "3"]:
        print("Invalid input. The team can have up to 3 players. Try again.")
        nb_players = input("How many players do you want to include in the team? (max 3): ")
    nb_players = int(nb_players)
    leader_found=False
    for i in range(nb_players):
        print(f"Enter details for Player {i + 1}:")
        name = input("Name: ")
        profession = input("Profession: ")
        if not leader_found:
            is_leader = input("Leader or Member: ")
            while is_leader not in ["Leader", "Member"]:
                is_leader=input("Invalid input. Choose 'Leader' or 'Member': ")
        else:
            print(f"The leader has already been selected. The player {name} is automatically assigned as a Member.")
            is_leader = 'Leader'
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
    challenges = ["Mathematics challenge", "Logic challenge", "Chance challenge", "Père Fouras' riddle"]
    while True:
        print("\n--- Challenges Menu ---")
        print("1. Mathematics challenge")
        print("2. Logic challenge")
        print("3. Chance challenge")
        print("4. Père Fouras' riddle")

        choice = input("Enter the number corresponding to your choice: ")
        while choice not in ["1", "2", "3", "4"]:
            choice = input("Invalid choice. Please enter a number between 1 and 4: ")
        choice = int(choice)
        print("You chose challenge", choice)
        print(challenges[choice-1])
        return choice

#challenges_menu()
#team = [
  #  {"name": "Jean Dupont", "profession": "Engineer", "role": "Leader"},
    #{"name": "Marie Martin", "profession": "Teacher", "role": "Member"},
    #{"name": "Paul Durand", "profession": "Doctor", "role": "Member"}]
#team=compose_equipe()
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
    choosed_player=input("Enter the player's number:")
    while choosed_player not in [str(i+1) for i in range(len(team))]:
        choosed_player=input("Invalid player number. Please try again:")
    choosed_player=int(choosed_player)
    choosed_player=team[choosed_player-1]
    print(choosed_player['name'])
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

    with open('Data/output/history.txt', 'a') as file:
        file.write(history_str)
#record_history("pere_fouras_challenge",team[0],team,3)
