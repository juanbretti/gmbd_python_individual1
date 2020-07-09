"""
@author: Juan Pedro Bretti Mandarano
GMBD, Intake 2020
2020/07/09

Main code to run the game.
"""

# Import the libraries
from mypackage import demo as aux_functions

# Constants
MS = PS = 0
xi = 1234
# Game select options
game_levels = {1: 'Easy', 2: 'Difficult'}
game_numbers = (0, 1)
# Initialize the previous throw counters
throw00 = throw01 = throw10 = throw11 = 0
player_move_previous = None

# Create opening message
print('Welcome to Human Behavior Prediction by Juan Pedro Bretti Mandarano')
# Set up the game size
select_difficulty = aux_functions.read_int(possible=game_levels,
                                           message_try='Choose the type of game %s: ' % ('(' + ', '.join('{}: {}'.format(k, v) for k, v in game_levels.items()) + ')',),
                                           message_error='Only accepts the values %s, try again.' % (tuple(game_levels.keys()),)
                                           )
moves = aux_functions.read_positive(message_try='Enter the number of moves: ',
                                    message_error='Only accepts positive integers, try again.'
                                    )

for turn in range(moves):

    # Capture moves
    # As per assignment, the computer move is calculated before the player and even if is not necessary
    pre_computer_move, xi = aux_functions.linear_congruence(xi)
    player_move = aux_functions.read_int(possible=game_numbers,
                                         message_try='Choose your move number %s %s: ' % (turn + 1, game_numbers),
                                         message_error = 'Only accepts the values %s, try again.' % (game_numbers,)
                                         )

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

    # Computer again depending of the difficulty
    if select_difficulty == 1:
        # Easy game
        computer_move = pre_computer_move
    else:
        # Difficult game
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

# Print Final score
if PS > MS:
    print('%s game is over, final score: player %d - %d computer - You won!' % (game_levels[select_difficulty], PS, MS))
elif PS < MS:
    print('%s game is over, final score: player %d - %d computer - Computer won!' % (game_levels[select_difficulty], PS, MS))
else:
    print('%s game is over, final score: player %d - %d computer - It was a tie!' % (game_levels[select_difficulty], PS, MS), '\n', 'Play against the computer and see if you are able to beat it!', sep='')