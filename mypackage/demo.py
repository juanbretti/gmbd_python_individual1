"""
@author: Juan Pedro Bretti Mandarano
IE, GMBD, Intake 2020
2020/07/19

Additional functions for the 'Human Behavior Prediction' application.
"""


# Import the libraries
from art import *  # Library for big fonts


# Color constants for the console
color_constant = {'input': '\033[94m', 'warning': '\033[93m', 'error': '\033[91m', 'end': '\033[0m'}


def clear_console(n=50):
    """
    Function to clear the Python console, by printing in the console 'new line'.
    This behavior is similar to Linux command 'clear'.
    :param n: Number of rows to enter a 'new line'.
    :type n: int
    :return: None
    """

    for i in range(n):
        print('\n')

    return None


def linear_congruence(xi):
    """
    Function to calculate linear congruences value and computer bet.
    :param xi: Seed.
    :type xi: int
    :return: Computer moves between (0, 1), Seed.
    :rtype: list
    """

    a = 22695477
    b = 1
    m = 2**32
    xi_plus_1 = (a * xi + b) % m
    if xi_plus_1 <= 2**31:
        comp_move = 0
    else:
        comp_move = 1
    return comp_move, xi_plus_1


def read_possible(possible, message_try='Type a value', message_error='Error', color='input'):
    """
    Function to read integer number only, inside the listed possibles values.
    :param possible: Possible values to be input by the user.
    :type possible: tuple, dict
    :param message_try: Message to display when requesting the input from the user.
    :type message_try: str
    :param message_error: Message to display when the user inputs something outside the possible values.
    :type message_error: str
    :param color: Color for the input, based on 'color_constant'
    :type color: str
    :return: User input value.
    :rtype: int
    """

    # Loop until the user enters a value in the possibles
    correct_value = False
    while not correct_value:
        try:
            user_value = int(input(color_constant[color] + message_try + color_constant['end']))
            if user_value in possible:
                correct_value = True
            else:
                raise ValueError
        except ValueError:
            correct_value = False
            print(color_constant['error'] + message_error + color_constant['end'])

    return user_value


def read_positive(message_try='Type a value', message_error='Error', color='input'):
    """
    Function to read only natural numbers (positive integers excluding 0).
    :param message_try: Message to display when requesting the input from the user.
    :type message_try: str
    :param message_error: Message to display when the user inputs something outside the possible values.
    :type message_error: str
    :param color: Color for the input, based on 'color_constant'
    :type color: str
    :return: User input value.
    :rtype: int
    """

    # Loop until the user enters a value in the possibles
    correct_value = False
    while not correct_value:
        try:
            user_value = int(input(color_constant[color] + message_try + color_constant['end']))
            if user_value > 0:
                correct_value = True
            else:
                raise ValueError
        except ValueError:
            correct_value = False
            print(color_constant['error'] + message_error + color_constant['end'])

    return user_value


def run_game(xi, player_throw, player_move_previous, game_levels, game_numbers):
    """
    Based on the assignment, follows the rules on how the game should work.
    :param xi: Seed.
    :type xi: int
    :param player_throw: Array containing previous throw from the player.
    :type player_throw: array
    :param player_move_previous: Last move from the player.
    :type player_move_previous: int
    :param game_levels: Possible game levels, i.e. Easy and Difficult.
    :type game_levels: dict
    :param game_numbers: Options to select from.
    :type game_numbers: tuple
    :return: Seed, Player throw array, Player previous move
    :rtype: tuple
    """

    # Set up the game size
    select_difficulty = read_possible(possible=game_levels,
                                      message_try='Choose the type of game %s: ' % (
                                          '(' + '; '.join('{}: {}'.format(k, v) for k, v in game_levels.items()) + ')',),
                                      message_error='Only accepts the values %s, try again.' % (tuple(game_levels.keys()),)
                                      )
    select_moves = read_positive(message_try='Enter the number of moves: ',
                                 message_error='Only accepts positive integers, try again.'
                                 )
    # Restart the win game's counters
    MS = PS = 0

    # Repeat the runs as many times as moves input at 'select_moves'
    for turn in range(select_moves):

        # Separator
        print('\n'*2)
        tprint('Move # {}'.format(turn + 1), "Standard")

        # Capture moves
        # As per assignment, the computer move is calculated before the player and even if is not necessary
        computer_move_pre, xi = linear_congruence(xi)
        # Captures player move
        player_move = read_possible(possible=game_numbers,
                                    message_try='Choose your move number %s %s: ' % (
                                        turn + 1, '(' + ' or '.join('{}'.format(x) for x in game_numbers) + ')'),
                                    message_error='Only accepts the values %s, try again.' % (game_numbers,)
                                    )

        # Computer again depending of the difficulty
        if select_difficulty == 1:  # Easy game
            computer_move = computer_move_pre
        elif select_difficulty == 2:  # Difficult game
            if player_move_previous is not None and player_throw.sum() > 0:  # After two game (checking if there is any previous player_throw).
                # Computer choice considering previous human move
                if player_move_previous == 0:
                    if player_throw[1, 0] > player_throw[0, 0]:
                        computer_move = 1
                    elif player_throw[1, 0] < player_throw[0, 0]:
                        computer_move = 0
                    else:
                        computer_move = computer_move_pre
                else:
                    if player_throw[1, 1] > player_throw[0, 1]:
                        computer_move = 1
                    elif player_throw[1, 1] < player_throw[0, 1]:
                        computer_move = 0
                    else:
                        computer_move = computer_move_pre
            else:  # The first time
                computer_move = computer_move_pre  # Considering random previous move from the user

        # Stores the moves in an np.array
        if player_move_previous is not None:  # The first time
            player_throw[player_move, player_move_previous] += 1
        # Record the previous move from the player
        player_move_previous = player_move

        # Game result
        if player_move == computer_move:
            MS = MS + 1
            print('Player move {} and Computer move {} > Computer wins!'.format(player_move, computer_move))
        else:
            PS = PS + 1
            print('Player move {} and Computer move {} > Player wins!'.format(player_move, computer_move))
        # print('You: %d Computer: %d' % (PS, MS))

        # Summary of all the moves
        print('PARTIAL SCORE:')
        print('  PLAYER: ' + '*' * PS)
        print('  COMPUTER: ' + '*' * MS)

    # Print Final score
    print('\n' * 2)
    if PS > MS:
        tprint('You won!', "Standard")
        print('%s game is over, final score: player %d - %d computer' % (
              game_levels[select_difficulty], PS, MS))
    elif PS < MS:
        tprint('Computer won!', "Standard")
        print('%s game is over, final score: player %d - %d computer' % (
              game_levels[select_difficulty], PS, MS))
    else:
        tprint('It was a tie!', "Standard")
        print('%s game is over, final score: player %d - %d computer' % (
              game_levels[select_difficulty], PS, MS))
    print('\n')

    return xi, player_throw, player_move_previous
