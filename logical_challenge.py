from random import randint
from time import sleep

def next_player(player):
    """
    Switches the turn to the next player.

    Parameters:
        player (int): The current player (1 for human, 0 for the Game Master).

    Returns:
        int: The next player (0 for Game Master, 1 for human).
    """
    return 0 if player == 1 else 1
def empty_grid():
    """
    Initializes an empty 3x3 grid for the game.

    Returns:
        list: A 3x3 grid filled with empty spaces represented as " ".
    """
    grid = [[" " for _ in range(3)] for _ in range(3)]
    return grid


def display_grid(grid, message):
    """
    Displays the game grid along with a message.

    Parameters:
        grid (list): The 3x3 grid to be displayed.
        message (str): A message to display above the grid.

    Returns:
        The game grid with the message displayed above it.
    """
    print(message)
    print()
    for row in grid:
        print("|" + "|".join(row) + "|")
    print("-" * (len(grid[0]) * 3 - 2))
    return grid
def ask_position():
    """
    Prompts the user to enter a valid position on the grid for their action.
    Checks the input validity and ensures the position is valid.

    Returns:
        str: The selected position in the format "row,column" (e.g., "1,2").
    """
    position = input("Enter the position you want to play (row, column) between 1 and 3 (e.g. 1,2):")
    while position not in ["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"]:
        print("Invalid position. Please try again.")
        position = input("Enter the position you want to play (row, column) between 1 and 3 (e.g. 1,2):")
    return position
def initialize():
    """
    Initializes the game by allowing the player to place boats on their grid and
    randomly places boats for the Game Master. This function sets the game state.

    Returns:
        tuple: A tuple containing the player's grid with boats and the opponent's grid with boats.
    """
    global  opponent_grid, grid
    grid=empty_grid()

    display_grid(grid, "Time to choose your boat position wisely!")

    boats = 0
    print("Place your boats!")

    # Human player places boats
    while boats < 2:
        position = ask_position()  # Use ask_position for valid input
        row, col = map(int, position.split(","))
        row -= 1
        col -= 1

        if grid[row][col] == " ":
            grid[row][col] = "B"  # Place a boat
            boats += 1
            display_grid(grid, f"Boat {boats} placed. Here is your grid with your boats:")
        else:
            print("Invalid position. Boat already placed at this position.")

    # Game Master places boats randomly
    boats = 0
    opponent_grid = empty_grid()
    while boats < 2:
        bot_boat_x = randint(1, 3)
        bot_boat_y = randint(1, 3)
        position = str(f"{bot_boat_x},{bot_boat_y}")
        row, col = map(int, position.split(","))
        row -= 1
        col -= 1

        if opponent_grid[row][col] == " ":
            opponent_grid[row][col] = "B"
            boats += 1

    return grid, opponent_grid

master_hit=0 #master win parameter
def turn(player, player_shot_grid, opponent_grid):
    """
    Executes the turn of the current player (human or Game Master).
    The human player chooses a position to shoot, while the Game Master shoots randomly.

    Parameters:
        player (int): Indicates the current player (1 for human, 0 for Game Master).
        player_shot_grid (list): The grid that tracks the player's shooting history.
        opponent_grid (list): The grid that contains the boats of the opponent.

    Returns:
        None
    """
    global master_hit
    if player == 1:  # Human player's turn
        print("It's your turn to shoot!")
        display_grid(player_shot_grid, "History of your previous shots")
        position = ask_position()
        row, col = map(int, position.split(","))
        row -= 1
        col -= 1
        while player_shot_grid[row][col] == "X" or player_shot_grid[row][col] == ".":
            print("You already shot there! Try again.")
            position = ask_position()
            row, col = map(int, position.split(","))
            row -= 1
            col -= 1
        if player_shot_grid[row][col] == " ":
            player_shot_grid[row][col] = "."
            if opponent_grid[row][col] == "B":
                print("Hit! Sunk!")
                player_shot_grid[row][col] = "X"
            else:
                print("Splash...")


    elif player == 0:  # Game Master's turn
        print("It's the Game Master's turn:")
        row_master, col_master = randint(0, 2), randint(0, 2)

        # Keep generating random positions until a valid one is found
        while grid[row_master][col_master] == "." or grid[row_master][col_master] == "X":
            row_master, col_master =randint(0, 2), randint(0, 2)

        print(f"The Game Master shoots at position {row_master + 1},{col_master + 1}")
        sleep(2)
        if grid[row_master][col_master] == "B":
            print("Hit! Sunk!")
            master_hit += 1
            grid[row_master][col_master] = "X"  # Update player's grid
        else:
            print("Splash...")
            grid[row_master][col_master]="."
        display_grid(grid, "The grid of your boats")
        sleep(4)
def has_won(player_shots_grid):
    """
    Checks if all the boats of the opponent have been sunk (i.e., all marked as 'X').

    Parameters:
        player_shots_grid (list): The grid representing the player's or Game Master's shots.

    Returns:
        bool: True if the player has won, False otherwise.
    """
    kill_count = 0
    for row in range(3):
        if player_shots_grid[row][0] == "X" or player_shots_grid[row][1] == "X" or player_shots_grid[row][2] == "X":
            kill_count +=1
    if kill_count == 2:
            return True
    return False

def battleship_game():
    """
    Starts and manages the flow of the Battleship game.
    Allows the human player to face the Game Master in a turn-based game.

    Returns:
        None
    """
    global player_shot_grid, opponent_grid, grid
    print("Welcome to the Battleship game!\nYou will face the mighty Game Master in a merciless battle.")
    print("Here are the rules:\n- Each player must place 2 boats on a 3x3 grid.\n- Boats are represented by 'B'.")
    print("- Missed shots are marked as '.'. Sunk boats are marked as 'X'. Good luck!")

    # Initialize game components
    grid=empty_grid()
    player = randint(0, 1)  # Randomly decide who starts
    initialize()
    player_shot_grid = empty_grid()  # For tracking the player's shots
    sleep(4)
    print(f"{'You' if player == 1 else 'The Game Master'} will start!")

    # Game loop
    while True:
        turn(player, player_shot_grid, opponent_grid)
        if has_won(player_shot_grid):
            print("Congratulations! You have sunk all the Game Master's boats!")
            return True
            break
        if master_hit==2:
            print("The Game Master has sunk all your boats. You lose!")
            return False
            break
        player = next_player(player)  # Pass turn to the next player
        sleep(3)

#battleship_game()