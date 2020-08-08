"""
@author: Juan Pedro Bretti Mandarano
IE, GMBD, Intake 2020
2020/07/19

Main code to run the game.
"""

# Import the libraries
from mypackage import demo as aux_functions
import numpy as np
from art import *

# Create opening message
aux_functions.clear_console()
tprint("Welcome to\nHuman Behavior Prediction\nby Juan Pedro Bretti","Standard")

# Game select options
game_levels = {1: 'Easy', 2: 'Difficult'}
game_continue = {1: 'Continue', 2: 'Exit'}
game_numbers = (0, 1)  # Options to select from

# Initialize the previous throw counters
player_throw = np.zeros(4).reshape(2, 2)  # 1 dimension (row): current throw, 2 dimension (column): previous throw
player_move_previous = None  # Previous move from the player
select_continue = 1  # Start the game
xi = 1234  # Random seed provided by the professor

# Infinite loop, will stop the game by pressing Ctrl+C or selecting 'Exit' when prompt
while select_continue == 1:

    # Run the game
    xi, player_throw, player_move_previous = aux_functions.run_game(xi, player_throw, player_move_previous, game_levels, game_numbers)

    # Prompt the user to continue or stop the infinite rounds
    select_continue = aux_functions.read_possible(possible=game_continue,
                                                  message_try='Want to keep playing %s?: ' % (
                                                    '(' + '; '.join('{}: {}'.format(k, v) for k, v in game_continue.items()) + ')',),
                                                  message_error='Only accepts the values %s, try again.' % (
                                                    tuple(game_continue.keys()),),
                                                  color='warning'
                                                  )

    # Clear console for the new game
    if select_continue == 1:
        aux_functions.clear_console()
        tprint("Human Behavior Prediction", "Standard")
