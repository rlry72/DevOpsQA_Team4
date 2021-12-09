import pytest
import os
import sys
from unittest.mock import Mock
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
from classes.game import *
from classes.menu import *

def test_see_remaining_building_initial_state():
    """
    Test script to test see remaining buildings during turn 1 from the game menu
    """

    set_keyboard_input(["3","0"])

    test_game = Game()
    test_game.start_new_turn()
    result = get_display_output()

    assert result == ["", "Turn 1",
    "    A     B     C     D  ",
    " +-----+-----+-----+-----+",
    "1|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "2|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "3|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "4|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "1. Build a SHP",
    "2. Build a SHP",
    "3. See remaining buildings",
    "4. See current score\n",
    "5. Save game",
    "0. Exit to main menu",
    "Your choice? ",
    "Building         Remaining",
    "---------        ---------",
    "HSE              8        ",
    "FAC              8        ",
    "SHP              8        ",
    "HWY              8        ",
    "BCH              8        ",
    "Turn 1",
     "    A     B     C     D  ",
    " +-----+-----+-----+-----+",
    "1|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "2|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "3|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "4|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "1. Build a SHP",
    "2. Build a SHP",
    "3. See remaining buildings",
    "4. See current score\n",
    "5. Save game",
    "0. Exit to main menu",
    "Your choice? "]

   
def test_see_remaining_building_after_play():
    """
    Test script to test see remaining buildings after turn 1 from the game menu
    """

    set_keyboard_input(["3","1","a1","3","0"])

    test_game = Game()
    test_game.start_new_turn()
    result = get_display_output()

    assert result == ["", "Turn 1",
    "    A     B     C     D  ",
    " +-----+-----+-----+-----+",
    "1|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "2|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "3|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "4|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "1. Build a SHP",
    "2. Build a SHP",
    "3. See remaining buildings",
    "4. See current score\n",
    "5. Save game",
    "0. Exit to main menu",
    "Your choice? ",
    "Building         Remaining",
    "---------        ---------",
    "HSE              8        ",
    "FAC              8        ",
    "SHP              8        ",
    "HWY              8        ",
    "BCH              8        ",
    "Turn 1",
     "    A     B     C     D  ",
    " +-----+-----+-----+-----+",
    "1|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "2|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "3|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "4|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "1. Build a SHP",
    "2. Build a SHP",
    "3. See remaining buildings",
    "4. See current score\n",
    "5. Save game",
    "0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "Turn 2",
    "    A     B     C     D  ",
    " +-----+-----+-----+-----+",
    "1| SHP |     |     |     |",
    " +-----+-----+-----+-----+",
    "2|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "3|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "4|     |     |     |     |",
    " +-----+-----+-----+-----+",
    "1. Build a SHP",
    "2. Build a SHP",
    "3. See remaining buildings",
    "4. See current score\n",
    "5. Save game",
    "0. Exit to main menu",
    "Your choice? ",
    "Building         Remaining",
    "---------        ---------",
    "HSE              8        ",
    "FAC              8        ",
    "SHP              7        ",
    "HWY              8        ",
    "BCH              8        "]

   
