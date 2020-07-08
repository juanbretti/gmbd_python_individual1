"""
@author: Juan Pedro Bretti Mandarano
Using PyCharm as IDE, that's why I need to address the complete path to the package.
"""
# Import the libraries
from IndividualAssignment1.Delivery.mypackage import demo as aux_functions

# Create opening message
print('Welcome to Human Behavior Prediction by Juan Pedro Bretti Mandarano')

select_difficulty = aux_functions.read_int('Chose the type of game (1: Easy; 2: Difficult): ')
# TODO: correct to write only numbers 1 or 2 only

moves = aux_functions.read_int('Enter the number of moves: ')

MS = 0
PS = 0
xi = 1234

# Initialize the previous throw counters
throw00 = throw01 = throw10 = throw11 = 0
player_move_previous = None

if select_difficulty == 1:
    for turn in range(moves):
        # Capture moves
        computer_move, xi = aux_functions.linear_congruence(xi)
        player_move = aux_functions.read_move('Chose your move number (0 or 1): ')
        # Game result
        if player_move == computer_move:
            MS = MS + 1
            print('player = 0 machine = 0 - Machine wins!')
            print('You: %d Computer: %d' % (PS, MS))
        else:
            PS = PS + 1
            print('player = 1 machine = 0 - Player wins!')
            print('You: %d Computer: %d' % (PS, MS))

        # Summary of all the moves
        print('PLAYER: ' + '*' * PS)
        print('COMPUTER: ' + '*' * MS)

elif select_difficulty == 2:
    for turn in range(moves):

        # Capture moves
        # As per assignment, the computer move is calculated before the player and even if is not necessary
        pre_computer_move, xi = aux_functions.linear_congruence(xi)
        player_move = aux_functions.read_move('Chose your move number (0 or 1): ')

        # Counters of previous movements
        if player_move_previous is None:
            pass
        elif player_move == 0 and player_move_previous == 0:
            throw00 += 1
        elif player_move == 0 and player_move_previous == 1:
            throw01 += 1
        elif player_move == 1 and player_move_previous == 0:
            throw10 += 1
        elif player_move == 1 and player_move_previous == 1:
            throw11 += 1
        else:
            pass
        player_move_previous = player_move

        # Computer choice considering previous human move
        if player_move_previous == 0:
            if throw10 > throw00:
                computer_move = 1
            elif throw10 < throw00:
                computer_move = 0
            else:
                computer_move = pre_computer_move
        else:
            if throw11 > throw01:
                computer_move = 1
            elif throw11 < throw01:
                computer_move = 0
            else:
                computer_move = pre_computer_move

        # Game result
        if player_move == computer_move:
            MS = MS + 1
            print('player = 0 machine = 0 - Machine wins!')
            print('You: %d Computer: %d' % (PS, MS))
        else:
            PS = PS + 1
            print('player = 1 machine = 0 - Player wins!')
            print('You: %d Computer: %d' % (PS, MS))

        # Summary of all the moves
        print('PLAYER: ' + '*' * PS)
        print('COMPUTER: ' + '*' * MS)

# Final score
if PS > MS:
    print('Easy game is over, final score: player 3 - 1 computer - You won!')
elif PS < MS:
    print('Easy game is over, final score: player 3 - 1 computer - Computer won!')
else:
    print('Easy game is over, final score: player 3 - 1 computer - It was a tie!', '\n', 'Play against the computer and see if you are able to beat it!', sep='')