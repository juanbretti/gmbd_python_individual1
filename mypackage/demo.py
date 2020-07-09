"""
@author: Juan Pedro Bretti Mandarano
GMBD, Intake 2020
2020/07/09

Additional functions for the 'Human Behavior Prediction' application.
"""


def linear_congruence(xi):
    """
    Function to calculate linear congruences value and computer bet
    """

    a = 22695477
    b = 1
    m = 2 ** 32
    xi_plus_1 = (a * xi + b) % m
    if xi_plus_1 <= 2 ** 31:
        comp_move = 0
    else:
        comp_move = 1
    return comp_move, xi_plus_1


def read_int(possible, move=None):
    """
    Function to read integer number only, inside the listed possibles.
    possible: Tuple with possible values to be input by the user.
    move: If move is set, then prints the 'move' number.
    """

    # Messages
    if move is not None:
        message_try = 'Choose your move number %s %s: ' % (move + 1, possible)
        message_error = 'Only accepts the values %s, try again.' % (possible,)
    else:
        message_try = 'Choose the type of game %s: ' % ('(' + ', '.join('{}: {}'.format(k, v) for k, v in possible.items()) + ')',)
        message_error = 'Only accepts the values %s, try again.' % (tuple(possible.keys()),)

    # Loop until the user enters a value in the possibles
    correct_value = False
    while not correct_value:
        try:
            user_value = int(input(message_try))
            if user_value in possible:
                correct_value = True
            else:
                raise ValueError
        except ValueError:
            correct_value = False
            print(message_error)

    return user_value


def read_positive():
    """
    Function to read only natural numbers (positive integers excluding 0).
    No additional arguments has to be defined.
    """

    # Messages
    message_try = 'Enter the number of moves: '
    message_error = 'Only accepts positive integers, try again.'

    # Loop until the user enters a value in the possibles
    correct_value = False
    while not correct_value:
        try:
            user_value = int(input(message_try))
            if user_value > 0:
                correct_value = True
            else:
                raise ValueError
        except ValueError:
            correct_value = False
            print(message_error)

    return user_value