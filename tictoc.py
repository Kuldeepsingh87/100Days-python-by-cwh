# Tic-Tac-Toe Game (2 Players)

def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    
    for turn in range(9):
        print_board(board)
        
        try:
            move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
        except ValueError:
            print("Invalid input! Try again.")
            continue
        
        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move! Try again.")
            continue
        
        board[move] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            return
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"
    
    print_board(board)
    print("🤝 It's a draw!")


tic_tac_toe()