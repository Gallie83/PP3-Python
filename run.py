board = []

x_axis = [" ", "A", "B", "C", "D", "E", "F"]


def create_board():
    """
    Creates the board at the start of a new round
    """
    board.append(x_axis)
    for i in range(0, 5):
        board.append([f"{i + 1}"] + ["O"] * 6)


create_board()


def stack_board(board):
    """
    Stacks the board into equal columns and rows
    """
    for i in board:
        print(i)


stack_board(board)
