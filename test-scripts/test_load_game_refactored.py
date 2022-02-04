from cmath import exp
from attr import Factory
import pytest
import classes
import os
from main import *
from classes.game import *
from classes.menu import *
from tud_test_base import set_keyboard_input, get_display_output

pytestmark = [pytest.mark.skipif("load_game" not in dir(classes.menu), reason="load game not implemented"), 
              pytest.mark.skipif("generate_remaining_building_string" not in dir(classes.game.Game), reason="view remaining buildings on side implemented")]

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

corruptedSaveError = ["", "The current file is corrupt and will therefore be deleted."]

turnNumberArr = ["", "Turn 2"]

turnNumber = 2

printBoard3x3 = [
"     A     B     C           Building   Remaining",
"  +-----+-----+-----+        --------------------",
" 1| BCH |     |     |        HSE      | 8",
"  +-----+-----+-----+        FAC      | 8",
" 2|     |     |     |        SHP      | 8",
"  +-----+-----+-----+        HWY      | 8",
" 3|     |     |     |        BCH      | 7",
"  +-----+-----+-----+",]

printEmptyBoard4x4 = [
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

printBoard4x4 = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1| BCH |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+        HWY      | 8",
    " 3|     |     |     |     |        BCH      | 7",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]
   
printBoard5x5 = [
    "     A     B     C     D     E           Building   Remaining",
    "  +-----+-----+-----+-----+-----+        --------------------",
    " 1| BCH |     |     |     |     |        HSE      | 8",
    "  +-----+-----+-----+-----+-----+        FAC      | 8",
    " 2|     |     |     |     |     |        SHP      | 8",
    "  +-----+-----+-----+-----+-----+        HWY      | 8",
    " 3|     |     |     |     |     |        BCH      | 7",
    "  +-----+-----+-----+-----+-----+",
    " 4|     |     |     |     |     |",
    "  +-----+-----+-----+-----+-----+",
    " 5|     |     |     |     |     |",
    "  +-----+-----+-----+-----+-----+",
]

defaultBuildingPoolBoard = {"HSE":7, "FAC":7, "SHP": 8, "HWY":7, "BCH":7}
nonDefaultBuildingPoolBoard = {"MON":8, "PRK":7, "SHP": 7, "HWY":7, "BCH":7}

defaultBuildingHistory = {"1": ["SHP", "SHP"], "2": ["HSE", "HSE"], "3": ["FAC", "FAC"], "4": ["HWY", "HWY"], "5": ["SHP", "SHP"], "6": ["HSE", "HSE"]}
nonDefaultBuildingHistory = {"1": ["PRK", "PRK"], "2": ["HSE", "HSE"], "3": ["FAC", "FAC"], "4": ["MON", "MON"], "5": ["MON", "MON"], "6": ["HSE", "HSE"]}

defaultBuildingsAllBoard = [
[Building(), House(1, 0), Factory(2, 0), Highway(3, 0)],
[Beach(0, 1), Building(), Building(), Building()],
[Building(), Building(), Building(), Building()],
[Building(), Building(), Building(), Building()]]

nonDefaultBuildingsAllBoard = [
[Building(), Highway(1, 0), Park(2, 0), Shop(3, 0)],
[Beach(0, 1), Building(), Building(), Building()],
[Building(), Building(), Building(), Building()],
[Building(), Building(), Building(), Building()]]

defaultPrintBoard = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1| SHP | HSE | FAC | HWY |        HSE      | 7",
    "  +-----+-----+-----+-----+        FAC      | 7",
    " 2| BCH |     |     |     |        SHP      | 7",
    "  +-----+-----+-----+-----+        HWY      | 7",
    " 3|     |     |     |     |        BCH      | 7",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

nonDefaultPrintBoard = [
    "     A     B     C     D           Building   Remaining",
    "  +-----+-----+-----+-----+        --------------------",
    " 1| MON | HWY | PRK | SHP |        MON      | 7",
    "  +-----+-----+-----+-----+        PRK      | 7",
    " 2| BCH |     |     |     |        SHP      | 7",
    "  +-----+-----+-----+-----+        HWY      | 7",
    " 3|     |     |     |     |        BCH      | 7",
    "  +-----+-----+-----+-----+",
    " 4|     |     |     |     |",
    "  +-----+-----+-----+-----+"
]

@pytest.mark.order(1)
def test_load_game_no_save():
    """
    Tests the output in console of load game option in menu when there is no save file
    """
    savePath = './game_save.json'

    if os.path.exists(savePath):
        os.remove(savePath)
    else:
        print('no save found')

    set_keyboard_input(["2", "0", "0"])


    # calls main menu. if no save file is found, it should return to main menu without welcome message, with error message "No save game found!"
    with pytest.raises(SystemExit) as e:
        main()

    result = get_display_output()
    
    # expected result should be main menu, no save game found error then back to main menu without welcome message.
    assert result == mainMenu + noSaveError + mainMenuNoWelcome

@pytest.mark.order(2)
def test_load_game_empty_board():
    """
    Tests the output in console of load game option in menu with 4x4 empty board existing save
    """
    savePath = './game_save.json'

    if os.path.exists(savePath):
        os.remove(savePath)
    else:
        print('no save found')
    # starts a game and saves without building a building, then exits
    # this is to set up prerequisite 
    set_keyboard_input(["5", "0"])

    defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    test_game = Game()
    test_game.building_pool = defaultBuildingPool
    test_game.randomized_building_history = {"1": ["HSE", "HSE"]}
    test_game.start_new_turn()


    set_keyboard_input(["2", "0", "0"])

    # calls main menu and loads game, then starts a turn.
    with pytest.raises(SystemExit) as e:
        main()

    result = get_display_output()
    expectedResult = mainMenu + ["", "Turn 1"] + printEmptyBoard4x4 + gameMenu + mainMenuNoWelcome

    # expected result should be main menu to game with turn 1 and empty board with game menu
    assert result == expectedResult

    check = all(item in result for item in expectedResult)

    assert check == True

    # tests whether the returned game object has the correct values for the variables inside
    # unable to test for game obj
    loadedGame = load_game()
    assert loadedGame.building_pool == defaultBuildingPool
    assert loadedGame.turn_num == 1
    assert loadedGame.randomized_building_history == {"1": ["HSE", "HSE"]}

