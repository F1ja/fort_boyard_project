def next_player(player):
    if player == 1:
        return 0
    else:
        return 1
def empty_grid():
    global grid
    grid=[[" "]*3]*3
def display_grid(grid,message):
    print(message)
    print()
    for row in grid:
        print("|"+"|".join(row)+"|")
    print("-"*(len(grid[0])*3-2))
    print(grid)
empty_grid()
display_grid(grid,"The game starts here")
def ask_position():
    while True:
        position=input("Enter the position you want to play (row, column) between 1 and 3 (e.g. 1,2):")
        if
