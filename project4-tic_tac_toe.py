def print_board(board):
    """Prints the current state of the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Checks if the given player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    """Checks if the game is a draw."""
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_index = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        current_player = players[current_player_index]
        print(f"Player {current_player}'s turn.")

        # Get valid input
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column numbers between 1 and 3, separated by space): ").split())
                row -= 1
                col -= 1
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell is already occupied. Choose another cell.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers between 1 and 3.")

        print_board(board)

        # Check for win or draw
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # Switch to the next player
        current_player_index = 1 - current_player_index


if __name__ == "__main__":
    tic_tac_toe()