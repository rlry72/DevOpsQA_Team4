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

defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

def test_compare_randomized_building_5_turns():
    """
    Test script to compare randomized building output over 5 turns
    """
    set_keyboard_input(["1","a1","1", "b1", "1", "c1", "1", "d1", "1", "a2","0"])

    optList = []

    # start game and input options and buildings
    test_game = Game()
    test_game.building_pool = defaultBuildingPool
    test_game.start_new_turn()
    result = get_display_output()

    # get all options returned and add to list
    for i in range(len(result)):
        if "1" or "2" in result[i]:
            # get only the building in option
            optList.append(result[i].split(" ")[-1])

    # check that all are not similar
    assert optList[0] != optList[1] != optList[2] != optList[3] != optList[4]
    # assert result[3] != result[9] != result[15] != result[21] != result[26]


def test_check_randomized_building_in_building_pool():
    """
    Test script to check that buildings in options are in building pool
    """

    # empty option list
    optList = []
   
    set_keyboard_input(["1","a1","1","a2","1","a3","1","a4","1","b1","1","b2","1","b3","1","b4","0"])

    test_game = Game()
    test_game.building_pool = defaultBuildingPool
     # get building pool from game
    # start game
    test_game.start_new_turn()
    result = get_display_output()

    # get all buildings returned in game menu in output
    for output in result:
        if "1." in output:
            # split by space and get the last item (the building name) in list and append to options list
            opt1 = output.split(" ")[-1]
            optList.append(opt1)
        if "2." in output:
            # split by space and get the last item (the building name) in list and append to options list
            opt2 = output.split(" ")[-1]
            optList.append(opt2)

    # convert option list to set (no duplicates) and assert that option list is a subset of building pool.
    assert set(optList).issubset(defaultBuildingPool) is True
    # assert result[3] != result[9]

def test_randomized_building_options_1_building_left():
    """
    Test script to test options when only 1 building is left
    """
    set_keyboard_input(["0"])

    test_game = Game()
    # set building pool to only have 1 SHP left and no other buildings
    test_game.building_pool = {"HSE": 0, "FAC": 0, "SHP": 1, "HWY": 0, "BCH": 0}
    test_game.start_new_turn()
    result = get_display_output()
    
    # initialize options
    opt1 = ""
    opt2 = ""

    for output in result:
        if "1." in output:
            # split by space and get the last item (the building name) in list and append to options list
            opt1 = output.split(" ")[-1]
            # opt1 = output.split("\n")[0].split(" ")[-1]
        if "2." in output:
            # split by space and get the last item (the building name) in list and append to options list
            opt2 = output.split(" ")[-1]
            # opt2 = output.split("\n")[1].split(" ")[-1]

    # check that option 1 is the same as option 2
    assert opt1 == opt2
# need to test how random the randomized selections actually are