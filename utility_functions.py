def introduction():
    """
    Provides an introduction to the game.

    Prints details about the goal of the game, which is to complete challenges,
    earn keys, and unlock the treasure room. Players must collect three keys
    to progress.
    """
    print("The player must complete challenges to earn keys and unlock the treasure room.")
    print("The aim is to collect three keys to access the treasure room.")


# introduction()

def compose_equipe():
    """
    Creates a team by allowing the user to input player details.

    The team size is limited to a maximum of 3 players. One player must
    be assigned the role of leader, while others are assigned as members.
    If no leader is selected, the first player is assigned the leader role
    automatically.

    Returns:
        list: A list of dictionaries containing player details,
              including name, profession, and role (Leader or Member).
    """
    team = []
    nb_players = 0

    # Prompt the user to choose the number of players
    nb_players = input("How many players do you want to include in the team? (max 3): ")
    while nb_players not in ["1", "2", "3"]:
        print("Invalid input. The team can have up to 3 players. Try again.")
        nb_players = input("How many players do you want to include in the team? (max 3): ")
    nb_players = int(nb_players)

    leader_found = False

    # Input player details for the specified number of players
    for i in range(nb_players):
        print(f"Enter details for Player {i + 1}:")
        name = input("Name: ")
        profession = input("Profession: ")

        # Only allow one player to be selected as the leader
        if not leader_found:
            is_leader = input("Leader or Member: ")
            while is_leader not in ["Leader", "Member"]:
                is_leader = input("Invalid input. Choose 'Leader' or 'Member': ")
        else:
            print(f"The leader has already been selected. The player {name} is automatically assigned as a Member.")
            is_leader = 'Member'

        if is_leader == 'Leader':
            leader_found = True

        # Create and add player to the team
        player = {"name": name, "profession": profession, "role": is_leader}
        team.append(player)

    # If no leader was selected, assign the first player as the leader
    if not leader_found:
        print(f"No leader was selected. {team[0]['name']} is automatically assigned as the leader.")
        team[0]['role'] = 'Leader'

    return team


# compose_equipe()


def challenges_menu():
    """
    Displays a menu of challenges for the user to choose from.

    The player selects one of four predefined challenges using a numeric input.
    Names of the challenges are displayed based on the selected option.

    Available challenges:
        1. Mathematics challenge
        2. Logic challenge
        3. Chance challenge
        4. Père Fouras' riddle

    Returns:
        int: The number corresponding to the chosen challenge (1-4).
    """
    challenges = ["Mathematics challenge", "Logic challenge", "Chance challenge", "Père Fouras' riddle"]
    while True:
        print("\n--- Challenges Menu ---")
        print("1. Mathematics challenge")
        print("2. Logic challenge")
        print("3. Chance challenge")
        print("4. Père Fouras' riddle")

        # Prompt user for a valid choice
        choice = input("Enter the number corresponding to your choice: ")
        while choice not in ["1", "2", "3", "4"]:
            choice = input("Invalid choice. Please enter a number between 1 and 4: ")

        choice = int(choice)
        print("You chose challenge", choice)
        print(challenges[choice - 1])
        return choice


# challenges_menu()

def choose_player(team):
    """
    Allows the user to select a player from the team.

    The function lists all team members with their attributes and prompts the
    user to select one. The player's details are returned.

    Args:
        team (list): A list of dictionaries, each representing a player's details.

    Returns:
        dict: The selected player's dictionary containing their information.
    """
    for position, player in enumerate(team):
        print(f"{position + 1}. {player['name']} ({player['profession']}) - {player['role']}")

    choosed_player = input("Enter the player's number: ")
    while choosed_player not in [str(i + 1) for i in range(len(team))]:
        choosed_player = input("Invalid player number. Please try again: ")

    # Retrieve and return the selected player's information
    choosed_player = int(choosed_player)
    choosed_player = team[choosed_player - 1]
    print(choosed_player['name'])
    return choosed_player


# choose_player(team)

def record_history(challenge_name, player, team, key_won):
    """
    Records the results of a challenge to a history file.

    The function saves information about the player, challenge chosen, and
    the result (Win or Loss) to an external file. Keys won, if any, are
    recorded as well.

    Args:
        challenge_name (str): The name of the completed challenge.
        player (dict): The player's details (name, profession, role).
        team (list): The full list of team members.
        key_won (int): The number of keys the team won from the challenge.
    """
    # Capture information about the challenge attempt
    history = {
        'challenge_name': challenge_name,
        'player_name': player['name'],
        'player_profession': player['profession'],
        'is_leader': player['role'],
        'result': 'Win' if key_won > 0 else 'Loss',
        'keys_won': key_won
    }

    # Format the information into a string
    history_str = f"Challenge: {history['challenge_name']}\n"
    history_str += f"Player: {history['player_name']} ({history['player_profession']})\n"
    history_str += f"Role: {history['is_leader']}\n"
    history_str += f"Result: {history['result']}\n"
    history_str += f"Keys Won: {history['keys_won']}\n"
    history_str += "-" * 40 + "\n"

    # Append the history to the output file
    with open('Data/output/history.txt', 'a') as file:
        file.write(history_str)
# record_history("pere_fouras_challenge", team[0], team, 3)
