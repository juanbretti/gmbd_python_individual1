myDict = {1: 'Easy', 2: 'Difficult'}

for key, value in myDict.items():
    print("{}: {}".format(key, value))

list(myDict.keys())



'_'.join(x + ': ' + y for x, y in myDict.items())

print('(' + ', '.join('{}: {}'.format(k,v) for k,v in myDict.items()) + ')')


def tet(x):
    """
    The Vehicles object contains lots of vehicles

    Parameters
    ----------
    arg : str
        The arg is used for ...
    *args
        The variable arguments are used for ...
    **kwargs
        The keyword arguments are used for ...

    Attributes
    ----------
    arg : str
        This is where we store arg,
    """

    return x
tet()