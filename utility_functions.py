def  introduction():
    print("The player must complete challenges to earn keys and unlock the treasure room.")
    print("The aim is to collect three keys to access the treasure room.")
def compose_equipe():
    n=4
    while n>3:
        n=int(input("Enter the number of players in your team: "))
        if n>3:
            print("you can't have more than 3 players in your team.")
            print("Enter again")

def challenges_menu():
    while True:
        print("\n--- Challenges Menu ---")
        print("1. Mathematics challenge")
        print("2. Logic challenge")
        print("3. Chance challenge")
        print("4. Père Fouras' riddle")

        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if 1 > choice or choice > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
            else:
                print("You chose challenge", choice)
                return choice
        finally:
            print("\n")
#challenges_menu()
team = [
    {"name": "Jean Dupont", "profession": "Engineer", "role": "Leader"},
    {"name": "Marie Martin", "profession": "Teacher", "role": "Member"},
    {"name": "Paul Durand", "profession": "Doctor", "role": "Member"}]
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
    choosed_player=team[choosed_player-1]
    print(choosed_player['name'])
    print(choosed_player)
    return choosed_player
choose_player(team)