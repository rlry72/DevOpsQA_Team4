from classes.game import *
from classes.menu import *
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
from unittest.mock import Mock, patch
import sys
import pytest
import os
import random
import math
import statistics

def test_compare_randomized_building_5_turns():
    """
    Test script to compare randomized building output over 5 turns
    """
    set_keyboard_input(["1","a1","1", "b1", "1", "c1", "1", "d1", "1", "a2","0"])

    optList = []

    test_game = Game()
    test_game.start_new_turn()
    result = get_display_output()

    for i in range(len(result)):
        if "1" or "2" in result[i]:
            optList.append(result[i])

    assert optList[0] != optList[1] != optList[2] != optList[3] != optList[4]
    # assert result[3] != result[9] != result[15] != result[21] != result[26]

@pytest.mark.skip(reason="no way of currently testing this, will manually test")
def test_compare_randomized_building_10_turns():
    """
    Test script to check randomized building output over 10 turns whether the randomizer is good enough
    """

    option1Arr = []
    option2Arr = []

    set_keyboard_input(["1","a1","1","a2","1","a3","1","a4","1","b1","1","b2","1","b3","1","b4","1","c1","1","c2","0"])

    test_game = Game()
    test_game.start_new_turn()
    result = get_display_output()

    for output in result:
        if "1." in output:
            opt1 = output.split("\n")[0].split(" ")[-1]
            option1Arr.append(opt1)
        if "2." in output:
            opt2 = output.split("\n")[1].split(" ")[-1]
            option2Arr.append(opt2)
    # assert result[3] != result[9]

def test_check_randomized_building_in_building_pool():
    """
    Test script to check that buildings in options are in building pool
    """

    optList = []
    buildingPool = ["BCH", "FAC", "HSE", "SHP", "HWY"]


    set_keyboard_input(["1","a1","1","a2","1","a3","1","a4","1","b1","1","b2","1","b3","1","b4","0"])

    test_game = Game()
    test_game.start_new_turn()
    result = get_display_output()

    for output in result:
        if "1." in output:
            opt1 = output.split("\n")[0].split(" ")[-1]
            optList.append(opt1)
        if "2." in output:
            opt2 = output.split("\n")[1].split(" ")[-1]
            optList.append(opt2)
    assert set(optList).issubset(buildingPool) is True
    # assert result[3] != result[9]

def test_randomized_building_options_1_building_left():
    """
    Test script to test options when only 1 building is left
    """
    set_keyboard_input(["0"])

    test_game = Game()
    test_game.building_pool = {"HSE": 0, "FAC": 0, "SHP": 1, "HWY": 0, "BCH": 0}
    test_game.start_new_turn()
    result = get_display_output()
    
    opt1 = ""
    opt2 = ""

    for output in result:
        if "1." in output:
            opt1 = output.split("\n")[0].split(" ")[-1]
        if "2." in output:
            opt2 = output.split("\n")[1].split(" ")[-1]

    assert opt1 == opt2
# need to test how random the randomized selections actually are