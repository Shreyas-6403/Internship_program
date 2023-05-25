# 2 Player Tic Tac Toe game

def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def get_player_move(board, player):
    while True:
        row = int(input("Enter row (1-3) for player {}: ".format(player)))
        col = int(input("Enter column (1-3) for player {}: ".format(player)))
        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Invalid input. Please enter row and column values between 1 and 3.")
        elif board[row-1][col-1] != " ":
            print("That spot is already taken. Please choose another spot.")
        else:
            board[row-1][col-1] = player
            break

def is_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    for row in board:
        for spot in row:
            if spot == " ":
                return False
    return True

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"]
    current_player = players[0]
    draw_board(board)
    while True:
        get_player_move(board, current_player)
        draw_board(board)
        if is_winner(board, current_player):
            print("Player {} wins!".format(current_player))
            break
        elif is_board_full(board):
            print("Tie!")
            break
        current_player = players[(players.index(current_player)+1) % 2]
    return play_again()

#Additional Feature :)

def play_again():
    while True:
        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again == 'y':
            return True
        elif play_again == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

while play_game():
    pass
