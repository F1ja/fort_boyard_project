from chance_challenges import chance_challenge
from final_challenge import treasure_room
from logical_challenge import battleship_game
from maths_challenge import math_challenge
from pere_fouras_challenge import pere_fouras_riddles
from utility_functions import introduction, compose_equipe, challenges_menu, record_history


def game():
    introduction()
    print("You are going to create your team.")
    team = compose_equipe()
    keys = 0

    while keys < 3:
        challenge_choice = challenges_menu()
        print("Choose a player for the challenge:")
        for i, player in enumerate(team):
            print(f"{i + 1}. {player['name']} ({player['role']})")

        player_choice = int(input("Enter the number of the player you want to select: ")) - 1
        player = team[player_choice]
        if challenge_choice == 1:
            if math_challenge():
                keys += 1
                print(f"{player['name']} won the math challenge!")
                record_history("Math Challenge", player, team, 1)
            else:
                print(f"{player['name']} failed the math challenge.")
                record_history("Math Challenge", player, team, 0)
        elif challenge_choice == 2:
            if battleship_game():
                keys += 1
                print(f"{player['name']} won the Battleship game!")
                record_history("Battleship Game", player, team, 1)
            else:
                print(f"{player['name']} failed the Battleship game.")
                record_history("Battleship Game", player, team, 0)
        elif challenge_choice == 3:
            if chance_challenge():
                keys += 1
                print(f"{player['name']} won the Chance Challenge!")
                record_history("Chance Challenge", player, team, 1)
            else:
                print(f"{player['name']} failed the Chance Challenge.")
                record_history("Chance Challenge", player, team, 0)
        elif challenge_choice == 4:
            if pere_fouras_riddles():
                keys += 1
                print(f"{player['name']} won the Pere Fouras Riddles!")
                record_history("Pere Fouras Riddles", player, team, 1)
            else:
                print(f"{player['name']} failed the Pere Fouras Riddles.")
                record_history("Pere Fouras Riddles", player, team, 0)
        if keys == 3:
            print("Congratulations! You have won 3 keys. Now, it's time for the final challenge.")
            if treasure_room():
                print("You have successfully unlocked the treasure room!")
            else:
                print("Unfortunately, you failed to unlock the treasure room.")
            show_summary = input("Would you like to see the game summary? (yes/no): ")
            if show_summary.lower() == "yes":
                with open("Data/output/history.txt", "r") as file:
                    print("\nGame Summary:")
                    print(file.read())
            play_again = input("\nDo you want to play another game? (yes/no): ")
            if play_again == "yes":
                game()
            else:
                print("Thank you for playing! Goodbye!")


game()