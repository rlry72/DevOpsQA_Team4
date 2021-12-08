import pytest
from tud_test_base import set_keyboard_input, get_display_output
from classes.menu import *
from classes.game import *


def test_game_menu_display_turn_number():
    """
    Tests if the turn number is displayed properly upon starting a new game
    Starts a new game and checks the game output against what the proper output should be.
    """
    # set input 0, but first input will be ignored.
    set_keyboard_input(["0"])
    # start new game and turn
    test_game = Game().start_new_turn()
    # get what is printed in the console
    result = get_display_output()[0]
    
    # compares what is printed in console with what should be shown. if different, test fails.
    assert result == "Turn 1"


def test_game_menu_display_turn_number_2():
    """
    Tests if turn number 2 is displayed properly upon starting a new game
    Starts a new game, build a building and start the next turn and checks the game output against what the proper output should be.
    """
    # set input 1, a1, 0, but first input will be ignored.
    set_keyboard_input(["1", "a1", "0"])
    # start new game and turn
    test_game = Game().start_new_turn()
    # when input reaches "a1" (build building on a1)
    if (test_game == "a1"):
        # get what is printed in the console (first thing that should be printed in console when this option is input should be "Turn 2")
        result = get_display_output()[0]
        # compares what is printed in console with what should be shown. if different, test fails.
        assert result == "Turn 2"


def test_game_menu_display_turn_number_4():
    """
    Tests if turn number 2 is displayed properly upon starting a new game
    Starts a new game, build a building and start the next turn and checks the game output against what the proper output should be.
    """
    # set input 1, a1, 0, but first input will be ignored.
    set_keyboard_input(["1", "a1", "2", "a2", "1", "b2", "0"])
    # start new game and turn
    test_game = Game().start_new_turn()
    # when input reaches "b2" (build building on b2)
    if (test_game == "b2"):
        # get what is printed in the console (first thing that should be printed in console when this option is input should be "Turn 4")
        result = get_display_output()[0]
        # compares what is printed in console with what should be shown. if different, test fails.
        assert result == "Turn 4"