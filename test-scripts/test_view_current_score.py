from classes.game import *
from classes.menu import *
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
from unittest.mock import Mock, patch
from unittest import mock
import sys
import pytest
import os
import random
import math
import statistics


gamemenuoptions = "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu"


def test_view_current_score_empty():
    """
    Test script to test viewing current score when there are 0 buildings on the board. (TC-07A)
    """
    set_keyboard_input(["4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["BCH", "HSE"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 0",
    "SHP: 0",
    "HWY: 0",
    "BCH: 0",
    "Total Score: 0",
    "",
    "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]


def test_view_current_score_bch_center_of_city():
    """
    Test script to test viewing current score when a single "BCH" is on the board not on the right or left side of the city. (TC-07B)
    """
    set_keyboard_input(["1","b2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["BCH", "HSE"], "2": ["BCH", "HSE"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | BCH |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 0",
    "SHP: 0",
    "HWY: 0",
    "BCH: 1 = 1",
    "Total Score: 1",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | BCH |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_bch_right_or_left_of_city():
    """
    Test script to test viewing current score when a single "BCH" is on the board on the right or left side of the city. (TC-07B)
    """
    set_keyboard_input(["1","a1","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["BCH", "HSE"], "2": ["BCH", "HSE"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| BCH |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 0",
    "SHP: 0",
    "HWY: 0",
    "BCH: 3 = 3",
    "Total Score: 3",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| BCH |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_fac_single_fac():
    """
    Test script to test viewing current score when a single "FAC" is on the board. (TC-07C)
    """
    set_keyboard_input(["1","a1","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["FAC", "HWY"], "2": ["FAC", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 1 = 1",
    "SHP: 0",
    "HWY: 0",
    "BCH: 0",
    "Total Score: 1",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_fac_4fac():
    """
    Test script to test viewing current score when a 4 "FAC" is on the board. (TC-07C)
    """
    set_keyboard_input(["1","a1","1","b1","1","c1","1","d1","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["FAC", "HWY"], "2": ["FAC", "HWY"], "3": ["FAC", "HWY"], "4": ["FAC", "HWY"], "5": ["FAC", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC | FAC |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC | FAC | FAC |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 5",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC | FAC | FAC | FAC |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 4 + 4 + 4 + 4 = 16",
    "SHP: 0",
    "HWY: 0",
    "BCH: 0",
    "Total Score: 16",
    "",
    "Turn 5",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC | FAC | FAC | FAC |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_fac_5fac():
    """
    Test script to test viewing current score when a 5 "FAC" is on the board. (TC-07C)
    """
    set_keyboard_input(["1","a1","1","b1","1","c1","1","d1","1","a2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["FAC", "HWY"], "2": ["FAC", "HWY"], "3": ["FAC", "HWY"], "4": ["FAC", "HWY"], "5": ["FAC", "HWY"], "6": ["FAC", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC | FAC |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC | FAC | FAC |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 5",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC | FAC | FAC | FAC |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 6",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC | FAC | FAC | FAC |\n +-----+-----+-----+-----+\n2| FAC |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 4 + 4 + 4 + 4 + 1 = 17",
    "SHP: 0",
    "HWY: 0",
    "BCH: 0",
    "Total Score: 17",
    "",
    "Turn 6",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| FAC | FAC | FAC | FAC |\n +-----+-----+-----+-----+\n2| FAC |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_hse_single_hse():
    """
    Test script to test viewing current score when a single "HSE" is on the board. (TC-07D)
    """
    set_keyboard_input(["2","a1","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["BCH", "HSE"], "2": ["BCH", "HSE"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| HSE |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 1 = 1",
    "FAC: 0",
    "SHP: 0",
    "HWY: 0",
    "BCH: 0",
    "Total Score: 1",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| HSE |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_hse_2hse_adjacent():
    """
    Test script to test viewing current score when  2 "HSE" is on the board and they are adjacent. (TC-07D)
    """
    set_keyboard_input(["2","a1","2","b1","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["BCH", "HSE"], "2": ["BCH", "HSE"], "3": ["BCH", "HSE"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| HSE |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| HSE | HSE |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 1 + 1 = 2",
    "FAC: 0",
    "SHP: 0",
    "HWY: 0",
    "BCH: 0",
    "Total Score: 2",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| HSE | HSE |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_hse_2bch_center():
    """
    Test script to test viewing current score when a single "HSE" and 2 "BCH" is on the board and the "BCH" are adjacent to the "HSE". The "BCH" are not in the Right or Left side of the city (TC-07D)
    """
    set_keyboard_input(["2","b2","1","b3","1","c2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["BCH", "HSE"], "2": ["BCH", "HSE"], "3": ["BCH", "HSE"], "4": ["BCH", "HSE"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | HSE |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | HSE |     |     |\n +-----+-----+-----+-----+\n3|     | BCH |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | HSE | BCH |     |\n +-----+-----+-----+-----+\n3|     | BCH |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 4 = 4",
    "FAC: 0",
    "SHP: 0",
    "HWY: 0",
    "BCH: 1 + 1 = 2",
    "Total Score: 6",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | HSE | BCH |     |\n +-----+-----+-----+-----+\n3|     | BCH |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_hse_2shp_adjacent_to_hse_but_not_to_each_other():
    """
    Test script to test viewing current score when a single "HSE" and 2 "SHP" is on the board and the "SHP" are adjacent to the "HSE" but not adjacent to each other. (TC-07D)
    """
    set_keyboard_input(["2","b2","1","a2","1","c2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["BCH", "HSE"], "2": ["SHP", "HWY"], "3": ["SHP", "HWY"], "4": ["SHP", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | HSE |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| SHP | HSE |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| SHP | HSE | SHP |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 2 = 2",
    "FAC: 0",
    "SHP: 1 + 1 = 2",
    "HWY: 0",
    "BCH: 0",
    "Total Score: 4",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| SHP | HSE | SHP |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_hse_1fac_adjacent():
    """
    Test script to test viewing current score when a single "HSE" and a single "FAC" is on the board and they are adjacent. (TC-07D)
    """
    set_keyboard_input(["2","b2","1","a2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["BCH", "HSE"], "2": ["FAC", "HWY"], "3": ["FAC", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | HSE |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| FAC | HSE |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 1 = 1",
    "FAC: 1 = 1",
    "SHP: 0",
    "HWY: 0",
    "BCH: 0",
    "Total Score: 2",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| FAC | HSE |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_shp_single_shp():
    """
    Test script to test viewing current score when a single "SHP" is on the board. (TC-07E)
    """
    set_keyboard_input(["1","b2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "HWY"], "2": ["SHP", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | SHP |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 0",
    "SHP: 1 = 1",
    "HWY: 0",
    "BCH: 0",
    "Total Score: 1",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | SHP |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_shp_single_bch_adjacent_not_in_center():
    """
    Test script to test viewing current score when a single "SHP" and a single "BCH" is on the board and they are adjacent. The "BCH" is on the right or left side of the City. (TC-07E)
    """
    set_keyboard_input(["1","b2","1","a2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "HWY"], "2": ["BCH", "HSE"], "3": ["BCH", "HSE"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | SHP |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| BCH | SHP |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 0",
    "SHP: 1 = 1",
    "HWY: 0",
    "BCH: 3 = 3",
    "Total Score: 4",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| BCH | SHP |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_shp_single_bch_adjacent_single_fac_adjacent_bch_not_in_center():
    """
    Test script to test viewing current score when a single "SHP", single "BCH" and a single "FAC" is on the board. They are adjacent to the SHP.  The "BCH" is on the Right or Left side of the City. (TC-07E)
    """
    set_keyboard_input(["1","b2","1","a2","1","c2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "HWY"], "2": ["BCH", "HSE"], "3": ["FAC", "HWY"], "4": ["FAC", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     | SHP |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| BCH | SHP |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| BCH | SHP | FAC |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 1 = 1",
    "SHP: 2 = 2",
    "HWY: 0",
    "BCH: 3 = 3",
    "Total Score: 6",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| BCH | SHP | FAC |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_shp_2_bch_adjacent_single_fac_adjacent_bch_not_in_center():
    """
    Test script to test viewing current score when a single "SHP", 2 "BCH" and a single "FAC" is on the board. They are adjacent.  The "BCH" is on the Right or Left side of the City. (TC-07E)
    """
    set_keyboard_input(["1","a2","1","a1","1","a3","1","b2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "HWY"], "2": ["BCH", "HSE"], "3": ["BCH", "HSE"], "4": ["FAC", "HWY"], "5": ["FAC", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| SHP |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| BCH |     |     |     |\n +-----+-----+-----+-----+\n2| SHP |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| BCH |     |     |     |\n +-----+-----+-----+-----+\n2| SHP |     |     |     |\n +-----+-----+-----+-----+\n3| BCH |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 5",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| BCH |     |     |     |\n +-----+-----+-----+-----+\n2| SHP | FAC |     |     |\n +-----+-----+-----+-----+\n3| BCH |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 1 = 1",
    "SHP: 2 = 2",
    "HWY: 0",
    "BCH: 3 + 3 = 6",
    "Total Score: 9",
    "",
    "Turn 5",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| BCH |     |     |     |\n +-----+-----+-----+-----+\n2| SHP | FAC |     |     |\n +-----+-----+-----+-----+\n3| BCH |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a FAC\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_hwy_single_hwy():
    """
    Test script to test viewing current score when a single "HWY" is on the board (TC-07F)
    """
    set_keyboard_input(["2","a2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "HWY"], "2": ["BCH", "HSE"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 0",
    "SHP: 0",
    "HWY: 1 = 1",
    "BCH: 0",
    "Total Score: 1",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_hwy_2_hwy_adjacent_on_single_row():
    """
    Test script to test viewing current score when a 2 "HWY" is on the board all adjacent on the same row. (TC-07F)
    """
    set_keyboard_input(["2","a2","2","b2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "HWY"], "2": ["SHP", "HWY"], "3": ["SHP", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY | HWY |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 0",
    "SHP: 0",
    "HWY: 2 + 2 = 4",
    "BCH: 0",
    "Total Score: 4",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY | HWY |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_current_score_hwy_4_hwy_adjacent_on_single_row():
    """
    Test script to test viewing current score when a 4 "HWY" is on the board all adjacent on the same row. (TC-07F)
    """
    set_keyboard_input(["2","a2","2","b2","2","c2","2","d2","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "HWY"], "2": ["SHP", "HWY"], "3": ["SHP", "HWY"], "4": ["SHP", "HWY"], "5": ["SHP", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY | HWY |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY | HWY | HWY |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 5",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY | HWY | HWY | HWY |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 0",
    "SHP: 0",
    "HWY: 4 + 4 + 4 + 4 = 16",
    "BCH: 0",
    "Total Score: 12",
    "",
    "Turn 5",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY | HWY | HWY | HWY |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_view_currentscore_hwy_2_hwy_adjacent_on_single_row_1hwy_adjacent_on_different_row():
    """
    Test script to test viewing current score when a 2 "HWY" is on the board all adjacent on the same row. (TC-07F)
    """
    set_keyboard_input(["2","a2","2","b2","2","a1","4","0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "HWY"], "2": ["SHP", "HWY"], "3": ["SHP", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 3",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2| HWY | HWY |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| HWY |     |     |     |\n +-----+-----+-----+-----+\n2| HWY | HWY |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "",
    "HSE: 0",
    "FAC: 0",
    "SHP: 0",
    "HWY: 2 + 2 + 1 = 4",
    "BCH: 0",
    "Total Score: 4",
    "",
    "Turn 4",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| HWY |     |     |     |\n +-----+-----+-----+-----+\n2| HWY | HWY |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]
