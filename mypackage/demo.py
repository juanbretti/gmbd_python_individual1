"""
@author: Juan Pedro Bretti Mandarano

Functions for the 'Human Behavior Prediction' application
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

# TODO define a max
def read_int(message):
    """
    Function to read integer number only.
    Careful, the function truncate if the users inputs a number with decimals.
    """

    ok2go = False
    while not ok2go:
        try:
            c_int = int(input(message))
            ok2go = True
        except:
            ok2go = False
    return c_int


# TODO player_move = int(input('Chose your move number %s (0 or 1): ' % (turn + 1)))
# https://stackoverflow.com/a/6983076/3780957


def read_move(message='Chose your move number (0 or 1): '):
    """
    Function to read only integers 0 and 1.
    It shows in the message the number of turn
    Careful, the function truncate if the users inputs a number with decimals.
    """

    ok2go = False
    while not ok2go:
        try:
            c_int = int(input(message))
            if c_int in range(0, 2):
                ok2go = True
            else:
                ok2go = False
        except:
            ok2go = False
    return c_int