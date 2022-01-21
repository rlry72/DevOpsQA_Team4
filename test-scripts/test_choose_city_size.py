import pytest
import os
from main import *
from classes.game import *
from classes.menu import *
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
import sys
from unittest.mock import Mock

mainMenu = ["Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
    "Your choice? "]

gameBoard = [
            "     A     B     C     D  ",
            "  +-----+-----+-----+-----+",
            " 1|     |     |     |     |",
            "  +-----+-----+-----+-----+",
            " 2|     |     |     |     |",
            "  +-----+-----+-----+-----+",
            " 3|     |     |     |     |",
            "  +-----+-----+-----+-----+",
            " 4|     |     |     |     |",
            "  +-----+-----+-----+-----+",]

gameMenu = ["Turn {turnNumber}",
            "{gameBoard}",
            '1. Build a {opt1}',
            '2. Build a {opt2}', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

currentCitySize = [
    "",
    "--------- CURRENT CITY SIZE ---------",
    "Width: 4",
    "Height: 4",
    "-------------------------------------",
]

citySize = [
    "",
    "Choose your city size below. Please take note that the multiplication of width and height cannot be more than 40.",
    "Enter 0 to exit this configuration."
]

inputWidth = [
    "",
    "Enter value for width: "
]

inputHeight = ["Enter value for height: "]

invalidInput = [
    "",
    "Invalid input has been entered. Please enter a number."
]

inputCitySizeExit = [
    "",
    "City size will not be updated.",
]

mainMenuToInputSize = mainMenu + currentCitySize + citySize

invalidInputWidthExpectedResult = mainMenuToInputSize + inputWidth + invalidInput + inputWidth + invalidInput + inputWidth + inputCitySizeExit + currentCitySize
invalidInputHeightExpectedResult = mainMenuToInputSize + inputWidth + invalidInput + inputWidth + inputHeight + invalidInput + [""] + inputHeight + inputCitySizeExit + currentCitySize

exitExpectedResultWidth = mainMenuToInputSize + inputWidth + inputCitySizeExit + currentCitySize
exitExpectedResultHeight = mainMenuToInputSize + inputWidth + inputHeight + inputCitySizeExit + currentCitySize


def test_change_city_size():
    """
    Tests successful city size change from 4x4 to 5x6
    """
    set_keyboard_input(["5", "4", "6", "1", "0", "0"])

    menu = main_menu()
    if menu == "5":
        prompt_city_size([4,4])
    
    if menu == "1":
        startGame = start_new_game()
    # if menu == 4:

        
    result = get_display_output()

    assert result == False

    # assert startGame.width == '5'
    # assert result[2] == ""
    # captured, err = capfd.readouterr()
    # assert captured != ''


    # if menu == 1:
    #     start_new_game()
    


    # assert Game.height == 4
    # assert Game.width == 4

    # for output in result:

@pytest.mark.parametrize("exitInput, expectedResult",
[(["5", "0", "0"], exitExpectedResultWidth), (["5", "4", "0", "0"], exitExpectedResultHeight)])
def test_exit_change_city_size(exitInput, expectedResult):
    """
    Tests exit from city size change to main menu from input width and input height
    """

    set_keyboard_input(exitInput)

    menu = main_menu()
    if menu == "5":
        prompt_city_size([4,4])

    result = get_display_output()

    assert result == expectedResult


@pytest.mark.parametrize("invalidInput, expectedResult",
[(["5", "a", "0"], invalidInputWidthExpectedResult), (["5", "", "0"], invalidInputWidthExpectedResult),
(["5", "5", "b", "0"], invalidInputWidthExpectedResult), (["5", "5", "", "0"], invalidInputWidthExpectedResult),
(["5", "100", "0"], invalidInputWidthExpectedResult)])
def test_invalid_input_change_city_size(invalidInput, expectedResult):
    """
    Tests invalid input in input width and input height
    """

    set_keyboard_input(invalidInput)

    menu = main_menu()
    if menu == "5":
        prompt_city_size([4,4])

    result = get_display_output()

    assert result == expectedResult


    