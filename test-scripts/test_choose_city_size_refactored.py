import pytest
import os
from main import *
from classes.game import *
from classes.menu import *
from classes.building import *
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
import sys
import classes
from unittest.mock import Mock

pytestmark = pytest.mark.skipif("generate_remaining_building_string" not in dir(classes.game.Game), reason="view remaining buildings on side not implemented")

mainMenu = ["Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
    "Your choice? "]

mainMenuNoWelcome = ["\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
    "Your choice? "]

gameBoardDefault = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1|     |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+        HWY      | 8",
    " 3|     |     |     |     |        BCH      | 8",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

gameBoardDefaultNoRemainingBuildings = [
    "     A     B     C     D  ",
    "  +-----+-----+-----+-----+",
    " 1|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 2|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 3|     |     |     |     |",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

gameBoard = [
    "     A     B     C     D     E           Building   Remaining",
    "  +-----+-----+-----+-----+-----+        --------------------",
    " 1|     |     |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+-----+        HWY      | 8",
    " 3|     |     |     |     |     |        BCH      | 8",
    "  +-----+-----+-----+-----+-----+",
    " 4|     |     |     |     |     |",
    "  +-----+-----+-----+-----+-----+",
    " 5|     |     |     |     |     |",
    "  +-----+-----+-----+-----+-----+",
    " 6|     |     |     |     |     |",
    "  +-----+-----+-----+-----+-----+"
]

gameBoardNoRemainingBuildings = [
    "     A     B     C     D     E  ",
    "  +-----+-----+-----+-----+-----+",
    " 1|     |     |     |     |     |",
    "  +-----+-----+-----+-----+-----+",
    " 2|     |     |     |     |     |",
    "  +-----+-----+-----+-----+-----+",
    " 3|     |     |     |     |     |",
    "  +-----+-----+-----+-----+-----+",
    " 4|     |     |     |     |     |",
    "  +-----+-----+-----+-----+-----+",
    " 5|     |     |     |     |     |",
    "  +-----+-----+-----+-----+-----+",
    " 6|     |     |     |     |     |",
    "  +-----+-----+-----+-----+-----+"
]

turnNumber = ["Turn 1"]
            
gameMenu = ['1. Build a SHP',
            '2. Build a SHP', 
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

chosenCitySize = [
    "",
    "--------- CHOSEN CITY SIZE ---------",
    "Width: 5",
    "Height: 6",
    "------------------------------------",
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

invalidSize = [
    "",
    "The multiplication of width and height exceeds the limit of 40. Please re-enter your input."
]

inputCitySizeExit = [
    "",
    "City size will not be updated.",
]

mainMenuToInputSize = mainMenu + currentCitySize + citySize

invalidInputWidthExpectedResult = mainMenuToInputSize + inputWidth + invalidInput + inputWidth + inputCitySizeExit + currentCitySize + mainMenuNoWelcome
invalidInputHeightExpectedResult = mainMenuToInputSize + inputWidth + inputHeight + invalidInput + [""] + inputHeight + inputCitySizeExit + currentCitySize + mainMenuNoWelcome

exitExpectedResultWidth = mainMenuToInputSize + inputWidth + inputCitySizeExit + currentCitySize + mainMenuNoWelcome
exitExpectedResultHeight = mainMenuToInputSize + inputWidth + inputHeight + inputCitySizeExit + currentCitySize + mainMenuNoWelcome


def test_change_city_size_main_menu():
    """
    Tests successful city size change from 4x4 to 5x6 from main menu
    This test only tests the output of main menu, unable to properly test whether city size changes in game, that is tested in the next test.
    """

    '''
    main menu change city size expected output:

    Welcome, mayor of Simp City!
    ----------------------------
    1. Start new game
    2. Load saved game
    3. Show high scores
    4. Choose building pool
    5. Choose city size
    
    0. Exit
    Your choice? 

    Enter value for width: 
    Enter value for height: 

    --------- CHOSEN CITY SIZE ---------
    Width: 5
    Height: 6
    ------------------------------------

    1. Start new game
    2. Load saved game
    3. Show high scores
    4. Choose building pool
    5. Choose city size
    
    0. Exit
    Your choice? 
    '''
    set_keyboard_input(["5", "5", "6", "1", "0", "0"])
    
    with pytest.raises(SystemExit) as e:
        main()
    
    result = get_display_output()
    expectedResult = mainMenuToInputSize + inputWidth + inputHeight + chosenCitySize + mainMenuNoWelcome + [""] + turnNumber + gameBoard

    check = all(item in result for item in expectedResult)

    # assert result == False
    assert check == True


def test_change_city_size_game():
    """
    Tests successful city size change from default 4x4 to 5x6 using game variables
    """

    '''
    default (4x4) city size expected output:

    Turn 1
        A     B     C     D           Building   Remaining
     +-----+-----+-----+-----+        --------------------
    1|     |     |     |     |        HSE      | 8
     +-----+-----+-----+-----+        FAC      | 8
    2|     |     |     |     |        SHP      | 8
     +-----+-----+-----+-----+        HWY      | 8
    3|     |     |     |     |        BCH      | 8
     +-----+-----+-----+-----+
    4|     |     |     |     |
     +-----+-----+-----+-----+

    1. Build a SHP
    2. Build a SHP
    3. See remaining buildings
    4. See current score
    
    5. Save game
    0. Exit to main menu
    Your choice? 
    '''

    '''
    5x6 city size expected output:

    Turn 1
        A     B     C     D     E           Building   Remaining
     +-----+-----+-----+-----+-----+        --------------------
    1|     |     |     |     |     |        HSE      | 8
     +-----+-----+-----+-----+-----+        FAC      | 8
    2|     |     |     |     |     |        SHP      | 8
     +-----+-----+-----+-----+-----+        HWY      | 8
    3|     |     |     |     |     |        BCH      | 8
     +-----+-----+-----+-----+-----+
    4|     |     |     |     |     |
     +-----+-----+-----+-----+-----+
    5|     |     |     |     |     |
     +-----+-----+-----+-----+-----+
    6|     |     |     |     |     |
     +-----+-----+-----+-----+-----+
    1. Build a SHP
    2. Build a SHP
    3. See remaining buildings
    4. See current score
    
    5. Save game
    0. Exit to main menu
    Your choice? 
    '''
    set_keyboard_input(["0"])

    defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    gameDefault = Game()
    gameDefault.building_pool = defaultBuildingPool
    gameDefault.randomized_building_history = {"1": ["SHP", "SHP"]}
    gameDefault.start_new_turn()

    resultDefault = get_display_output()



    set_keyboard_input(["0"])

    defaultBuildingPool2 = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    game5x6 = Game(width = 5, height = 6)
    game5x6.building_pool = defaultBuildingPool2
    game5x6.randomized_building_history = {"1": ["SHP", "SHP"]}
    game5x6.start_new_turn()

    result5x6 = get_display_output()
    assert gameDefault.width == 4
    assert gameDefault.height == 4
    assert game5x6.width == 5
    assert game5x6.height == 6
    assert resultDefault == [""] + turnNumber + gameBoardDefault + gameMenu
    assert result5x6 == [""] + turnNumber + gameBoard + gameMenu

@pytest.mark.parametrize("exitInput, expectedResult",
[(["5", "0", "0"], exitExpectedResultWidth), (["5", "4", "0", "0"], exitExpectedResultHeight)])
def test_exit_change_city_size(exitInput, expectedResult):
    """
    Tests exit from city size change to main menu from input width and input height
    """

    '''
    exit from width selection expected output:

    Welcome, mayor of Simp City!
    ----------------------------
    1. Start new game
    2. Load saved game
    3. Show high scores
    4. Choose building pool
    5. Choose city size
    
    0. Exit
    Your choice? 

    Enter value for width: 
    
    City size will not be updated.

    --------- CURRENT CITY SIZE ---------
    Width: 4
    Height: 4
    -------------------------------------
    '''

    '''
    exit from height selection expected output:

    Welcome, mayor of Simp City!
    ----------------------------
    1. Start new game
    2. Load saved game
    3. Show high scores
    4. Choose building pool
    5. Choose city size
    
    0. Exit
    Your choice? 

    Enter value for width: 
    Enter value for height: 
    
    City size will not be updated.

    --------- CURRENT CITY SIZE ---------
    Width: 4
    Height: 4
    -------------------------------------

    1. Start new game
    2. Load saved game
    3. Show high scores
    4. Choose building pool
    5. Choose city size
    
    0. Exit
    Your choice? 
    '''

    set_keyboard_input(exitInput)

    with pytest.raises(SystemExit) as e:
        main()

    result = get_display_output()

    assert result == expectedResult

def test_change_city_size_invalid_size():
    """
    Tests invalid city size change from 4x4 to 8x8 from main menu
    """

    '''
    main menu change city size expected output:

    Welcome, mayor of Simp City!
    ----------------------------
    1. Start new game
    2. Load saved game
    3. Show high scores
    4. Choose building pool
    5. Choose city size
    
    0. Exit
    Your choice? 

    Enter value for width: 
    Enter value for height: 

    The multiplication of width and height exceeds the limit of 40. Please re-enter your input.

    Enter value for width:
    '''
    set_keyboard_input(["5", "8", "8", "0", "0"])
    
    with pytest.raises(SystemExit) as e:
        main()
    
    result = get_display_output()
    expectedResult = mainMenuToInputSize + inputWidth + inputHeight + invalidSize + inputWidth
    check = all(item in result for item in expectedResult)

    # assert result == False
    assert check == True
@pytest.mark.parametrize("invalidInput, expectedResult",
[(["5", "a", "0", "0"], invalidInputWidthExpectedResult), (["5", "", "0", "0"], invalidInputWidthExpectedResult),
(["5", "5", "b", "0", "0"], invalidInputHeightExpectedResult), (["5", "5", "", "0", "0"], invalidInputHeightExpectedResult),
(["5", "100", "0", "0"], invalidInputWidthExpectedResult)])
def test_invalid_input_change_city_size(invalidInput, expectedResult):
    """
    Tests invalid input in input width and input height
    """

    '''
    invalid height expected output:

    Welcome, mayor of Simp City!
    ----------------------------
    1. Start new game
    2. Load saved game
    3. Show high scores
    4. Choose building pool
    5. Choose city size
    
    0. Exit
    Your choice? 

    Enter value for width: 

    Invalid input has been entered. Please enter a number.

    Enter value for width: 

    City size will not be updated.

    --------- CURRENT CITY SIZE ---------
    Width: 4
    Height: 4
    -------------------------------------
    '''

    '''
    invalid width expected output:

    Welcome, mayor of Simp City!
    ----------------------------
    1. Start new game
    2. Load saved game
    3. Show high scores
    4. Choose building pool
    5. Choose city size
    
    0. Exit
    Your choice? 

    Enter value for width: 
    Enter value for height: 

    Invalid input has been entered. Please enter a number.

    Enter value for height: 

    City size will not be updated.

    --------- CURRENT CITY SIZE ---------
    Width: 4
    Height: 4
    -------------------------------------
    '''

    set_keyboard_input(invalidInput)

    with pytest.raises(SystemExit) as e:
        main()

    result = get_display_output()
    
    check = all(item in result for item in expectedResult)

    # assert result == False
    assert check == True