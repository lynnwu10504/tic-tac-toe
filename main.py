import os

static_position = [['1', '2', '3'],
                   ['4', '5', '6'],
                   ['7', '8', '9']]

art = '''
  _______ _        _______           _______         
 |__   __(_)      |__   __|         |__   __|        
    | |   _  ___     | | __ _  ___     | | ___   ___ 
    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\
    | |  | | (__     | | (_| | (__     | | (_) |  __/
    |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|

'''

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

player_1_position = []
player_2_position = []

final_position = ''
winner = ''


def print_board(board):
    print("-------------")
    print("| {} | {} | {} |".format(board[0][0], board[0][1], board[0][2]))
    print("-------------")
    print("| {} | {} | {} |".format(board[1][0], board[1][1], board[1][2]))
    print("-------------")
    print("| {} | {} | {} |".format(board[2][0], board[2][1], board[2][2]))
    print("-------------")


def get_position(player_number):
    global final_position
    while final_position == '':
        try:
            player_input = int(input(f"Player {player_number}, which position? "))
        except ValueError:
            print("Please enter an integer")
        else:
            if player_input > 9 or player_input < 0:
                print("Please enter a valid position")
            elif player_input in player_1_position or player_input in player_2_position:
                print("This position has been chosen before. Choose another position.")
            else:
                final_position = player_input
                if player_number == 1:
                    player_1_position.append(final_position)
                else:
                    player_2_position.append(final_position)


def place_shape(position, shape):
    mapping = {1: [0, 0], 2: [0, 1], 3: [0, 2],
               4: [1, 0], 5: [1, 1], 6: [1, 2],
               7: [2, 0], 8: [2, 1], 9: [2, 2]}
    board[mapping[position][0]][mapping[position][1]] = shape
    print_board(board)


def check_winner(board, shape):
    global winner
    count = 0
    # check row
    for row in board:
        if row.count(shape) == 3:
            winner = shape

    # check columns
    for col in range(3):
        if all(board[row][col] == shape for row in range(3)):
            winner = shape

    # check for diagonals
    if all(board[i][i] == shape for i in range(3)) or all(board[i][2-i] == shape for i in range(3)):
        winner = shape

    for row in board:
        count += row.count('X')
        count += row.count('O')
    if count == 9:
        winner = "draw"

    return False


def alternate_lists():
    while True:
        yield [1, 'X']
        yield [2, 'O']


alternator = alternate_lists()

is_restart = "Y"
while is_restart == "Y":
    print(art)
    print("Welcome to the Tic Tae Toe game! Player 1 will play 'X' and Player 2 will play 'O'. "
          "When it's your turn, enter the position (1 to 9 as shown below)")
    print_board(static_position)
    print("Ok, let's get started!")

    while winner == '':
        first_list = next(alternator)
        get_position(first_list[0])
        place_shape(final_position, first_list[1])
        final_position = ''
        check_winner(board, first_list[1])

    if winner == 'X' or winner == 'O':
        is_restart = input(f"Congrats Player {first_list[0]}! You won!\nRestart the game? Enter 'Y' or 'N'")
    elif winner == 'draw':
        is_restart = input("It's a draw! Restart the game? Enter 'Y' or 'N'")
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    player_1_position = []
    player_2_position = []

    final_position = ''
    winner = ''
    os.system('clear')