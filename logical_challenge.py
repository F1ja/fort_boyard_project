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
    global player_shot_grid, opponent_grid, grid
    empty_grid()

    display_grid(grid, "Time to choose your boat position wisely !")

    boats = 0
    print("Place your boats !")

    while boats < 2:
        position = ask_position()
        row, col = map(int, position.split(","))
        row -= 1
        col -= 1

        if grid[row][col] == " ":
            grid[row][col] = "B"
            boats += 1
            display_grid(grid, f"Boat {boats} placed. Here is your grid with your boats:")
        else:
            print("Invalid position. Boat already placed at this position.")

    boats = 0
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
    global grid
    if player == 1:
        print("It's your turn to shoot!")
        display_grid(grid, "History of your previous shots ")
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
        display_grid(grid, "TEST")
        if grid[row_master][col_master] == "B":
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
    global player_shot_grid, opponent_grid, grid
    print("Welcome to the Battleship game!\nYou will face the mighty Game Master in a merciless battle.")
    print(
        "Here are the rules:\n- Each player must place 2 boats on a 3x3 grid.\n- Boats are represented by 'B' and missed shots by '.'.\n- Sunk boats are marked by 'X'.")

    # Initialisation des grilles
    grid = empty_grid()  # Grille du joueur contenant ses bateaux
    opponent_grid = empty_grid()  # Grille du Game Master contenant ses bateaux
    player_shot_grid = empty_grid()  # Grille où le joueur tire (historique de ses tirs)
    master_shot_grid = empty_grid()  # Grille où le Game Master tire (historique de ses tirs)

    # Placer les bateaux du joueur et du Game Master
    initialize()

    # Choix du premier joueur au hasard
    player = randint(0, 1)
    print(f"The Game Master is deciding who plays first...")
    sleep(2)
    print(f"{'You' if player == 1 else 'The Game Master'} will start!")
    sleep(1)

    # Boucle principale du jeu
    while True:
        if player == 1:
            # Tour du joueur
            print("\nYour turn to shoot!")
            display_grid(player_shot_grid, "Your shot history:")
            position = ask_position()  # Demander une position au joueur
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
            else:
                print("You already shot there! Try again.")
        else:
            # Tour du Game Master
            print("\nThe Game Master's turn:")
            row_master, col_master = randint(0, 2), randint(0, 2)  # Générer un tir aléatoire

            # Tant qu'il tire sur une position déjà essayée, on génère de nouvelles coordonnées
            while master_shot_grid[row_master][col_master] != " ":
                row_master, col_master = randint(0, 2), randint(0, 2)

            print(f"The Game Master shoots at position {row_master + 1},{col_master + 1}")
            master_shot_grid[row_master][col_master] = "."  # Marquer le tir du Game Master
            if grid[row_master][col_master] == "B":  # Vérifier si un bateau a été touché
                print("Hit! Sunk!")
                master_shot_grid[row_master][col_master] = "X"
                grid[row_master][col_master] = "X"  # Mettre à jour la grille principale
            else:
                print("Splash...")

            display_grid(master_shot_grid, "The Game Master's shot history:")

        # Vérification de victoire
        if has_won(player_shot_grid):
            print("Congratulations! You have sunk all the Game Master's boats. You win!")
            break
        elif has_won(master_shot_grid):
            print("The Game Master has sunk all your boats. You lose!")
            break

        # Passer au joueur suivant
        player = next_player(player)  # Passage au tour suivant
        sleep(1)


battleship_game()
