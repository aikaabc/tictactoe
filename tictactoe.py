from IPython.display import clear_output
import random

print('Welcome to Tic Tac Toe! ')
the_board = [' '] * 10


def display_board(board):
    clear_output()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range (1,10):
        if space_check(board, i):
            return False
    # board is full if we return True
    return False


def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def player_input():

    '''
    OUTPUT = (Player 1 name, Player 2 name)
    '''

    name = ''
    while name != 'X' and name != 'O':
    # while not name == 'X' or name == 'O':
        name = input('Player 1, please choose X or O :').upper()

    player1 = name

    if player1 == 'X':
        player2 = 'O'
        return ('X', 'O')
    else:
        player2 = 'X'
        return ('O', 'X')

# player1_name, player2_name = player_input()

def place_name(board, name, position):
    board[position] = name


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: from 1 to 9 '))


def win_check(board, name):
    return ((board[1] == board[2] == board[3] == name) or
    (board[4] == board[5] == board[6] == name) or
    (board[7] == board[8] == board[9] == name) or
    (board[1] == board[4] == board[7] == name) or
    (board[2] == board[5] == board[8] == name) or
    (board[3] == board[6] == board[9] == name) or
    (board[1] == board[5] == board[9] == name) or
    (board[3] == board[5] == board[7] == name))


def replay():
    choice = input('Do you want to play again?Enter Yes or No ')
    return choice == 'Yes'

while True:
    ''' set everything up: BOARD, WHO IS FIRST, CHOOSE NAMES (X,O)'''
    the_board = [' '] * 10
    player1_name, player2_name = player_input()

    turn = choose_first()
    print(turn + 'will go first!')

    play_game = input('Ready to play? Yes or No? ')

    if play_game == 'Yes':
        game_on =True
    else:
        game_on = False


    while game_on:
        if turn == 'Player 1':
            display_board(the_board) # show the board
            position = player_choice(the_board) #choose a position
            place_name(the_board, player1_name, position)  #place the name on the position (x, o)

            if win_check(the_board, player1_name): # check if they won
                display_board(the_board)
                print('PLAYER 1 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'

            # check if there is a tie
            # no tie and no win then next player's turn
        else:
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the name on the position (x, o)
            place_name(the_board, player2_name, position)
            # check if the won
            if win_check(the_board, player2_name):
                display_board(the_board)
                print('PLAYER 2 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False

    if not replay():
        break

