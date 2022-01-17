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

class SideEffect:
    def __init__(self, *fns):
        self.fs = iter(fns)
    def __call__(self, *args, **kwargs):
        f = next(self.fs)
        return f(*args, **kwargs)

def fake_randomized_buildings_1(self, building_pool):
    # updates randomized building history with the list of 2 randomized buildings
    self.randomized_building_history[str(self.turn_num)] = ["SHP", "HSE"]

    # return ["BCH", "HSE"]

def fake_randomized_buildings_2(self, building_pool):
    # updates randomized building history with the list of 2 randomized buildings
    self.randomized_building_history[str(self.turn_num)] = ["BCH", "HWY"]

    # return ["SHP", "HWY"]


def runsTest(l, l_median):
  
    runs, n1, n2 = 0, 0, 0
      
    # Checking for start of new run
    for i in range(len(l)):
          
        # no. of runs
        if (l[i] >= l_median and l[i-1] < l_median) or \
                (l[i] < l_median and l[i-1] >= l_median):
            runs += 1  
          
        # no. of positive values
        if(l[i]) >= l_median:
            n1 += 1   
          
        # no. of negative values
        else:
            n2 += 1   
  
    runs_exp = ((2*n1*n2)/(n1+n2))+1
    stan_dev = math.sqrt((2*n1*n2*(2*n1*n2-n1-n2))/ \
                       (((n1+n2)**2)*(n1+n2-1)))
  
    z = (runs-runs_exp)/stan_dev
  
    return z

# @patch('classes.game.Game.get_two_buildings_from_pool', side_effect = SideEffect(fake_randomized_buildings_1, fake_randomized_buildings_2))
@pytest.mark.skip(reason="invalid test, does not really test random")
def test_mock_randomized_building(mocker):
    """
    Test script to test building a randomized building from the game menu
    """
    set_keyboard_input(["1","a1","0"])

    test_game = Game()
    # test_game.randomized_building_history = {"1": ["SHP", "HSE"], "2": ["BCH", "HWY"]}
    test_game.start_new_turn()
    result = get_display_output()
    
    # mock_randomized_building = mocker.patch('classes.game.Game.get_two_buildings_from_pool');

    # assert mock_randomized_building.call_count == 2

    assert result == ["", "Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a HSE\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? ",
    "Build where? ",
    "",
    "Turn 2",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1| SHP |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a BCH\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

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