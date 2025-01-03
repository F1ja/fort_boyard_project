from chance_challenges import chance_challenge
from final_challenge import treasure_room
from logical_challenge import battleship_game
from maths_challenge import math_challenge
from pere_fouras_challenge import pere_fouras_riddles
from utility_functions import introduction, compose_equipe, challenges_menu, record_history, choose_player

game_number = 1
def game():
    global game_number
    if game_number == 1:
        with open("Data/output/history.txt", "w") as file:
            file.write("")
    with open("Data/output/history.txt", "a") as file:
        file.write(f"Game {game_number} summary:\n")
    introduction()
    print("You are going to create your team.")
    team = compose_equipe()
    keys = 0

    while keys < 3:
        challenge_choice = challenges_menu()
        print("Choose a player for the challenge:")
        player_choice = choose_player(team)
        player = player_choice['name']
        if challenge_choice == 1:
            if math_challenge():
                sleep(2)
                keys += 1
                print(f"{player} won the math challenge!")
                record_history("Math Challenge", player_choice, team, 1)
            else:
                sleep(2)
                print(f"{player} failed the math challenge.")
                record_history("Math Challenge", player_choice, team, 0)
        elif challenge_choice == 2:
            if battleship_game():
                sleep(2)
                keys += 1
                print(f"{player} won the Battleship game!")
                record_history("Battleship Game", player_choice, team, 1)
            else:
                sleep(2)
                print(f"{player} failed the Battleship game.")
                record_history("Battleship Game", player_choice, team, 0)
        elif challenge_choice == 3:
            if chance_challenge():
                sleep(2)
                keys += 1
                print(f"{player} won the Chance Challenge!")
                record_history("Chance Challenge", player_choice, team, 1)
            else:
                sleep(2)
                print(f"{player} failed the Chance Challenge.")
                record_history("Chance Challenge", player_choice, team, 0)
        elif challenge_choice == 4:
            if pere_fouras_riddles():
                sleep(2)
                keys += 1
                print(f"{player} won the Pere Fouras Riddles!")
                record_history("Pere Fouras Riddles", player_choice, team, 1)
            else:
                sleep(2)
                print(f"{player} failed the Pere Fouras Riddles.")
                record_history("Pere Fouras Riddles", player_choice, team, 0)
        if keys == 3:
            print("Congratulations! You have won 3 keys. Now, it's time for the final challenge.")
            if treasure_room():
                with open("Data/output/history.txt", "a") as file:
                    file.write("You unlocked the treasure room!\n")
                print("You have successfully unlocked the treasure room!")
            else:
                with open("Data/output/history.txt", "a") as file:
                    file.write("You failed to unlock the treasure room.\n")
                print("Unfortunately, you failed to unlock the treasure room.")
            show_summary = input("Would you like to see the game summary? (yes/no): ")
            if show_summary.lower() == "yes":
                with open("Data/output/history.txt", "r") as file:
                    print(file.read())
            play_again = input("\nDo you want to play another game? (yes/no): ")
            if play_again == "yes":
                game_number += 1
                game()
            else:
                game_number = 1
                print("Thank you for playing! Goodbye!")


game()