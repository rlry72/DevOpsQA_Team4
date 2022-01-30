from email.policy import default
import pytest
import os
from classes.game import *
from classes.menu import *
from classes.building import *
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
import sys
from unittest.mock import Mock


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
    "  +-----+-----+-----+-----+",
]

gameBoardPlaced = [
    "     A     B     C     D  ",
    "  +-----+-----+-----+-----+",
    " 1| SHP |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 2|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 3|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+",
]

gameMenu = ['1. Build a SHP',
            '2. Build a SHP', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

def test_build_a_building():
    """
    Test script to test Building a building from the game menu
    """
    set_keyboard_input(["1","a1","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "SHP"], "2": ["SHP", "SHP"]}
    test_game.building_pool = defaultBuildingPool
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1"] + gameBoard + gameMenu + ["Build where? ", "", "Turn 2"] + gameBoardPlaced + gameMenu


@pytest.mark.parametrize("invalidInput",
[(["1","2a","0"]), (["1","a","0"]), (["1","","0"])])
def test_build_a_building_invalid_input(invalidInput):
    """
    Test Script to test Invalid input when building from game menu
    """
    set_keyboard_input(invalidInput)
    test_game = Game()
    test_game.building_pool = defaultBuildingPool
    test_game.randomized_building_history = {"1": ["SHP", "SHP"], "2": ["SHP", "SHP"]}
    test_game.start_new_turn()
    result = get_display_output()

    assert result == ["","Turn 1"] + gameBoard + gameMenu + ["Build where? ",
    "Your input is invalid, please follow 'letter' + 'digit' format to input for location.",
    "", "Turn 1"] + gameBoard + gameMenu



def test_build_a_building_invalid_location():
    """
    Test Script to test Invalid location for building
    """
    set_keyboard_input(["1","a1","1","c4","0"])
    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "SHP"], "2": ["SHP", "SHP"]}
    test_game.building_pool = defaultBuildingPool
    test_game.start_new_turn()
    result = get_display_output()

    assert result == ["","Turn 1"] + gameBoard +gameMenu + ["Build where? ","","Turn 2"] + gameBoardPlaced + gameMenu + ["Build where? ",
    "You must build next to an existing building.", "", "Turn 2"] + gameBoardPlaced + gameMenu



def test_build_a_building_build_on_existing_building():
    """
    Test script to test building on existing building
    """
    set_keyboard_input(["1","a1","1","a1","0"])
    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "SHP"], "2": ["SHP", "SHP"]}
    test_game.building_pool = defaultBuildingPool
    test_game.start_new_turn()
    result = get_display_output()


    assert result == ["","Turn 1"] + gameBoard +gameMenu + ["Build where? ","","Turn 2"] + gameBoardPlaced + gameMenu + ["Build where? ",
    "You cannot build on a location that has already had a building", "", "Turn 2"] + gameBoardPlaced + gameMenu
    