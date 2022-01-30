
import pytest
import os
import sys
import json
from io import StringIO 
from unittest.mock import Mock
from tud_test_base import set_keyboard_input, get_display_output
from classes.game import *
from classes.menu import *



mainMenuNoWelcome = ["\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
                     "Your choice? "]


gameMenu = ['1. Build a FAC',
            '2. Build a FAC', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

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

choose_city_size_msg = [
    "Choose your city size below. Please take note that the multiplication of width and height cannot be more than 40.",
    "Enter 0 to exit this configuration."
]

prompt_width = ["Enter value for width: "]
prompt_height = ["Enter value for height: "]

chosen_city_size_4x1_1 = [
    "--------- CHOSEN CITY SIZE ---------",
    "Width: 4",
    "Height: 1",
    "------------------------------------"
]
current_city_size_2x2_1 = [
    "--------- CURRENT CITY SIZE ---------",
    "Width: 2",
    "Height: 2",
    "-------------------------------------"
]


# .json should be included in filename
def get_position(filename, score):
    position = 0

    fileExist = os.path.exists('./' + filename)
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


def test_update_high_scores_diff_citysize_same_cityarea_samename(finalLayoutMsg, gameBoard2x2_1, board2x2Filled_1,score_computation_2x2_1):
    

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
        " 1. HelloWorld\\nHeyDevOp      7",
        "-------------------------------"
    ]

    high_score_list_4x1_1 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. HelloWorld\\nHeyDevOp     16",
        " 2. HelloWorld\\nHeyDevOp      7",
        "-------------------------------"
    ]

      
   

    position = get_position("high_score_4.json", 7)  
    congratsMsg = ["Congratulations! You made the high score board at position " + str(position) + "!",
                    "Please enter your name (max 20 chars):"]

    
    set_keyboard_input(["HelloWorld\nHeyDevOp", "0", "HelloWorld\nHeyDevOp"])

    test_game = Game(width = 2, height = 2)
    test_game.board = gameBoard2x2_1 
    test_game.turn_num = 5
    test_game.start_new_turn()
    main_menu(True)
    test_game_2 = Game(width = 4, height = 1)
    test_game_2.board = gameBoard4x1_1
    test_game_2.turn_num = 5
    test_game_2.start_new_turn()
    main_menu(True)

    result = get_display_output()

    assert result == [""] + finalLayoutMsg + board2x2Filled_1 + score_computation_2x2_1 + congratsMsg \
                     + [""] + high_score_list_2x2_1 + [""] + mainMenuNoWelcome + [""] \
                     + finalLayoutMsg + board4x1Filled_1 + score_computation_4x1_1 + congratsMsg \
                     + [""] + high_score_list_4x1_1 + [""] + mainMenuNoWelcome

                 
     
    '''    
    + current_city_size_2x2_1 + [""] + choose_city_size_msg +[""] \    
    + prompt_width + prompt_height + [""] + chosen_city_size_4x1_1 + [""] \
    + mainMenuNoWelcome + [""] 
    '''

def test_update_high_scores_invalid_name(finalLayoutMsg, gameBoard2x2_1, board2x2Filled_1,score_computation_2x2_1):

    error_message = [
        "Invalid input for the name has been entered. ",
        "Please remember only a max of 20 characters are allowed for the name.",
        "",
        "Please enter your name (max 20 chars):"
        ]

    position = get_position("high_score_4.json", 7)  
    congratsMsg = ["Congratulations! You made the high score board at position " + str(position) + "!",
                    "Please enter your name (max 20 chars):"]


    set_keyboard_input(["HelloWorld\nHeyDevOps"])

    test_game = Game(width = 2, height = 2)
    test_game.board = gameBoard2x2_1
    test_game.turn_num = 5
    test_game.start_new_turn()

    result = get_display_output()

    assert result == [""] + finalLayoutMsg + board2x2Filled_1 + score_computation_2x2_1 + congratsMsg +[""] + error_message


def test_update_high_scores_same_score_lower_position(finalLayoutMsg, gameBoard2x2_1, board2x2Filled_1,score_computation_2x2_1):
    
    position = get_position("high_score_4.json", 7)  
    congratsMsg = ["Congratulations! You made the high score board at position " + str(position) + "!",
                    "Please enter your name (max 20 chars):"]


    high_score_list_2x2_2 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. HelloWorld\\nHeyDevOp     16",
        " 2. HelloWorld\\nHeyDevOp      7",
        " 3. Player 2                  7",
        "-------------------------------"
    ]

    set_keyboard_input(["Player 2"])

    test_game = Game(width = 2, height = 2)
    test_game.board = gameBoard2x2_1
    test_game.turn_num = 5
    test_game.start_new_turn()
    main_menu(True)

    result = get_display_output()

    assert result == [""] + finalLayoutMsg + board2x2Filled_1 + score_computation_2x2_1 + congratsMsg \
                    + [""] + high_score_list_2x2_2 + [""] + mainMenuNoWelcome

    