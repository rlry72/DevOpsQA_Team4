from unittest import expectedFailure
import pytest
import os
import sys
import json
from io import StringIO 
from unittest.mock import Mock
from tud_test_base import set_keyboard_input, get_display_output
from classes.game import *
from classes.menu import *
import classes

pytestmark = pytest.mark.skipif("update_high_score" not in dir(classes.game.Game), reason="update high score not implemented")

mainMenuNoWelcome = ["\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
                     "Your choice? "]


finalLayoutMsg = ["Final layout of Simp City:"]


emptyGameBoard4x1 = [
    "     A     B     C     D  ",
    "  +-----+-----+-----+-----+",
    " 1|     |     |     |     |",
    "  +-----+-----+-----+-----+",       
]

gameBoard2x2_1 = [
    [Highway(0,0), Highway(1,0)],
    [Shop(0,1), House(1,1)]
    ]

board2x2Filled_1 = [
    "     A     B  ",
    "  +-----+-----+",
    " 1| HWY | HWY |",
    "  +-----+-----+",
    " 2| SHP | HSE |",
    "  +-----+-----+",]

score_computation_2x2_1 = [
    "HSE: 1 = 1", 
    "FAC: 0",
    "SHP: 2 = 2",
    "HWY: 2 + 2 = 4",
    "BCH: 0",
    "Total score: 7"
    ]



def get_position(filename, score):
    """
    Get the position of the player from High Score List files.  
    """

    position = 0
    
    fileExist = os.path.exists(filename)
    if fileExist:
        f = open(filename)
        data = json.load(f)
        f.close()
        high_score_list = data["high_scores"]
        if len(high_score_list) != 0:
            for high_score in high_score_list:
                if score > int(high_score["score"]):
                    position += 1
                    break
                position += 1       
    else:
        position = 1
    return position

@pytest.mark.order(1)
def test_update_high_scores_diff_citysize_same_cityarea_samename():
    """
    Test whether the application will display the high scores of different city sizes that are same city area into the same high score list.
    It also test whether the system accepts same name for different players in the high score list.
    """ 

    board4x1Filled_1 = [
        "     A     B     C     D  ",
        "  +-----+-----+-----+-----+",
        " 1| FAC | FAC | FAC | FAC |",
        "  +-----+-----+-----+-----+",       
    ]
    
    gameBoard4x1_1 = [
    [Factory(0,0), Factory(1,0), Factory(2,0), Factory(3,0)]
    ]   

    score_computation_4x1_1 = [
        "HSE: 0", 
        "FAC: 4 + 4 + 4 + 4 = 16",
        "SHP: 0",
        "HWY: 0",
        "BCH: 0",
        "Total score: 16"
    ]

    high_score_list_2x2_1 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. HelloWorldHeyDevOps       7",
        "-------------------------------"
    ]

    high_score_list_4x1_1 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. HelloWorldHeyDevOps      16",
        " 2. HelloWorldHeyDevOps       7",
        "-------------------------------"
    ]    
   
    position = get_position("high_score_4.json", 7)  
    congratsMsg = ["Congratulations! You made the high score board at position " + str(position) + "!",
                    "Please enter your name (max 20 chars): "]
    
    set_keyboard_input(["HelloWorldHeyDevOps", "0", "HelloWorldHeyDevOps","0"])
    
    defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    test_game = Game(width = 2, height = 2)
    test_game.building_pool = defaultBuildingPool
    test_game.board = gameBoard2x2_1 
    test_game.turn_num = 5
    test_game.start_new_turn()
    main_menu(True)
    position = get_position("high_score_4.json", 7)  

    defaultBuildingPool2 = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    test_game_2 = Game(width = 4, height = 1)
    test_game_2.building_pool = defaultBuildingPool2
    test_game_2.board = gameBoard4x1_1
    test_game_2.turn_num = 5
    test_game_2.start_new_turn()
    main_menu(True)
    position = get_position("high_score_4.json", 7)
    result = get_display_output()

    assert result == [""] + finalLayoutMsg + board2x2Filled_1 + score_computation_2x2_1 + congratsMsg \
                     + [""] + high_score_list_2x2_1 + mainMenuNoWelcome + [""] \
                     + finalLayoutMsg + board4x1Filled_1 + score_computation_4x1_1 + congratsMsg \
                     + [""] + high_score_list_4x1_1  + mainMenuNoWelcome


