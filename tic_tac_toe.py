# ----- global variables ----

current_player = "X"
max_turn = 9
user = True


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    rows = {"A": 0, "B": 1, "C": 2}
    cols = {"1": 0, "2": 1, "3": 2}

    move = input("Please give me a coordinate!")

    if move == "quit":
        return ("q", "q")

    if len(move) == 2 and (move[0] in rows.keys() and move[1] in cols.keys()):
        row, col = rows[move[0]], cols[move[1]]
        if board[row][col] == ".":
            return (row, col)
        else:
            print("This coordinate is already taken!")
            return get_move(board, player)
    else:
        print("Give me valid coordinate!!! Combine (A, B, C) with (1, 2, 3)")
        return get_move(board, player)


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player
    return board


def win_row(board, user):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False


def win_col(board):
    board = [item for sublist in board for item in sublist]
    if board[0:7:3] == ["X", "X", "X"] or board[0:7:3] == ["0", "0", "0"]:
        return True
    elif board[1:8:3] == ["X", "X", "X"] or board[0:7:3] == ["0", "0", "0"]:
        return True
    elif board[2::3] == ["X", "X", "X"] or board[0:7:3] == ["0", "0", "0"]:
        return True
    else:
        return False


def win_diagonal(board):
    if (
        board[0][0] == current_player
        and board[1][1] == current_player
        and board[2][2] == current_player
    ):
        return True
    elif (
        board[0][2] == current_player
        and board[1][1] == current_player
        and board[2][0] == current_player
    ):
        return True
    else:
        return False


def has_won(board, player):
    """Returns True if player has won the game."""

    if win_row(board, player) or win_col(board) or win_diagonal(board):
        return True
    else:
        return False


def is_full(board):
    """Returns True if board is full."""
    flat_board = [item for sublist in board for item in sublist]
    return "." not in flat_board


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print("  1   2   3")
    print(f"A {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" ---+---+---")
    print(f"B {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" ---+---+---")
    print(f"C {board[2][0]} | {board[2][1]} | {board[2][2]}")


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    return print(f"{winner}")


def current_user(user):
    if user:
        return "X"
    else:
        return "O"


def tictactoe_game(mode="HUMAN-HUMAN"):
    global current_player

    board = init_board()
    turn = 0
    winner = ""
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    while turn < max_turn:
        print_board(board)
        print(f"{current_player}'s turn")
        (row, col) = get_move(board, current_player)
        if (row, col) == ("q", "q"):
            print("Thanks for playing")
            exit()
        board = mark(board, current_player, row, col)
        if is_full(board):
            print("No more moves left!")
            winner = "It's a tie!"
            break
        if has_won(board, current_player):
            winner = current_player + " has won!"
            break
        turn += 1
        if current_player == "X":
            current_player = "0"
        else:
            current_player = "X"

    print_board(board)
    print_result(winner)


def main_menu():
    tictactoe_game("HUMAN-HUMAN")


if __name__ == "__main__":
    main_menu()
