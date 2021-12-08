import pytest
from tud_test_base import set_keyboard_input, get_display_output
from classes.menu import *
from classes.game import *


def test_game_menu_display_board_options():
    set_keyboard_input(["0"])
    test_game = Game()
    test_game.start_new_turn()
    result = get_display_output()
    
    assert result == ["Turn 1",
    "    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+",
    "1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\n",
    "Your choice? "]



@pytest.mark.parametrize("invalidInput, expectedResult", 
[("-1", ["Invalid input, please try again", "Your choice? "]), ("asdf", ["Invalid input, please try again", "Your choice? "]), 
("13@!$`a", ["Invalid input, please try again", "Your choice? "]), (9, ["Invalid input, please try again", "Your choice? "]), ("", ["Invalid input, please try again", "Your choice? "])])
def test_game_menu_invalid_input(invalidInput, expectedResult):
    set_keyboard_input(["1", "1", invalidInput, "0"])
    testGame = Game()
    testGame.start_new_turn()
    result = get_display_output()[-2:]
    assert result == expectedResult


def test_game_menu_return_main_menu():

    set_keyboard_input(["1", "0", "0"])
    expectedOutput = ["Welcome, mayor of Simp City!        \n----------------------------\n1. Start new game\n2. Load saved game\n0. Exit\n",
    "Your choice? "]
    selection = Game().start_new_turn()
    if selection == 0:
        result = get_display_output()
        assert result == expectedOutput