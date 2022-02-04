from email.policy import default
import pytest
import os
import classes
from classes.game import *
from classes.menu import *
from classes.building import *
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
import sys
from unittest.mock import Mock

pytestmark = pytest.mark.skipif("generate_remaining_building_string" not in dir(classes.game.Game), reason="view remaining buildings on side not implemented")

gameBoard = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1|     |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+        HWY      | 8",
    " 3|     |     |     |     |        BCH      | 8",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

gameBoardMONPRK = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1|     |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+        MON      | 8",
    " 3|     |     |     |     |        PRK      | 8",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

gameBoardPlacedHSE = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1| HSE |     |     |     |        HSE      | 7",
    "  +-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+        HWY      | 8",
    " 3|     |     |     |     |        BCH      | 8",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

gameBoardPlacedFAC = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1| FAC |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+        FAC      | 7",
    " 2|     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+        HWY      | 8",
    " 3|     |     |     |     |        BCH      | 8",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

gameBoardPlaced = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1| SHP |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |        SHP      | 7",
    "  +-----+-----+-----+-----+        HWY      | 8",
    " 3|     |     |     |     |        BCH      | 8",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

gameBoardPlacedHWY = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1| HWY |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+        HWY      | 7",
    " 3|     |     |     |     |        BCH      | 8",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

gameBoardPlacedBCH = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1| BCH |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+        HWY      | 8",
    " 3|     |     |     |     |        BCH      | 7",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]


gameBoardPlacedMON = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1| MON |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+        MON      | 7",
    " 3|     |     |     |     |        PRK      | 8",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

gameBoardPlacedPRK = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1| PRK |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+        MON      | 8",
    " 3|     |     |     |     |        PRK      | 7",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]


gameMenu = ['1. Build a SHP',
            '2. Build a SHP', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']
        
gameMenuFAC = ['1. Build a FAC',
            '2. Build a FAC', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

gameMenuBCH = ['1. Build a BCH',
            '2. Build a BCH', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

gameMenuHWY = ['1. Build a HWY',
            '2. Build a HWY', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

gameMenuHSE = ['1. Build a HSE',
            '2. Build a HSE', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

gameMenuMON = ['1. Build a MON',
            '2. Build a MON', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

gameMenuPRK = ['1. Build a PRK',
            '2. Build a PRK', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']


defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

def test_build_a_building_SHP():
    """
    Test script to test Building a building from the game menu
    """
    set_keyboard_input(["1","a1","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "SHP"], "2": ["SHP", "SHP"]}
    test_game.building_pool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1"] + gameBoard + gameMenu + ["Build where? ", "", "Turn 2"] + gameBoardPlaced + gameMenu

def test_build_a_building_BCH():
    """
    Test script to test Building a beach from the game menu
    """
    set_keyboard_input(["1","a1","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "SHP"], "2": ["SHP", "SHP"]}
    test_game.building_pool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1"] + gameBoard + gameMenuBCH + ["Build where? ", "", "Turn 2"] + gameBoardPlacedBCH + gameMenuBCH

def test_build_a_building_HWY():
    """
    Test script to test Building a highway from the game menu
    """
    set_keyboard_input(["1","a1","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "SHP"], "2": ["SHP", "SHP"]}
    test_game.building_pool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1"] + gameBoard + gameMenuHWY + ["Build where? ", "", "Turn 2"] + gameBoardPlacedHWY + gameMenuHWY

def test_build_a_building_FAC():
    """
    Test script to test Building a factory from the game menu
    """
    set_keyboard_input(["1","a1","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "SHP"], "2": ["SHP", "SHP"]}
    test_game.building_pool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1"] + gameBoard + gameMenuFAC + ["Build where? ", "", "Turn 2"] + gameBoardPlacedFAC + gameMenuFAC

def test_build_a_building_HSE():
    """
    Test script to test Building a house from the game menu
    """
    set_keyboard_input(["1","a1","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "SHP"], "2": ["SHP", "SHP"]}
    test_game.building_pool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1"] + gameBoard + gameMenuHSE + ["Build where? ", "", "Turn 2"] + gameBoardPlacedHSE + gameMenuHSE

def test_build_a_building_MON():
    """
    Test script to test Building a Monument from the game menu
    """
    set_keyboard_input(["1","a1","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["MON", "MON"], "2": ["MON", "MON"]}
    test_game.building_pool = {"HSE":8, "FAC":8, "SHP": 8, "MON":8, "PRK":8}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1"] + gameBoardMONPRK + gameMenuMON + ["Build where? ", "", "Turn 2"] + gameBoardPlacedMON + gameMenuMON

def test_build_a_building_PRK():
    """
    Test script to test Building a Park from the game menu
    """
    set_keyboard_input(["1","a1","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["PRK", "PRK"], "2": ["PRK", "PRK"]}
    test_game.building_pool = {"HSE":8, "FAC":8, "SHP": 8, "MON":8, "PRK":8}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1"] + gameBoardMONPRK + gameMenuPRK + ["Build where? ", "", "Turn 2"] + gameBoardPlacedPRK + gameMenuPRK


@pytest.mark.parametrize("invalidInput",
[(["1","2a","0"]), (["1","a","0"]), (["1","","0"])])
def test_build_a_building_invalid_input(invalidInput):
    """
    Test Script to test Invalid input when building from game menu
    """
    set_keyboard_input(invalidInput)
    test_game = Game()
    test_game.building_pool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}
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
    test_game.building_pool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}
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
    test_game.building_pool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}
    test_game.start_new_turn()
    result = get_display_output()


    assert result == ["","Turn 1"] + gameBoard +gameMenu + ["Build where? ","","Turn 2"] + gameBoardPlaced + gameMenu + ["Build where? ",
    "You cannot build on a location that has already had a building", "", "Turn 2"] + gameBoardPlaced + gameMenu
    