import pytest
import os
import sys
from unittest.mock import Mock
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
from classes.game import *
from classes.menu import *

defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

gameMenu = ['1. Build a SHP',
            '2. Build a SHP', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

board = [
        "     A     B     C     D           Building   Remaining",
        "  +-----+-----+-----+-----+        --------------------",
        " 1|     |     |     |     |        HSE      | 8",
        "  +-----+-----+-----+-----+        FAC      | 8",
        " 2|     |     |     |     |        SHP      | 8",
        "  +-----+-----+-----+-----+        HWY      | 8",
        " 3|     |     |     |     |        BCH      | 8",
        "  +-----+-----+-----+-----+",
        " 4|     |     |     |     |",
        "  +-----+-----+-----+-----+"]

boardPlaced = [
        "     A     B     C     D           Building   Remaining",
        "  +-----+-----+-----+-----+        --------------------",
        " 1| SHP |     |     |     |        HSE      | 8",
        "  +-----+-----+-----+-----+        FAC      | 8",
        " 2|     |     |     |     |        SHP      | 7",
        "  +-----+-----+-----+-----+        HWY      | 8",
        " 3|     |     |     |     |        BCH      | 8",
        "  +-----+-----+-----+-----+",
        " 4|     |     |     |     |",
        "  +-----+-----+-----+-----+"]

remainingBuildings = ["Building         Remaining\n--------         --------\nHSE              8\nFAC              8\nSHP              8\nHWY              8\nBCH              8\n"]

remainingBuildingsPlaced = ["Building         Remaining\n--------         --------\nHSE              8\nFAC              8\nSHP              7\nHWY              8\nBCH              8\n"]


def test_see_remaining_building_initial_state():
    """
    Test script to test see remaining buildings during turn 1 from the game menu
    """

    set_keyboard_input(["3","0"])

    test_game = Game()
    test_game.building_pool = defaultBuildingPool
    test_game.randomized_building_history = {"1": ["SHP", "SHP"], "2": ["SHP", "SHP"]}
    test_game.start_new_turn()
    result = get_display_output()

    assert result == ["","Turn 1"] + board + gameMenu + remainingBuildings + ["", "Turn 1"] + board + gameMenu
 
   
def test_see_remaining_building_after_play():
    """
    Test script to test see remaining buildings after turn 1 from the game menu
    """

    set_keyboard_input(["3","1","a1","3","0"])

    test_game = Game()
    test_game.building_pool = defaultBuildingPool
    test_game.randomized_building_history = {"1": ["SHP", "SHP"], "2": ["SHP", "SHP"]}
    test_game.start_new_turn()
    result = get_display_output()

    assert result == ["","Turn 1"] + board + gameMenu + remainingBuildings + ["", "Turn 1"] + board + gameMenu + ["Build where? ","", "Turn 2"] + boardPlaced + gameMenu + remainingBuildingsPlaced + ["",
    "Turn 2"] + boardPlaced + gameMenu


   
