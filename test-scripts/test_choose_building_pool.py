import pytest
import os
from classes.game import *
from classes.menu import *
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
import sys
from unittest.mock import Mock

defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

invalidInputArray = ["",
    "--------- CURRENT BUILDING POOL ---------",
    "[HSE, FAC, SHP, HWY, BCH]",
    "-----------------------------------------",
    "",
    "Choose your new building pool below.",
    "",
    "1. Beach (BCH)",
    "2. Factory (FAC)",
    "3. House (HSE)",
    "4. Highway (HWY)",
    "5. Monument (MON)",
    "6. Park (PRK)",
    "7. Shop (SHP)",
    "",
    "0. Exit to main menu",
    "Enter input: ",
    "",
    "Invalid input has been entered.",
    "Please enter number for the option (e.g. 1) and it needs to be within the range.",
    "",
    "1. Beach (BCH)",
    "2. Factory (FAC)",
    "3. House (HSE)",
    "4. Highway (HWY)",
    "5. Monument (MON)",
    "6. Park (PRK)",
    "7. Shop (SHP)",
    "",
    "0. Exit to main menu",
    "Enter input: ",
    "",
    "Configuring building pool is unsuccessful.",
    "Building pool remains the same as the current building pool."]


errorMessage = ["Invalid input has been entered.","Please enter number for the option (e.g. 1) and it needs to be within the range."]

def test_choose_building_pool():
    """
    Test script to test choosing HSE, FAC, SHP, HWY, MON buildings in the building pool.
    """

    set_keyboard_input(["3","2","5","2","2","4","0"])
    building_list = choose_building_pool(defaultBuildingPool)
    
    test_game = Game()
    test_game.randomized_building_history = {"1": ["SHP", "SHP"]}
    test_game.building_pool = building_list
    test_game.start_new_turn()


    result = get_display_output()
    assert result == ["",
    "--------- CURRENT BUILDING POOL ---------",
    "[HSE, FAC, SHP, HWY, BCH]",
    "-----------------------------------------",
    "",
    "Choose your new building pool below.",
    "",
    "1. Beach (BCH)",
    "2. Factory (FAC)",
    "3. House (HSE)",
    "4. Highway (HWY)",
    "5. Monument (MON)",
    "6. Park (PRK)",
    "7. Shop (SHP)",
    "",
    "0. Exit to main menu",
    "Enter input: ",
    "",
    "--------- CURRENT BUILDING POOL ---------",
    "[HSE]",
    "-----------------------------------------",
    "",
    "1. Beach (BCH)",
    "2. Factory (FAC)",
    "3. Highway (HWY)",
    "4. Monument (MON)",
    "5. Park (PRK)",
    "6. Shop (SHP)",
    "",
    "0. Exit to main menu",
    "Enter input: ",
    "",
    "--------- CURRENT BUILDING POOL ---------",
    "[HSE, FAC]",
    "-----------------------------------------",
    "",
    "1. Beach (BCH)",
    "2. Highway (HWY)",
    "3. Monument (MON)",
    "4. Park (PRK)",
    "5. Shop (SHP)",
    "",
    "0. Exit to main menu",
    "Enter input: ",
    "",
    "--------- CURRENT BUILDING POOL ---------",
    "[HSE, FAC, SHP]",
    "-----------------------------------------",
    "",
    "1. Beach (BCH)",
    "2. Highway (HWY)",
    "3. Monument (MON)",
    "4. Park (PRK)",
    "",
    "0. Exit to main menu",
    "Enter input: ",
    "",
    "--------- CURRENT BUILDING POOL ---------",
    "[HSE, FAC, SHP, HWY]",
    "-----------------------------------------",
    "",
    "1. Beach (BCH)",
    "2. Monument (MON)",
    "3. Park (PRK)",
    "",
    "0. Exit to main menu",
    "Enter input: ",
    "",
    "--------- CHOSEN BUILDING POOL ---------",
    "[HSE, FAC, SHP, HWY, MON]",
    "----------------------------------------",
    "",
    "Turn 1",
    "     A     B     C     D  ",
    "  +-----+-----+-----+-----+",
    " 1|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 2|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 3|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    '1. Build a SHP',
    '2. Build a SHP', 
    '3. See remaining buildings',
    '4. See current score',
    '', 
    '5. Save game', 
    '0. Exit to main menu', 
    'Your choice? ',
    "",
    "HSE: 0",
    "FAC: 0",
    "SHP: 0",
    "HWY: 0",
    "MON: 0",
    "Total score: 0",
    "",
    "Turn 1",
    "     A     B     C     D  ",
    "  +-----+-----+-----+-----+",
    " 1|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 2|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 3|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    '1. Build a SHP',
    '2. Build a SHP', 
    '3. See remaining buildings',
    '4. See current score',
    '', 
    '5. Save game', 
    '0. Exit to main menu', 
    'Your choice? ']

@pytest.mark.parametrize("invalidInput, expectedResult",
[(["9", "0"], invalidInputArray), (["haha", "0"], invalidInputArray), (["", "0"], invalidInputArray)])
def test_choose_building_pool_invalid_input(invalidInput, expectedResult):
    """
    Test script to test invalid input when choosing building
    """

    set_keyboard_input(invalidInput)
    building_list = choose_building_pool(defaultBuildingPool)
    

    result = get_display_output()
    assert result == expectedResult

    
@pytest.mark.parametrize("invalidInput, expectedResult",
[(["8", "0"], errorMessage), (["7","7", "0"], errorMessage), (["6","6","6","0"], errorMessage), (["5","5","5","5","0"], errorMessage)
, (["4","4","4","4","4","0"], errorMessage)])
def test_choose_building_pool_out_of_range(invalidInput, expectedResult):
    """
    Test script to test invalid input when choosing building
    """

    set_keyboard_input(invalidInput)
    building_list = choose_building_pool(defaultBuildingPool)
    result = get_display_output()

    check =  all(item in result for item in expectedResult)

    assert check == True

