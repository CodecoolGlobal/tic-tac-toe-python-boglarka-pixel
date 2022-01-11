import time
import random

# ----- global variables ----

current_player = "X"
max_turn = 9


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return board


def want_quit(move):
    if move == "quit":
        exit()


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    rows = {"A": 0, "B": 1, "C": 2}
    cols = {"1": 0, "2": 1, "3": 2}

    move = input("Please give me a coordinate!")
    want_quit(move)

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
    row, col = random.randrange(3), random.randrange(3)

    if board[row][col] == ".":
        return (row, col)
    else:
        return get_ai_move(board, player)


def mark(board, current_player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = current_player
    return board


def win_row(board, current_player):
    for row in board:
        if row[0] == row[1] == row[2] and "." not in row:
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


def win_diagonal(board, current_player):
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


def has_won(board, current_player):
    """Returns True if player has won the game."""
    if (
        win_row(board, current_player)
        or win_col(board)
        or win_diagonal(board, current_player)
    ):
        return True
    else:
        return False


def is_full(board):
    """Returns True if board is full."""
    flat_board = [item for sublist in board for item in sublist]
    return "." not in flat_board


def print_board(board, current_player):
    """Prints a 3-by-3 board on the screen with borders."""
    print("  1   2   3")
    print(f"A {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" ---+---+---")
    print(f"B {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" ---+---+---")
    print(f"C {board[2][0]} | {board[2][1]} | {board[2][2]}")
    # print(f"{current_player}'s turn")


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    return print(f"{winner}")


def current_user(current_player):
    if current_player == "X":
        return "0"
    else:
        return "X"


def change_AI(is_AI):
    if is_AI:
        return False
    else:
        return True


def is_end(board, current_player, turn, winner):
    if is_full(board):
        print("No more moves left!")
        winner = "It's a tie!"
        turn = max_turn
    if has_won(board, current_player):
        winner = current_player + " has won!"
        turn = max_turn
    return turn, winner


def step(board, current_player, turn, winner, is_AI):
    print_board(board, current_player)
    if is_AI:
        print("Now AI is start to think!")
        for i in range(3):
            time.sleep(0.3)
            print(".")
        (row, col) = get_ai_move(board, current_player)
    else:
        (row, col) = get_move(board, current_player)
    board = mark(board, current_player, row, col)
    turn, winner = is_end(board, current_player, turn, winner)
    current_player = current_user(current_player)
    turn += 1
    return turn, winner, board, current_player


def tictactoe_game(mode, current_player):
    board = init_board()
    turn = 0
    winner = ""
    is_AI_start = {"HUMAN-HUMAN": False, "AI-HUMAN": True, "HUMAN-AI": False}
    is_AI = is_AI_start[mode]
    while turn < max_turn:
        if mode == "HUMAN-HUMAN":
            turn, winner, board, current_player = step(
                board, current_player, turn, winner, is_AI
            )
        elif mode == "AI-HUMAN":
            turn, winner, board, current_player = step(
                board, current_player, turn, winner, is_AI
            )
            is_AI = change_AI(is_AI)
        else:
            turn, winner, board, current_player = step(
                board, current_player, turn, winner, is_AI
            )
            is_AI = change_AI(is_AI)

    print_board(board, current_player)
    print_result(winner)


def main_menu():
    mode = input(
        "Please choose a game mode (1 = HUMAN-HUMAN, 2 = AI-HUMAN, 3 = HUMAN-AI): "
    )
    levels = {"1": "HUMAN-HUMAN", "2": "AI-HUMAN", "3": "HUMAN-AI"}

    try:
        mode = levels[mode]
        tictactoe_game(mode, current_player)
    except KeyError:
        print("Your choosed mode is invalid!")
        return main_menu()


if __name__ == "__main__":
    main_menu()
