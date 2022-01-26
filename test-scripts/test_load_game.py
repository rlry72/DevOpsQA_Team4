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

saveBoard3x3 = [
[Beach(0, 0), Building(), Building()],
[Building(), Building(), Building()],
[Building(), Building(), Building()]]

saveEmptyBoard4x4 = [
[Building(), Building(), Building(), Building()],
[Building(), Building(), Building(), Building()],
[Building(), Building(), Building(), Building()],
[Building(), Building(), Building(), Building()]]

saveBoard4x4 = [
[Beach(0, 0), Building(), Building(), Building()],
[Building(), Building(), Building(), Building()],
[Building(), Building(), Building(), Building()],
[Building(), Building(), Building(), Building()]]

saveBoard5x5 = [
[Beach(0, 0), Building(), Building(), Building(), Building()],
[Building(), Building(), Building(), Building(), Building()],
[Building(), Building(), Building(), Building(), Building()],
[Building(), Building(), Building(), Building(), Building()],
[Building(), Building(), Building(), Building(), Building()]]

jsonBoard3x3 = {"0,0": "BCH", }

def test_load_game_no_save():
    """
    Tests the output in console of load game option in menu when there is no save file
    """
    set_keyboard_input(["2", "0"])

    mainMenu = main_menu()
    if mainMenu == "2":
        load_game()
        main_menu(True)
    
    result = get_display_output()

    assert result == mainMenu + noSaveError + mainMenuNoWelcome

def test_load_game_empty_board():
    """
    Tests the output in console of load game option in menu with 4x4 board existing save
    """
    set_keyboard_input(["5", "0"])

    test_game = Game()
    test_game.randomized_building_history = {"1": ["HSE", "HSE"]}
    test_game.start_new_turn()


    set_keyboard_input(["2"])

    mainMenu = main_menu()
    if mainMenu == "2":
        loadedGame = load_game()

    result = get_display_output()

    assert loadedGame == saveEmptyBoard4x4
    assert result == mainMenu + ["", "Turn 1"] + printEmptyBoard4x4 + gameMenu


@pytest.mark.parametrize("saveBoard, printBoard, boardSize, boardJson",
(saveBoard3x3, printBoard3x3, 3),
(saveBoard4x4, printBoard4x4, 4),
(saveBoard5x5, printBoard5x5, 5))
def test_load_game_with_save_different_board_sizes(saveBoard, printBoard, boardSize):
    """
    Tests the output in console of load game option in menu with existing save
    """
    set_keyboard_input(["1", "5", "0"])

    test_game = Game(height = boardSize, width = boardSize)
    test_game.turn_num = turnNumber
    test_game.randomized_building_history = {"1": ["BCH", "BCH"], "2": ["HSE", "HSE"]}
    test_game.start_new_turn()


    set_keyboard_input(["2"])

    mainMenu = main_menu()
    if mainMenu == "2":
        loadedGame = load_game()

    result = get_display_output()

    assert loadedGame == saveBoard
    assert result == mainMenu + turnNumberArr + printBoard + gameMenu
