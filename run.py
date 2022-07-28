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

guessed_locations = []


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
        ships_location.append(x)
        grid_locations.remove(x)


spawn_ships()
print(ships_location)


def check_col(player_guess):
    """
    Takes players shot and converts it to a number(e.g. D1=41)
    """
    global number
    number = str(x_axis.index(player_guess[0].upper())) + player_guess[1]
    print(number)


def hit_board(number, board):
    """
    If player hits ship, it marks an X on the board.
    Then removes ship from ships_location
    """
    board[int(number[1])][int(number[0])] = "X"
    set_board(board)
    x = str(player_guess.upper())
    ships_location.remove(x)


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


def check_duplicate(player_guess):
    """
    Ensures players guess has not already been used.
    Then checks that players guess is within row length.
    Then adds player shots to guessed_locations
    """
    if str(player_guess.upper()) in guessed_locations:
        print("You already shot there!")
        set_board(board)
        player_turn()
    elif int(number[1]) < 1 or int(number[1]) > 6:
        print("That point is not in the ocean! Try Again!")
        player_turn()
    else:
        check_col(player_guess)
        check_hit(player_guess)
        x = str(player_guess.upper())
        guessed_locations.append(x)
        player_turn()


def guess_check(player_guess):
    """
    Checks if the players guess is on the board
    """
    if str(player_guess.upper()) in grid_locations or ships_location:
        try:
            print(player_guess)
            check_duplicate(player_guess)

        except:
            print("That point is not in the ocean! Try Again!")
            player_turn()


def player_turn():
    """
    Checks that player has run out of turns or if game has been won.
    If neither is true then asks player for next shot
    """
    if len(guessed_locations) > 10:
        print("Your out of moves! Game over!")

    elif len(ships_location) == 0:
        print("Congratulations! You Won!")

    else:
        global player_guess
        player_guess = input("Enter your shot coordinates(in the form A1): ")
        guess_check(player_guess)


player_turn()
