
























from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''

    while marker!='X' or marker!='O':
        marker = input('Wanna play!,choose X or O: ')

        if marker == 'X':
            return ('X','O')
        else:
            return('O','X')

    return marker
    
def place_marker(board,position,marker):
    board[position]=marker

##winning function

def win_check(board, mark):
 # win Tic Tac Toe
   return((board[1]==board[2]==board[3]==mark)or
    (board[4]==board[5]==board[6]==mark)or ##(all rows, check to see if they have the same marker)
    (board[7]==board[8]==board[9]==mark)or
    (board[1]==board[4]==board[7]==mark)or
    (board[2]==board[5]==board[8]==mark)or # all coloumns, check to see if the marker matches
    (board[3]==board[6]==board[9]==mark)or
    (board[1]==board[5]==board[9]==mark)or
    (board[7]==board[5]==board[3]==mark)) # two diagonals

 # two diagonalsY

#choosing who will play first using randint

def choose_first():
    import random
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    

# check wheter there is enough space or not in the board
def space_check(board,position):
    return board[position]== " "


#checking if the board is full or not

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
              
    return True
        
 # ask for players next position       
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9,10] or not space_check(board,position):
        position = int(input('Please choose a position (1-9): '))
    return position

# ask if wanna play again
def replay():
    choice = input('Wanna play again, Yes or No')
    return choice == 'y'




print('welcome to tic tac toe')

while True:

    the_board = [' ']*10
    player1_marker ,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + 'will play first') 

    play_game = input("Ready to play the game? y or n? ")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,position,player1_marker)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on=False
                else:
                    turn = 'PLAYER 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,position,player2_marker)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on=False
                else:
                    turn = 'PLAYER 1'
                
    if not replay():
             break



             