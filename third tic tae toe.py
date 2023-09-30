import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def player_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (e.g., 1 2): ").split())
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == ' ':
                board[row - 1][col - 1] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter row and column as numbers (e.g., 1 2).")

def computer_move(board, computer):
    empty_cells = get_empty_cells(board)
    row, col = random.choice(empty_cells)
    board[row][col] = computer

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = random.choice(players)
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        if current_player == 'X':
            player_move(board, current_player)
        else:
            computer_move(board, current_player)
        
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break
        
        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    main()
