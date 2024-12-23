from random import randint
from time import sleep

def next_player(player):
    if player == 1:
        return 0
    else:
        return 1
#def empty_grid():
#    global grid
#    grid=[[" "]*3]*3
# Correction de la fonction empty_grid
def empty_grid():
    global grid
    grid = [[" " for _ in range(3)] for _ in range(3)]
    return grid
#empty_grid()

def display_grid(grid,message):
    print(message)
    print()
    for row in grid:
        print("|"+"|".join(row)+"|")
    print("-"*(len(grid[0])*3-2))

#display_grid(grid,"The game starts here")
def ask_position():
        position=input("Enter the position you want to play (row, column) between 1 and 3 (e.g. 1,2):")
        while position not in ["1,1","1,2","1,3","2,1","2,2","2,3","3,1","3,2","3,3"]:
            print("Invalid position. Please try again.")
            position=input("Enter the position you want to play (row, column) between 1 and 3 (e.g. 1,2):")
        return position
#ask_position()





def initialize():
    empty_grid()

    display_grid(grid, "Time to choose your boat position wisely !")

    boats = 0
    print("Place your boats !")

    while boats < 2:
        position = input(f"Enter the position of boat {boats + 1} (row,column) between 1 and 3 (e.g., 1,2): ")
        if position in ["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"]:
            row, col = map(int, position.split(","))
            row -= 1
            col -= 1

            if grid[row][col] == " ":
                grid[row][col] = "B"
                boats += 1
                display_grid(grid, f"Boat {boats} placed. Here is your game with you boats:")
            else:
                print("Invalid position. Boat already placed at this position.")
        else:
            print("Invalid position. Please try again.")

    boats = 0
    position=0
    opponent_grid = empty_grid()
    while boats < 2:
        bot_boat_x = randint(1, 3)
        bot_boat_y = randint(1, 3)
        position = str(f"{bot_boat_x},{bot_boat_y}")
        if position in ["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"]:
            row, col = map(int, position.split(","))
            row -= 1
            col -= 1

            if opponent_grid[row][col] == " ":
                opponent_grid[row][col] = "B"
                boats += 1
    display_grid(opponent_grid, "Here is the game master's board:")
    return grid, opponent_grid

#print(initialize())
#global player_shot_grid,opponent_grid
#player_shot_grid=empty_grid()
#opponent_grid=empty_grid()

def turn(player, player_shot_grid, opponent_grid):

    if player == 1:
        print("It's your turn to shoot!")
        display_grid(player_shot_grid, "History of your previous shots ")
        position=ask_position()
        row,col=map(int,position.split(",")) #split and extract values
        row-=1
        col-=1
        if player_shot_grid[row][col] == " ":
            player_shot_grid[row][col]="."
            if opponent_grid[row][col] == "B":
                print("Hit! Sunk!")
                player_shot_grid[row][col]="X"
            else:
                print("Splash...")
    if player == 0:
        print("It's the game master's turn:")
        row_master=randint(0,2) #no need to -1 it
        col_master=randint(0,2)
        print(f"The game master shoots at position {row_master+1},{col_master+1}")
        if opponent_grid[row_master][col_master] == " ":
            opponent_grid[row_master][col_master]="."
            if player_shot_grid[row_master][col_master] == "B":
                print("Hit! Sunk!")
                opponent_grid[row_master][col_master]="X"
            else:
                print("Splash...")
#turn(1,player_shot_grid,opponent_grid)

def has_won(player_shots_grid):
    for row in player_shot_grid:
        kill_count=0
        if "X" in row:
            kill_count+=1
    if kill_count==2:
        return True
    else:
        return False
def battleship_game():
    print("Welcome to the Battleship game!\nYou will face the mighty Boyard Master in a merciless battle.")
    print("Here are the rules:\n-Each player must place 2 boats on a 3x3 grid.\n-Boats are represented by 'B' and missed shots by '.'.\n-Sunk boats are marked by 'x'.")
    empty_grid()
    player= randint(0,1)
    sleep(5)
    initialize()
    global player_shot_grid,opponent_grid
    player_shot_grid=empty_grid()
    sleep(2)
    display_grid(grid, "Here is your game with you boats:")
    display_grid(opponent_grid, "Here is the game master's board:")
    turn(player, player_shot_grid, opponent_grid)
    player=next_player(player)
    sleep(1)
    while has_won(player_shot_grid)==False:
        turn(player,player_shot_grid,opponent_grid)
        player=next_player(player)
        sleep(1)
battleship_game()
