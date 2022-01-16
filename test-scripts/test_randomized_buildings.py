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

class SideEffect:
    def __init__(self, *fns):
        self.fs = iter(fns)
    def __call__(self, *args, **kwargs):
        f = next(self.fs)
        return f(*args, **kwargs)

def fake_randomized_buildings_1():
    return ["BCH", "HSE"]

def fake_randomized_buildings_2():
    return ["SHP", "HWY"]


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

@mock.patch('classes.game.random_buildings', side_effect = SideEffect(fake_randomized_buildings_1, fake_randomized_buildings_2))
def test_mock_randomized_building(mock_random_buildings):
    """
    Test script to test building a randomized building from the game menu
    """
    set_keyboard_input(["1","a1","0"])

    test_game = Game()
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
    "1. Build a SHP\n2. Build a HWY\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu",
    "Your choice? "]

def test_compare_randomized_building():
    """
    Test script to compare randomized building output over 2 turns
    """
    set_keyboard_input(["1","a1","0"])

    test_game = Game()
    test_game.start_new_turn()
    result = get_display_output()

    assert result[3] != result[9]
    

# need to test how random the randomized selections actually are