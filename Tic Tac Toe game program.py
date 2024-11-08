def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Row 1
        [board[1][0], board[1][1], board[1][2]],  # Row 2
        [board[2][0], board[2][1], board[2][2]],  # Row 3
        [board[0][0], board[1][0], board[2][0]],  # Column 1
        [board[0][1], board[1][1], board[2][1]],  # Column 2
        [board[0][2], board[1][2], board[2][2]],  # Column 3
        [board[0][0], board[1][1], board[2][2]],  # Diagonal 1
        [board[2][0], board[1][1], board[0][2]]   # Diagonal 2
    ]
    return [player, player, player] in win_conditions

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    for _ in range(9):
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")

        while True:
            try:
                row, col = map(int, input("Enter row and column (0, 1, 2) separated by space: ").split())
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Cell already taken. Choose another.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
        
        turn += 1

    print_board(board)
    print("It's a tie!")

tic_tac_toe()
