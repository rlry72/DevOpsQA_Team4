import pytest
import classes
from tud_test_base import set_keyboard_input, get_display_output
from classes.menu import *
from classes.game import *

pytestmark = pytest.mark.skipif("generate_remaining_building_string" not in dir(classes.game.Game), reason="view remaining buildings on side not implemented")

mainMenuNoWelcome = ["\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
    "Your choice? "]

turnNumber = ["", "Turn 1"]

gameBoard = [
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

gameMenu = ['1. Build a HSE',
            '2. Build a HSE', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

invalidInputList = ['Invalid Input. Please enter a valid input ("1" / "2" / "3" / "4" / "5" / "0").', "Your choice? "]

defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}


def test_game_menu_display_board():
    """
    Tests if the game board is displayed properly upon starting a new game
    Starts a new game and checks the game output against what the proper output should be.
    """
    # set input 0, but first input will be ignored.
    set_keyboard_input(["0"])
    # start new game and turn
    test_game = Game()
    test_game.building_pool = defaultBuildingPool
    test_game.start_new_turn()
    # get what is printed in the console
    result = get_display_output()
    
    expectedResult = turnNumber + gameBoard

    # compares what is printed in console with what should be shown. if different, test fails.
    for line in range(len(expectedResult)):
        assert result[line] == expectedResult[line]



def test_game_menu_display_options():
    """
    Tests if the game options (only game options) are displayed properly upon starting a new game
    Starts a new game and checks the game output against what the proper output should be.
    """
    # set input 0, but first input will be ignored.
    set_keyboard_input(["0"])
    # start new game and turn
    test_game = Game()
    test_game.building_pool = defaultBuildingPool
    test_game.randomized_building_history = {"1": ["HSE", "HSE"]}
    test_game.start_new_turn()
    # get what is printed in the console
    result = get_display_output()[-8:]
    
    # compares what is printed in console with what should be shown. if different, test fails.
    assert result == gameMenu


def test_game_menu_display_board_options():
    """
    Tests if the game menu (game board and game options) are displayed properly upon starting a new game
    Starts a new game and checks the game output against what the proper output should be.
    """
    # set input 0, but first input will be ignored.
    set_keyboard_input(["0"])
    # start new game and turn
    test_game = Game()
    test_game.randomized_building_history = {"1": ["HSE", "HSE"]}
    test_game.building_pool = defaultBuildingPool
    test_game.start_new_turn()
    # get what is printed in the console
    result = get_display_output()
    
    # compares what is printed in console with what should be shown. if different, test fails.
    assert result == turnNumber + gameBoard + gameMenu



@pytest.mark.parametrize("invalidInput, expectedResult", 
[("-1", invalidInputList), ("asdf", invalidInputList), 
("13@!$`a", invalidInputList), (9, invalidInputList), ("", invalidInputList)])
def test_game_menu_invalid_input(invalidInput, expectedResult):
    """
    Runs a set of invalid inputs to test the input failure and message in the game menu. Tests to check if output messages are correct.
    Invalid inputs are values outside of 0, 1, 2, 3, 4 and 5. 
    Tested invalid inputs: special characters, integers, strings, out of bound number string.
    """
    # set input to start new game, then set invalid input and exit
    set_keyboard_input([invalidInput, "0"])
    # start game and new turn
    testGame = Game().start_new_turn()
    # get the LAST TWO items printed in console. These last two items must be "Invalid input, please try again" and "Your choice? "
    result = get_display_output()[-2:]
    # compares console output to expected result set in pytest mark parametrize. if different, test fails
    assert result == expectedResult



def test_game_menu_return_main_menu():
    """
    Tests if the game can return to the main menu from the game menu. Tests to make sure the output in console is correct and main menu is displayed.
    """
    # set keyboard input to 0, then 0. (ignores 1)
    set_keyboard_input(["0", "0"])
    # set expected output to that of main menu string
    expectedOutput = mainMenuNoWelcome
    # starts a new game and new turn and enters game menu
    selection = Game().start_new_turn()
    # if input in game menu is 0,
    if selection == "0":
        # get output messages in console
        result = get_display_output()
        # compares output messages with the expected output set above. if different, test fails
        assert result == expectedOutput