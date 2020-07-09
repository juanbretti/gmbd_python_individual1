"""
@author: Juan Pedro Bretti Mandarano
GMBD, Intake 2020
2020/07/09

Additional functions for the 'Human Behavior Prediction' application.
"""


def linear_congruence(xi):
    """
    Function to calculate linear congruences value and computer bet.
    :param int xi: Seed.
    :return: Computer move between (0, 1), Seed
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


def read_int(possible, message_try='Type a value', message_error='Error'):
    """
    Function to read integer number only, inside the listed possibles.
    :param tuple-dict possible: Possible values to be input by the user.
    :param str message_try: Message to display when requesting the input from the user.
    :param str message_error: Message to display when the user inputs something outside the possible values.
    :return: User input value
    """

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


def read_positive(message_try='Type a value', message_error='Error'):
    """
    Function to read only natural numbers (positive integers excluding 0).
    :param str message_try: Message to display when requesting the input from the user.
    :param str message_error: Message to display when the user inputs something outside the possible values.
    :return: User input value
    """

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