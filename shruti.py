def check_winner(board):
    lines = [
        board[0] + board[1] + board[2],
        board[3] + board[4] + board[5],
        board[6] + board[7] + board[8],
        board[0] + board[3] + board[6],
        board[1] + board[4] + board[7],
        board[2] + board[5] + board[8],
        board[0] + board[4] + board[8],
        board[2] + board[4] + board[6],
    ]

    for line in lines:
        if line == "xxx":
            return "x"
        elif line == "000":
            return "0"
    if all(spot in ['x', '0'] for spot in board ):
            return "draw"
    return None

def print_board(board):
    print("|---|---|---|")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("|-----------|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("|-----------|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("|---|---|---|")

def main():
    board = [str(i+1) for i in range(9)]
    turn = "x"
    winner = None

    print("welcome to 3x3 tic tac toe.")
    print_board(board)

    print("x will play first. enter a slot no. to place{turn} in:")
    
    while winner is None:
        try:
            num_input = int(input(f"{turn}'s turn; enter a slot no. to place {turn} in:"))
            if num_input < 1 or num_input > 9:
                print("Invalid input; re-enter slot no.:")
                continue
        except ValueError:
            print("Invalid input; re-enter")
            continue
        
        if board[num_input - 1] == str(num_input):
            board[num_input - 1] = turn 
            turn = "0" if turn == "x" else "x"
            print_board(board)
            winner = check_winner(board)
        else:
            print("slot already taken; re-enter:")
            
    if winner == "draw":
        print("Draw! Thanks for playing:")
    else:
        print("congratulations!{winner} has won!")

if __name__ == "__main__":
    main()

        

