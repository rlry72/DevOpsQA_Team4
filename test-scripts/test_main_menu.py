import pytest
import os
from classes.game import *
from classes.menu import *
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
import sys
from unittest.mock import Mock




def test_main_menu_to_game_menu():
    """
    Test script test going to main menu from game menu
    """
    set_keyboard_input(["1","0"])
    selected = main_menu()

    if (selected == "1"):
        start_new_game()


    result = get_display_output()
    assert result == ["Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit",
    "Your choice? ",
    "",
    "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]



def test_main_menu():
    """
    Test script to test main menu output
    """
    set_keyboard_input(["0"])
    main_menu()
    result = get_display_output()

    assert result == ["Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit",
    "Your choice? "]




def test_main_menu_invalid_input():
    """
    Test script to test invalid input in main menu
    """
    set_keyboard_input(["-1","0"])
    main_menu()
    result = get_display_output()

    assert result == ["Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit",
    "Your choice? ",
    "Invalid input, please try again",
    "Your choice? "]