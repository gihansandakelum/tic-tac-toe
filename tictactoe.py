# tictactoe.py
import time

from random import randrange, choice
from typing import List, Dict

Board = List[List[str]]


def display_board(board: Board) -> None:
    """
    Displays the current state of the Tic-Tac-Toe board.

    Args:
        board (Board): 3x3 list containing numbers, 'X', or 'O'.
    """
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        for col in range(3):
            print(f"|   {board[row][col]}   ", end="")
        print("|")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def free_fields(board: Board) -> List[int]:
    """
    Returns a list of available positions on the board.

    Args:
        board (Board): Current 3x3 board.

    Returns:
        List[int]: List of free cell numbers.
    """
    return [int(cell) for row in board for cell in row if cell not in ("X", "O")]


def game_opponent() -> str:
    """
    User can call the game opponent.
    """
    while True:
        user_game_mode = input("Do you want to play with Computer(C) or with Friend(F): ").strip().upper()
        if user_game_mode =="C":
            return "COMPUTER"
        if user_game_mode =="F":
            return "FRIEND"
        print("Invalid choice. Type C or F.")


def toss() -> dict:
    """
    User calls Heads or Tails before the toss.
    Returns a dictionary containing toss result and player assignments.
    """
    user_game_opponent = game_opponent()

    while True:
        user_call = input("Call it! Heads (H) or Tails (T): ").strip().upper()
        if user_call in ("H", "T"):
            break
        print("Invalid choice. Type H or T.")

    print("Flipping the coin", end="", flush=True)
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()

    coin = choice(("H", "T"))

    if coin == user_call:
        print(f"🎉 Coin landed {coin}! You won the toss.")
        return {
            "toss_winner": "USER",
            "next_player": "USER",
            "game_opponent": user_game_opponent,
            "user": "X",
            "opponent": "O",
        }
    else:
        print(f"🎉 Coin landed {coin}! {user_game_opponent} won the toss.")
        return {
            "toss_winner": user_game_opponent,
            "next_player": user_game_opponent,
            "game_opponent": user_game_opponent,
            "user": "O",
            "opponent": "X",
        }


def computer_move(board: Board, symbol: str) -> None:
    """
    Performs a random move for the computer.

    Args:
        board (Board): Current board.
        symbol (str): Computer's symbol ('X' or 'O').
    """
    move = choice(free_fields(board))
    row, col = (move - 1) // 3, (move - 1) % 3
    board[row][col] = symbol
    print("Computer played:")
    display_board(board)


def user_move(board: Board, symbol: str) -> None:
    """
    Prompts the user to make a move.

    Args:
        board (Board): Current board.
        symbol (str): User's symbol ('X' or 'O').
    """
    while True:
        try:
            move = int(input("Input your move (1-9): "))
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        if move in free_fields(board):
            row, col = (move - 1) // 3, (move - 1) % 3
            board[row][col] = symbol
            print("You played:")
            display_board(board)
            break
        else:
            print("This position is already taken or invalid.")

            
def friend_move(board: Board, symbol: str) -> None:
    """
    Prompts the user to make a move.

    Args:
        board (Board): Current board.
        symbol (str): User's symbol ('X' or 'O').
    """
    while True:
        try:
            move = int(input("Input friend's move (1-9): "))
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        if move in free_fields(board):
            row, col = (move - 1) // 3, (move - 1) % 3
            board[row][col] = symbol
            print("Friend played:")
            display_board(board)
            break
        else:
            print("This position is already taken or invalid.")
            
            

def check_winner(board: Board, symbol: str) -> bool:
    """
    Checks if the player has won the game.

    Args:
        board (Board): Current board.
        symbol (str): Player's symbol ('X' or 'O').

    Returns:
        bool: True if the player has won, else False.
    """
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False


def main() -> None:
    """
    Main loop to run the Tic-Tac-Toe game.
    """
    print("===== Welcome to Tic-Tac-Toe =====")
    while True:
        # Initialize board
        board = [[str(3 * j + i + 1) for i in range(3)] for j in range(3)]
        display_board(board)
        
        # Toss to decide first player
        result = toss()
        #print(f"Toss Winner: {result['toss_winner']}")
        print(f"You: {result['user']} | Opponent: {result['opponent']}")

        for i in range(9):
            if result['game_opponent'] == "COMPUTER":  # COMPUTER mode
                if result['next_player'] == "COMPUTER":
                    computer_move(board, result['opponent'])
                    print(f"You: {result['user']} | Computer: {result['opponent']}")

                    if check_winner(board, result['computer']):
                        print("🎉 Computer Won! 🎉")
                        break
                    result['next_player'] = "USER"
                else:
                    user_move(board, result['user'])
                    print(f"You: {result['user']} | Computer: {result['opponent']}")

                    if check_winner(board, result['user']):
                        print("🎉 You Won! 🎉")
                        break
                    result['next_player'] = "COMPUTER"
            else:  # FRIEND mode
                if result['next_player'] == "FRIEND":
                    friend_move(board, result['opponent'])
                    print(f"You: {result['user']} | Friend: {result['opponent']}")

                    if check_winner(board, result['opponent']):
                        print("🎉 Friend Won! 🎉")
                        break
                    result['next_player'] = "USER"
                else:
                    user_move(board, result['user'])
                    print(f"You: {result['user']} | Friend: {result['opponent']}")

                    if check_winner(board, result['user']):
                        print("🎉 You Won! 🎉")
                        break
                    result['next_player'] = "FRIEND"
        else:
            print("It's a draw! 🤝")

        if input("Do you want to play again? (Y/N): ").strip().upper() != "Y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()



