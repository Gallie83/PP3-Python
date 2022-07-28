import random
board = []

x_axis = [" ", "A", "B", "C", "D", "E", "F"]

grid_locations = [
    "A1", "A2", "A3", "A4", "A5", "A6",
    "B1", "B2", "B3", "B4", "B5", "B6",
    "C1", "C2", "C3", "C4", "C5", "C6",
    "D1", "D2", "D3", "D4", "D5", "D6",
    "E1", "E2", "E3", "E4", "E5", "E6",
    "F1", "F2", "F3", "F4", "F5", "F6"
]

ships_location = []


def create_board():
    """
    Creates the board at the start of a new round
    """
    board.append(x_axis)
    for i in range(0, 6):
        board.append([f"{i + 1}"] + ["O"] * 6)


create_board()


def set_board(board):
    """
    Removes apostrophes from board and replaces with spaces
    """
    for i in board:
        print("  ".join(i))


set_board(board)


def spawn_ships():
    """
    Generates 4 random points on the grid for ships to be spawned
    """
    for i in range(4):
        x = random.choice(grid_locations)
        if x not in ships_location:
            ships_location.append(x)


spawn_ships()
print(ships_location)


player_guess = input("Enter your shot coordinates(in the form A1): ")


def check_col(player_guess):
    """
    Takes players shot and converts it to a number(e.g. D1=41)
    """
    global number
    number = str(x_axis.index(player_guess[0].upper())) + player_guess[1]
    print(number)


def hit_board(number, board):
    board[int(number[1])][int(number[0])] = "X"
    set_board(board)


def check_hit(player_guess):
    """
    Checks if player has hit a ship
    """
    if str(player_guess.upper()) in ships_location:
        print("You sunk my battleship!")
        hit_board(number, board)
    else:
        print("Miss!")
        board[int(number[1])][int(number[0])] = "!"
        set_board(board)


def guess_check(player_guess):
    """
    Checks if the players guess is on the board
    """
    if str(player_guess.upper()) in grid_locations:
        print(player_guess)
        check_col(player_guess)
        check_hit(player_guess)
    else:
        print("Invalid location. Try Again!")


guess_check(player_guess)
