import pytest
from tud_test_base import set_keyboard_input, get_display_output
from classes.menu import *
from classes.game import *

def test_game_menu_display_board():
    """
    Tests if the game board is displayed properly upon starting a new game
    Starts a new game and checks the game output against what the proper output should be.
    """
    # set input 0, but first input will be ignored.
    set_keyboard_input(["0"])
    # start new game and turn
    test_game = Game()
    test_game.start_new_turn()
    # get what is printed in the console
    result = get_display_output()
    
    # compares what is printed in console with what should be shown. if different, test fails.
    assert result == ["Turn 1"
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    ]


def test_game_menu_display_options():
    """
    Tests if the game options (only game options) are displayed properly upon starting a new game
    Starts a new game and checks the game output against what the proper output should be.
    """
    # set input 0, but first input will be ignored.
    set_keyboard_input(["0"])
    # start new game and turn
    test_game = Game()
    test_game.start_new_turn()
    # get what is printed in the console
    result = get_display_output()[2:4]
    
    # compares what is printed in console with what should be shown. if different, test fails.
    assert result == [
    "1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\n",
    "Your choice? "    ]


def test_game_menu_display_board_options():
    """
    Tests if the game menu (game board and game options) are displayed properly upon starting a new game
    Starts a new game and checks the game output against what the proper output should be.
    """
    # set input 0, but first input will be ignored.
    set_keyboard_input(["0"])
    # start new game and turn
    test_game = Game()
    test_game.start_new_turn()
    # get what is printed in the console
    result = get_display_output()
    
    # compares what is printed in console with what should be shown. if different, test fails.
    assert result == ["Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\n",
    "Your choice? "]



@pytest.mark.parametrize("invalidInput, expectedResult", 
[("-1", ['Please enter a valid input ("1" / "2" / "3" / "4" / "5" / "0").', "Your choice? "]), ("asdf", ['Please enter a valid input ("1" / "2" / "3" / "4" / "5" / "0").', "Your choice? "]), 
("13@!$`a", ['Please enter a valid input ("1" / "2" / "3" / "4" / "5" / "0").', "Your choice? "]), (9, ['Please enter a valid input ("1" / "2" / "3" / "4" / "5" / "0").', "Your choice? "]), ("", ["Invalid input, please try again", "Your choice? "])])
def test_game_menu_invalid_input(invalidInput, expectedResult):
    """
    Runs a set of invalid inputs to test the input failure and message in the game menu. Tests to check if output messages are correct.
    Invalid inputs are values outside of 0, 1, 2, 3, 4 and 5. 
    Tested invalid inputs: special characters, integers, strings, out of bound number string.
    """
    # set input to start new game, then set invalid input and exit
    set_keyboard_input(["1", "1", invalidInput, "0"])
    # start game and new turn
    testGame = Game()
    testGame.start_new_turn()
    # get the LAST TWO items printed in console. These last two items must be "Invalid input, please try again" and "Your choice? "
    result = get_display_output()[-2:]
    # compares console output to expected result set in pytest mark parametrize. if different, test fails
    assert result == expectedResult



def test_game_menu_return_main_menu():
    """
    Tests if the game can return to the main menu from the game menu. Tests to make sure the output in console is correct and main menu is displayed.
    """
    # set keyboard input to 0, then 0. (ignores 1)
    set_keyboard_input(["1", "0", "0"])
    # set expected output to that of main menu string
    expectedOutput = ["Welcome, mayor of Simp City!        \n----------------------------\n1. Start new game\n2. Load saved game\n0. Exit\n",
    "Your choice? "]
    # starts a new game and new turn and enters game menu
    selection = Game().start_new_turn()
    # if input in game menu is 0,
    if selection == 0:
        # get output messages in console
        result = get_display_output()
        # compares output messages with the expected output set above. if different, test fails
        assert result == expectedOutput