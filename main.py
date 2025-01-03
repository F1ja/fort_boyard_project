from chance_challenges import chance_challenge
from final_challenge import treasure_room
from logical_challenge import battleship_game
from maths_challenge import math_challenge
from pere_fouras_challenge import pere_fouras_riddles
from utility_functions import introduction, compose_equipe, challenges_menu, record_history, choose_player

game_number = 1  # Tracks the current game number


def game():
    """
    Main function to run the entire game sequence.

    The game involves creating a team, completing various challenges,
    earning keys, and attempting to unlock the treasure room. Each game
    is recorded in the history file, and the player can choose to replay
    or view a summary after completing the game.

    Workflow:
        1. Clear the history file for the first game.
        2. Introduce the game and allow the user to form a team.
        3. Loop through challenges until three keys are earned.
        4. Enter the final challenge (treasure room).
        5. Record results in the history file and offer replay or summary.

    Global Variables:
        - `game_number`: Tracks and resets the game count.

    """
    global game_number

    # Clear the history file for the first game
    if game_number == 1:
        with open("Data/output/history.txt", "w") as file:
            file.write("")

    # Start logging the summary of the current game
    with open("Data/output/history.txt", "a") as file:
        file.write(f"Game {game_number} summary:\n")

    # Game introduction and team composition
    introduction()  # Display introductory instructions
    print("You are going to create your team.")
    team = compose_equipe()  # Gather player details
    keys = 0  # Initialize the number of keys earned

    # Loop to perform challenges until 3 keys are earned
    while keys < 3:
        # Display challenges menu and allow player selection
        challenge_choice = challenges_menu()
        print("Choose a player for the challenge:")
        player_choice = choose_player(team)  # Let user select a team member
        player = player_choice['name']  # Get the player's name

        # Perform the selected challenge
        if challenge_choice == 1:  # Mathematics Challenge
            if math_challenge():
                # On success, log result and increase key count
                sleep(2)
                keys += 1
                print(f"{player} won the math challenge!")
                record_history("Math Challenge", player_choice, team, 1)
            else:
                # On failure, log result
                sleep(2)
                print(f"{player} failed the math challenge.")
                record_history("Math Challenge", player_choice, team, 0)
        elif challenge_choice == 2:  # Battleship Game
            if battleship_game():
                sleep(2)
                keys += 1
                print(f"{player} won the Battleship game!")
                record_history("Battleship Game", player_choice, team, 1)
            else:
                sleep(2)
                print(f"{player} failed the Battleship game.")
                record_history("Battleship Game", player_choice, team, 0)
        elif challenge_choice == 3:  # Chance Challenge
            if chance_challenge():
                sleep(2)
                keys += 1
                print(f"{player} won the Chance Challenge!")
                record_history("Chance Challenge", player_choice, team, 1)
            else:
                sleep(2)
                print(f"{player} failed the Chance Challenge.")
                record_history("Chance Challenge", player_choice, team, 0)
        elif challenge_choice == 4:  # Père Fouras' Riddles
            if pere_fouras_riddles():
                sleep(2)
                keys += 1
                print(f"{player} won the Pere Fouras Riddles!")
                record_history("Pere Fouras Riddles", player_choice, team, 1)
            else:
                sleep(2)
                print(f"{player} failed the Pere Fouras Riddles.")
                record_history("Pere Fouras Riddles", player_choice, team, 0)

        # Check if the player has earned 3 keys to proceed to the final challenge
        if keys == 3:
            print("Congratulations! You have won 3 keys. Now, it's time for the final challenge.")

            # Attempt to unlock the treasure room
            if treasure_room():
                # Success: Log result in history
                with open("Data/output/history.txt", "a") as file:
                    file.write("You unlocked the treasure room!\n")
                print("You have successfully unlocked the treasure room!")
            else:
                # Failure: Log result in history
                with open("Data/output/history.txt", "a") as file:
                    file.write("You failed to unlock the treasure room.\n")
                print("Unfortunately, you failed to unlock the treasure room.")

            # Offer to show game summary
            show_summary = input("Would you like to see the game summary? (yes/no): ")
            if show_summary.lower() == "yes":
                with open("Data/output/history.txt", "r") as file:
                    print(file.read())

            # Offer replay option
            play_again = input("\nDo you want to play another game? (yes/no): ")
            if play_again == "yes":
                game_number += 1
                game()  # Restart the game
            else:
                game_number = 1  # Reset game count
                print("Thank you for playing! Goodbye!")


# Main entry point
game()