@pytest.mark.order(3)
@pytest.mark.parametrize("printBoard, boardSize",
[(printBoard3x3, 3),
(printBoard4x4, 4),
(printBoard5x5, 5)])
def test_load_game_with_save_different_board_sizes(printBoard, boardSize):
    """
    Tests the output in console of load game option in menu with existing save
    """
    savePath = './game_save.json'

    if os.path.exists(savePath):
        os.remove(savePath)
    else:
        print('no save found')

    set_keyboard_input(["1", "a1", "5", "0"])
    
    defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    # starts a game with different board sizes (3x3, 4x4, 5x5) to set up prerequisites.
    # turn number is 2, and BCH is built in a1 spot
    test_game = Game(height = boardSize, width = boardSize)
    test_game.building_pool = defaultBuildingPool
    test_game.turn_num = 1
    test_game.randomized_building_history = {"1": ["BCH", "BCH"], "2": ["HSE", "HSE"]}
    test_game.start_new_turn()

    # checkResult = get_display_output()
    # assert checkResult == [""]
    set_keyboard_input(["2", "0", "0"])

    # calls main menu to load game.
    with pytest.raises(SystemExit) as e:
        main()

    result = get_display_output()
    expectedResult = mainMenu + turnNumberArr + printBoard + gameMenu + mainMenuNoWelcome
    # expected result should be main menu to game with turn 2, and board with BCH in a1 on all sizes with game menu.

    assert result == expectedResult
    check = all(item in result for item in expectedResult)
    assert check == True

    # tests whether the returned game object has the correct values for the variables inside
    # unable to test for game board obj as errors will be thrown not due to the dev code
    loadedGame = load_game()
    assert loadedGame.building_pool == {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":7}
    assert loadedGame.turn_num == 2
    assert loadedGame.randomized_building_history == {"1": ["BCH", "BCH"], "2": ["HSE", "HSE"]}

@pytest.mark.order(4)
@pytest.mark.parametrize("board, testPrintBoard, buildingPool, buildingHistory", [
(defaultBuildingsAllBoard, defaultPrintBoard, defaultBuildingPoolBoard, defaultBuildingHistory),
(nonDefaultBuildingsAllBoard, nonDefaultPrintBoard, nonDefaultBuildingPoolBoard, nonDefaultBuildingHistory)])
def test_load_game_with_all_buildings(board, testPrintBoard, buildingPool, buildingHistory):
    """
    Tests the output in console of load game option in menu with existing save with all buildings on board
    """
    savePath = './game_save.json'

    if os.path.exists(savePath):
        os.remove(savePath)
    else:
        print('no save found')

    set_keyboard_input(["1", "a1", "5", "0"])
    


    # turn number is 2, and BCH is built in a1 spot
    test_game = Game(height = 4, width = 4, building_pool = buildingPool)
    # test_game.building_pool = buildingPool
    test_game.board = board
    test_game.turn_num = 5
    test_game.randomized_building_history = buildingHistory
    test_game.start_new_turn()

    # checkResult = get_display_output()
    # assert checkResult == [""]
    set_keyboard_input(["2", "0", "0"])

    # calls main menu to load game.
    with pytest.raises(SystemExit) as e:
        main()

    result = get_display_output()
    expectedResult = mainMenu + ["", "Turn 6"] + testPrintBoard + gameMenu + mainMenuNoWelcome
    # expected result should be main menu to game with turn 2, and board with BCH in a1 on all sizes with game menu.

    assert result == expectedResult
    check = all(item in result for item in expectedResult)
    assert check == True

    # tests whether the returned game object has the correct values for the variables inside
    # unable to test for game board obj as errors will be thrown not due to the dev code
    loadedGame = load_game()
    assert loadedGame.building_pool == buildingPool
    assert loadedGame.turn_num == 6
    assert loadedGame.randomized_building_history == buildingHistory

@pytest.mark.order(5)
@pytest.mark.parametrize("corruptStr", [
    ("asdf"), ("1234"), (""), ('{"board": {"1,1": "PRK"}, "turn_num": 2, "width": 4, "height": 4}'),
    ('{"boardasdf": {"0,0": "SHP"}, "turn_num": 2, "width": 4, "height": 4, "randomized_history": {"1": ["SHP", "SHP"], "2": ["BCH", "HWY"]}, "building_pool": {"HSE": 8, "FAC": 8, "SHP": 7, "HWY": 8, "BCH": 8}}')
])
def test_load_game_corrupted_save(corruptStr):
    savePath = './game_save.json'
    with open(savePath, "w") as save:
            save.write(corruptStr)

    set_keyboard_input(["2", "2", "0", "0"])


    # calls main menu. if save file is corrupted, it should return to main menu without welcome message, with error message "Failed to load game!"
    with pytest.raises(SystemExit) as e:
        main()

    result = get_display_output()
    
    # expected result should be main menu, no save game found error then back to main menu without welcome message.
    assert result == mainMenu + corruptedSaveError + mainMenuNoWelcome + noSaveError + mainMenuNoWelcome