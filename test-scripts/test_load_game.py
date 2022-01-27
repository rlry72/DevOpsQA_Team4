import pytest
from classes.game import *
from classes.menu import *
from tud_test_base import set_keyboard_input, get_display_output

mainMenu = ["Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
    "Your choice? "]

mainMenuNoWelcome = ["\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
    "Your choice? "]

gameMenu = ['1. Build a HSE',
            '2. Build a HSE', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

noSaveError = ["", "No save game found!"]

turnNumberArr = ["", "Turn 2"]

turnNumber = 2

printBoard3x3 = [
"     A     B     C  ",
"  +-----+-----+-----+",
" 1| BCH |     |     |",
"  +-----+-----+-----+",
" 2|     |     |     |",
"  +-----+-----+-----+",
" 3|     |     |     |",
"  +-----+-----+-----+",]

printEmptyBoard4x4 = [
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

printBoard4x4 = [
"     A     B     C     D  ",
"  +-----+-----+-----+-----+",
" 1| BCH |     |     |     |",
"  +-----+-----+-----+-----+",
" 2|     |     |     |     |",
"  +-----+-----+-----+-----+",
" 3|     |     |     |     |",
"  +-----+-----+-----+-----+",
" 4|     |     |     |     |",
"  +-----+-----+-----+-----+",]
   
printBoard5x5 = [
"     A     B     C     D     E  ",
"  +-----+-----+-----+-----+-----+",
" 1| BCH |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 2|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 3|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 4|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 5|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",]


def test_load_game_no_save():
    """
    Tests the output in console of load game option in menu when there is no save file
    """
    set_keyboard_input(["2", "0"])

    # calls main menu. if no save file is found, it should return to main menu without welcome message, with error message "No save game found!"
    menu = main_menu()
    if menu == "2":
        loadedGame = load_game()
        if loadedGame == False:
            main_menu(True)
    
    result = get_display_output()

    # expected result should be main menu, no save game found error then back to main menu without welcome message.
    assert result == mainMenu + noSaveError + mainMenuNoWelcome

def test_load_game_empty_board():
    """
    Tests the output in console of load game option in menu with 4x4 empty board existing save
    """
    # starts a game and saves without building a building, then exits
    # this is to set up prerequisite 
    set_keyboard_input(["5", "0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["HSE", "HSE"]}
    test_game.start_new_turn()


    set_keyboard_input(["2"])

    # calls main menu and loads game, then starts a turn.
    menu = main_menu()
    if menu == "2":
        loadedGame = load_game()
        loadedGame.start_new_turn()

    result = get_display_output()

    # expected result should be main menu to game with turn 1 and empty board with game menu
    assert result == mainMenu + ["", "Turn 1"] + printEmptyBoard4x4 + gameMenu


@pytest.mark.parametrize("printBoard, boardSize",
[(printBoard3x3, 3),
(printBoard4x4, 4),
(printBoard5x5, 5)])
def test_load_game_with_save_different_board_sizes(printBoard, boardSize):
    """
    Tests the output in console of load game option in menu with existing save
    """
    set_keyboard_input(["1", "a1", "5", "0"])

    # starts a game with different board sizes (3x3, 4x4, 5x5) to set up prerequisites.
    # turn number is 2, and BCH is built in a1 spot
    test_game = Game(height = boardSize, width = boardSize)
    test_game.turn_num = turnNumber
    test_game.randomized_building_history = {"1": ["BCH", "BCH"], "2": ["HSE", "HSE"]}
    test_game.start_new_turn()


    set_keyboard_input(["2", "0"])

    # calls main menu to load game.
    menu = main_menu()
    if menu == "2":
        loadedGame = load_game()
        loadedGame.start_new_turn()

    result = get_display_output()

    # expected result should be main menu to game with turn 2, and board with BCH in a1 on all sizes with game menu.
    assert result == mainMenu + turnNumberArr + printBoard + gameMenu
