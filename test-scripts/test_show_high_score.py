
from unittest import result
import pytest
import os
import sys
import json
from io import StringIO 
from unittest.mock import Mock
from tud_test_base import set_keyboard_input, get_display_output
from classes.game import *
from classes.menu import *
from main import *


mainMenu = ["Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
    "Your choice? "]
mainMenuNoWelcome = ["\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
                     "Your choice? "]


def test_show_high_scores_options_in_main_menu():
    """
    Test whether the "3. Show high scores" option is added to main menu
    """
    set_keyboard_input(["0"])
    
    test_application = main_menu()

    result = get_display_output()
    assert result == mainMenu


def test_show_high_scores_choice_chosen():
    """
    Test whether "Show high scores" option can display the desired output when chosen in main menu
    """
        
    high_score_list_4x4_1 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. Jerry                    48",
        " 2. Mary                     40",
        " 3. Henry                    36",        
        " 4. Johnson                  34",
        "-------------------------------"
    ]
    set_keyboard_input(["3"])

    test_application = main_menu()

    result = get_display_output()
    assert result == mainMenu + [""] + high_score_list_4x4_1 + [""] + mainMenuNoWelcome


def test_show_high_scores_on_two_diff_city_area():
    """
    Test whether the high score lists for different city areas are separated. 
    """
    
    high_score_list_4x4_1 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. Jerry                    48",
        " 2. Mary                     40",
        " 3. Henry                    36",        
        " 4. Johnson                  34",
        "-------------------------------"
    ]


    high_score_list_3x3_1 = [
        "--------- HIGH SCORES ---------",
        "Pos Player                Score",
        "--- ------                -----",
        " 1. Shi Qing                 20",
        " 2. Zaidan                   17",
        " 3. Ken Liu                  17",        
        " 4. Ting Ru                  15",
        " 5. Ya Ru                    15",
        "-------------------------------"
    ]

    
    choose_city_size_msg = [
        "Choose your city size below. Please take note that the multiplication of width and height cannot be more than 40.",
        "Enter 0 to exit this configuration."
    ]

    prompt_width = ["Enter value for width: "]
    prompt_height = ["Enter value for height: "]

   
    current_city_size_4x4 = [
        "--------- CURRENT CITY SIZE ---------",
        "Width: 4",
        "Height: 4",
        "-------------------------------------"
    ] 
    
    chosen_city_size_3x3 = [
        "--------- CHOSEN CITY SIZE ---------",
        "Width: 3",
        "Height: 3",
        "------------------------------------"
    ]
    set_keyboard_input(["3", "5", "3", "3", "3"])
    test_application = main_menu()

    result = get_display_output()
    assert result == mainMenu + [""] + high_score_list_4x4_1 + [""] + mainMenuNoWelcome + [""] + current_city_size_4x4 + ["0"] + choose_city_size_msg + [""] \
        + prompt_width + prompt_height + [""] + chosen_city_size_3x3 + [""] + mainMenuNoWelcome + [""] + high_score_list_3x3_1 + [""] + mainMenuNoWelcome