@pytest.mark.order(3)
def test_update_high_scores_invalid_name():
    """
    Test whether the system will display error messages when an invalid input for name is entered.
    """

    error_message = [
        "Invalid input for the name has been entered.",
        "Please remember only a max of 20 characters are allowed for the name.",
        "",
        "Please enter your name (max 20 chars): "
        ]

    set_keyboard_input(["HelloWorldHeyHeyDevOps","0"])
    
    defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    test_game = Game(width = 2, height = 2)
    test_game.building_pool = defaultBuildingPool
    test_game.board = gameBoard2x2_1
    test_game.turn_num = 5
    test_game.start_new_turn()
    position = get_position("high_score_4.json", 7)  
    congratsMsg = ["Congratulations! You made the high score board at position " + str(position) + "!",
                    "Please enter your name (max 20 chars): "]
    result = get_display_output()
    
    #assert result ==[""] + finalLayoutMsg + board2x2Filled_1 + score_computation_2x2_1 + congratsMsg +[""] + error_message
    expectedResult= [""] + finalLayoutMsg + board2x2Filled_1 + score_computation_2x2_1 + congratsMsg +[""] + error_message

    check = all(item in result for item in expectedResult)
    assert check == True

@pytest.mark.order(2)
def test_update_high_scores_same_score_lower_position():
    """
    Test whether the position of the current player will be lowered than the previous players that have the same scores.
    """
    
    


    high_score_list_2x2_2 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. HelloWorldHeyDevOps      16",
        " 2. HelloWorldHeyDevOps       7",
        " 3. Player 2                  7",
        "-------------------------------"
    ]

    set_keyboard_input(["Player 2","0", "0"])
    
    defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    test_game = Game(width = 2, height = 2)
    test_game.building_pool = defaultBuildingPool
    test_game.board = gameBoard2x2_1
    test_game.turn_num = 5
    test_game.start_new_turn()
    main_menu(True)
    position = get_position("high_score_4.json", 7)  
    congratsMsg = ["Congratulations! You made the high score board at position " + str(position) + "!",
                    "Please enter your name (max 20 chars): "]
    result = get_display_output()

    assert result == [""] + finalLayoutMsg + board2x2Filled_1 + score_computation_2x2_1 + congratsMsg \
                    + [""] + high_score_list_2x2_2 + mainMenuNoWelcome


@pytest.mark.order(4)
def test_update_high_scores_never_got_top_10():
    """
    Test whether the user will return back to the main menu without prompting for name when the user never got into the top 10.
    """
    
    gameBoard3x1_1 = [
    [House(0,0), Factory(1,0), House(2,0)]
    ]

    board3x1Filled_1 = [
        "     A     B     C  ",        
        "  +-----+-----+-----+",        
        " 1| HSE | FAC | HSE |",
        "  +-----+-----+-----+",       
    ]     

    score_computation_3x1_1 = [
        "HSE: 1 + 1 = 2", 
        "FAC: 1 = 1",
        "SHP: 0",
        "HWY: 0",
        "BCH: 0",
        "Total score: 3"
    ]

    set_keyboard_input(["0","0"])

    defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    test_game = Game(width = 3, height = 1)
    test_game.building_pool = defaultBuildingPool
    test_game.board = gameBoard3x1_1
    test_game.turn_num = 4
    test_game.start_new_turn()
    main_menu(True)

    result = get_display_output()
    assert result == [""] + finalLayoutMsg + board3x1Filled_1 + score_computation_3x1_1 + mainMenuNoWelcome


@pytest.mark.order(5)
def test_update_high_scores_only_got_10_players_in_list():
    """
    Test whether the high score list will only have the top 10 players.
    """

    position = get_position("high_score_3.json", 9)  
    congratsMsg = ["Congratulations! You made the high score board at position " + str(position) + "!",
                    "Please enter your name (max 20 chars): "]

    gameBoard3x1_2 = [
    [Highway(0,0), Highway(1,0), Highway(2,0)]
    ]

    board3x1Filled_2 = [
        "     A     B     C  ",        
        "  +-----+-----+-----+",        
        " 1| HWY | HWY | HWY |",
        "  +-----+-----+-----+",       
    ]  

    score_computation_3x1_2 = [
        "HSE: 0", 
        "FAC: 0",
        "SHP: 0",
        "HWY: 3 + 3 + 3 = 9",
        "BCH: 0",
        "Total score: 9"
    ]
    
    high_score_list_3x1_2 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. Player1                   9",
        " 2. Player2                   9",
        " 3. Player3                   9",
        " 4. Player                    9",
        " 5. Player4                   5",
        " 6. Player5                   5",
        " 7. Player6                   5",
        " 8. Player7                   5",
        " 9. Player8                   5",
        "10. Player9                   5",
        "-------------------------------"
    ]

    set_keyboard_input(["Player","0","0"])

    defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    test_game = Game(width = 3, height = 1)
    test_game.building_pool = defaultBuildingPool
    test_game.board = gameBoard3x1_2
    test_game.turn_num = 4
    test_game.start_new_turn()
    main_menu(True)

    result = get_display_output()
    assert result == [""] + finalLayoutMsg + board3x1Filled_2 + score_computation_3x1_2 + congratsMsg \
                    + [""] + high_score_list_3x1_2 + mainMenuNoWelcome


