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

    assert result == ["","Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Building         Remaining\n--------         --------\nHSE              8\nFAC              8\nSHP              8\nHWY              8\nBCH              8\n",
    "","Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",]
 
   
def test_see_remaining_building_after_play():
    """
    Test script to test see remaining buildings after turn 1 from the game menu
    """

    set_keyboard_input(["3","1","a1","3","0"])

    test_game = Game()
    test_game.start_new_turn()
    result = get_display_output()

    assert result == ["","Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Building         Remaining\n--------         --------\nHSE              8\nFAC              8\nSHP              8\nHWY              8\nBCH              8\n",
    "","Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| SHP |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Building         Remaining\n--------         --------\nHSE              8\nFAC              8\nSHP              7\nHWY              8\nBCH              8\n",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| SHP |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    ]

   
