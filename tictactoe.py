from IPython.display import clear_output
import random


def display_board(board):
    '''This function displays the board using indexing '''
    print('\n' * 100) #to scroll previous board up out of view
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X'] #test board to see if it actually works
display_board(test_board) #call the display_board function


def choose_first():
    '''This function uses random module to randomly decide which player goes first'''
    if random.randint(0, 1) == 0: #we have only 2 players
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    '''This function returns a boolean indicating whether a space on the board is freely available '''
    return board[position] == ' '


def full_board_check(board):
    '''This function checks if the board is full and returns a boolean value.
    True is full, False - otherwise'''
    for i in range (1,10):
        if space_check(board, i):
            return False
    return False


def player_input():
    '''This function asks the player to enter their desirable marker name X or O'''
    name = ''
    while name != 'X' and name != 'O':
    # while not name == 'X' or name == 'O':
        name = input('Player 1, please choose X or O :').upper()

    if name == 'X': #if name X then the Player 1 is x, Player 2 is O
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_name(board, name, position):
    ''' This function takes in the board list object, a name(x or o), and a
    desired position (number 1-9) and assigns it to the board '''
    board[position] = name #when you choose position on a board it releases your name on a board


def player_choice(board):
    '''This function asks for a player's next position(1-9) if it is, then
    return the position for a later use'''
    position = 0 #thus 0 index can not be seen on the board
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: from 1 to 9 '))
    return position  #shows what position they have now


def win_check(board, name):
    '''This function takes in a board and checks if someone has won'''
    return ((board[1] == board[2] == board[3] == name) or
    (board[4] == board[5] == board[6] == name) or
    (board[7] == board[8] == board[9] == name) or
    (board[1] == board[4] == board[7] == name) or
    (board[2] == board[5] == board[8] == name) or
    (board[3] == board[6] == board[9] == name) or
    (board[1] == board[5] == board[9] == name) or
    (board[3] == board[5] == board[7] == name))

# win_check(test_board, 'X')


def replay():
    '''This function asks if the player wants to play again
    and returns boolean True if they do want to play again'''
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

while True:
    # RESET THE BOARD
    theBoard = [' '] * 10
    player1_name, player2_name = player_input()
    turn = choose_first()
    print(turn + 'will go first!')

    play_game = input('Ready to play? Yes or No? ')

    if play_game.lower()[0] == 'y':
        game_on =True
    else:
        game_on = False


    while game_on == True:
        if turn == 'Player 1':
            # Player 1's turn
            display_board(theBoard) # show the board
            position = player_choice(theBoard) #choose a position
            place_name(theBoard, player1_name, position)  #place the name on the position (x, o)

            if win_check(theBoard, player1_name): # check if they won
                display_board(theBoard)
                print('PLAYER 1 HAS WON!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'Player 2'
            # check if there is a tie
            # no tie and no win then next player's turn

        else:
            # PLAYER 2'S TURN
            display_board(theBoard)
            position = player_choice(theBoard)
            place_name(theBoard, player2_name, position)

            if win_check(theBoard, player2_name):
                display_board(theBoard)
                print('PLAYER 2 HAS WON!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