@pytest.mark.order(6)
def test_update_high_scores_display_separately_for_diff_city_area():
    """
    Test whether the high score list for different city areas will display separately
    """
    
    congratsMsg = ["Congratulations! You made the high score board at position 1!",
                    "Please enter your name (max 20 chars): "]
    
    gameBoard1x1_1 = [
    [Highway(0,0)]
    ]
    
    gameBoard2x1_1 = [
    [Highway(0,0), Highway(1,0)]
    ]

    board1x1Filled_1 = [
        "     A  ",        
        "  +-----+",        
        " 1| HWY |",
        "  +-----+",       
    ]  

    board2x1Filled_1 = [
        "     A     B  ",        
        "  +-----+-----+",        
        " 1| HWY | HWY |",
        "  +-----+-----+",       
    ] 

    score_computation_1x1_1 = [
        "HSE: 0", 
        "FAC: 0",
        "SHP: 0",
        "HWY: 1 = 1",
        "BCH: 0",
        "Total score: 1"
    ]

    score_computation_2x1_1 = [
        "HSE: 0", 
        "FAC: 0",
        "SHP: 0",
        "HWY: 2 + 2 = 4",
        "BCH: 0",
        "Total score: 4"
    ]
    
    high_score_list_1x1_1 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. First Game                1",        
        "-------------------------------"
    ]

    high_score_list_2x1_1 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. Second Game               4",        
        "-------------------------------"
    ]    


    set_keyboard_input(["First Game", "0", "Second Game","0"])
    
    defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    test_game = Game(width = 1, height = 1)
    test_game.building_pool = defaultBuildingPool
    test_game.board = gameBoard1x1_1 
    test_game.turn_num = 2
    test_game.start_new_turn()
    main_menu(True)

    defaultBuildingPool2 = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    test_game_2 = Game(width = 2, height = 1)
    test_game_2.building_pool = defaultBuildingPool2
    test_game_2.board = gameBoard2x1_1
    test_game_2.turn_num = 3
    test_game_2.start_new_turn()
    main_menu(True)

    result = get_display_output()

    assert result == [""] + finalLayoutMsg + board1x1Filled_1 + score_computation_1x1_1 + congratsMsg \
                     + [""] + high_score_list_1x1_1 + mainMenuNoWelcome + [""] \
                     + finalLayoutMsg + board2x1Filled_1 + score_computation_2x1_1 + congratsMsg \
                     + [""] + high_score_list_2x1_1 +  mainMenuNoWelcome

@pytest.mark.order(7)
@pytest.mark.xfail(reason = "It will fail as setkeyboard does not work as expected, it will convert string input \ n to new line character")
def test_update_high_scores_special_character_in_input():
    """
    Test whether the system will escape and display special characters for name 
    """

    gameBoard5x1_1 = [
    [Factory(0,0), Factory(1,0), Factory(2,0), Factory(3,0), Factory(4,0)]
    ]   


    board5x1Filled_1 = [
        "     A     B     C     D     E  ",
        "  +-----+-----+-----+-----+-----+",
        " 1| FAC | FAC | FAC | FAC | FAC |",
        "  +-----+-----+-----+-----+-----+",       
    ]
    score_computation_5x1_1 = [
        "HSE: 0", 
        "FAC: 4 + 4 + 4 + 4 + 1 = 17",
        "SHP: 0",
        "HWY: 0",
        "BCH: 0",
        "Total score: 17"
    ]

    high_score_list_5x1_1 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. HelloWorld\\nHeyDevOp     17",
        "-------------------------------"
    ]


    congratsMsg = ["Congratulations! You made the high score board at position 1!",
                    "Please enter your name (max 20 chars): "]

    set_keyboard_input(["HelloWorld\nHeyDevOp"])
    
    defaultBuildingPool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}

    test_game = Game(width = 5, height = 1)
    test_game.building_pool = defaultBuildingPool
    test_game.board = gameBoard5x1_1
    test_game.turn_num = 6
    test_game.start_new_turn()

    result = get_display_output()

    assert result == [""] + finalLayoutMsg + board5x1Filled_1 + score_computation_5x1_1 + congratsMsg +[""] + high_score_list_5x1_1\
                    + mainMenuNoWelcome 

    