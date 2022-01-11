import sys
import random

# ----- global variables ----

current_player = "X"
max_turn = 9


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
    row, col = random.randrange(3), random.randrange(3)

    if board[row][col] == ".":
        return (row, col)
    else:
        return get_ai_move(board, player)


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


def current_user(current_player):
    if current_player:
        return "X"
    else:
        return "O"


def human_human(board, turn, winner, max_turn, current_player):
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
        turn = max_turn
    if has_won(board, current_player):
        winner = current_player + " has won!"
        turn = max_turn
    turn += 1
    if current_player == "X":
        current_player = "0"
    else:
        current_player = "X"
    return turn, winner


def ai_human(board, turn, winner, max_turn):
    global current_player
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
        turn = max_turn
    if has_won(board, current_player):
        winner = current_player + " has won!"
        turn = max_turn
    turn += 1
    if current_player == "X":
        current_player = "0"
    else:
        current_player = "X"
    return turn, winner


def tictactoe_game(mode):
    print(mode)
    global current_player
    board = init_board()
    turn = 0
    winner = ""
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    while turn < max_turn:

        if mode == "HUMAN-HUMAN":
            turn, winner = human_human(board, turn, winner, max_turn)
        elif mode == "AI-HUMAN":
            turn, winner = ai_human(board, turn, winner, max_turn)
        else:
            turn, winner = human_ai(board, turn, winner, max_turn)

    print_board(board)
    print_result(winner)


def main_menu():
    mode = input(
        "Please choose a game mode (1 = HUMAN-HUMAN, 2 = AI-HUMAN, 3 = HUMAN-AI): "
    )
    levels = {"1": "HUMAN-HUMAN", "2": "AI-HUMAN", "3": "HUMAN-AI"}

    try:
        mode = levels[mode]
        tictactoe_game(mode)
    except KeyError:
        print("Your choosed mode is invalid!")
        return main_menu()


if __name__ == "__main__":
    main_menu()
