import pytest
import os
from classes.game import *
from classes.menu import *
from main import *
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
import sys
from unittest.mock import Mock
import classes
pytestmark = pytest.mark.skipif("generate_remaining_building_string" in dir(classes.game.Game), reason="view remaining buildings on side implemented")

mainMenu = ["Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
    "Your choice? "]

invalidInputList = [
    "Invalid input, please try again",
    "Your choice? "]

turnNumber = ["", "Turn 1"]

gameBoard = [
    "     A     B     C     D  ",
    "  +-----+-----+-----+-----+",
    " 1|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 2|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 3|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

gameMenu = ['1. Build a HSE',
            '2. Build a HSE', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']


def test_main_menu_to_game_menu():
    """
    Test script test going to main menu from game menu
    """
    set_keyboard_input(["1","0","0"])

    expectedResult = [
    "     A     B     C     D  ",
    "  +-----+-----+-----+-----+",
    " 1|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 2|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 3|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+", 
    '3. See remaining buildings',
    '4. See current score',
    '', 
    '5. Save game', 
    '0. Exit to main menu', 
    'Your choice? ']

    with pytest.raises(SystemExit) as e:
        main()

    result = get_display_output()
    check =  all(item in result for item in expectedResult)

    assert check == True



def test_main_menu():
    """
    Test script to test main menu output
    """
    set_keyboard_input(["0"])
    with pytest.raises(SystemExit) as e:
        main()
    result = get_display_output()

    assert result == mainMenu



@pytest.mark.parametrize("invalidInput", 
[("-1"), ("asdf"), 
("13@!$`a"), (9), ("")])
def test_main_menu_invalid_input(invalidInput):
    """
    Test script to test invalid input in main menu
    """
    set_keyboard_input([invalidInput,"0"])
    with pytest.raises(SystemExit) as e:
        main()
    result = get_display_output()

    assert result == mainMenu + invalidInputList