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

ships_sank = []

guessed_locations = []

difficulty = []

wins = 0

losses = 0


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


def hit_board(number, board):
    """
    If player hits ship, it marks an X on the board.
    Then removes ship from ships_location
    """
    board[int(number[1])][int(number[0])] = "X"
    set_board(board)
    x = str(player_guess.upper())
    ships_sank.append(x)
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
    else:
        check_col(player_guess)
        check_hit(player_guess)
        x = str(player_guess.upper())
        guessed_locations.append(x)
        player_turn()


def check_row(player_guess):
    """
    Checks that the row selection from the players shot is valid
    """
    if int(player_guess[1]) < 1 or int(player_guess[1]) > 6:
        print("That point is not in the ocean! Try Again!")
        player_turn()
    else:
        check_duplicate(player_guess)


def guess_check(player_guess):
    """
    Checks if the players guess is on the board
    """
    try:
        if str(player_guess.upper()) in grid_locations or ships_location:
            check_row(player_guess)

    except:
        print("That point is not in the ocean! Try Again!")
        player_turn()


def next_round():
    """
    Generates a new board with new ships
    """
    create_board()
    set_board(board)
    spawn_ships()
    print(ships_location)
    choose_difficulty()


def clear_table():
    """
    Clears table and resets arrays
    """
    board.clear()
    ships_location.clear()
    guessed_locations.clear()
    grid_locations.append(ships_sank)
    ships_sank.clear()
    next_round()


def new_game():
    """
    Checks if user wants to play again
    """
    n = str(input("Press Y to play again!"))
    if n.upper() == "Y":
        clear_table()


def player_turn():
    """
    Checks if player has run out of turns or if game has been won.
    If neither is true then asks player for next shot
    """
    if len(guessed_locations) > (difficulty[0] - 1):
        print("Your out of moves! Game over!")
        print("Ships Remaining: " + str(4 - len(ships_sank)))
        new_game()

    elif len(ships_sank) == 4:
        print("Congratulations! You Won!")
        new_game()

    else:
        global player_guess
        print("Remaining chances: " +
              str(difficulty[0] - len(guessed_locations)))
        player_guess = input("Enter your shot coordinates(in the form A1): ")
        guess_check(player_guess)


def choose_difficulty():
    """
    Asks player for difficulty and bases amount of turns on player input
    """
    level = input("Choose your difficulty(Easy(30)/Med(20)/Hard(15)): ")
    if str(level.upper()) == "EASY":
        difficulty.append(30)
    elif str(level.upper()) == "MED":
        difficulty.append(20)
    elif str(level.upper()) == "HARD":
        difficulty.append(15)
    else:
        print(level + " is not an option!")
        choose_difficulty()
    player_turn()


choose_difficulty()
