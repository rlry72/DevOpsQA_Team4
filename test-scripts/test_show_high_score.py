
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
import main
import classes


pytestmark = pytest.mark.skipif("display_high_score" not in dir(classes.game.Game), reason="display high score not implemented")

mainMenu = ["Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
    "Your choice? "]
mainMenuNoWelcome = ["\n1. Start new game\n2. Load saved game\n3. Show high scores\n4. Choose building pool\n5. Choose city size\n\n0. Exit",
                     "Your choice? "]

high_score_list_empty = [
    "--------- HIGH SCORES ---------",
    "Pos Player                Score",
    "--- ------                -----",       
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


def test_show_high_scores_options_in_main_menu():
    """
    Test whether the "3. Show high scores" option is added to main menu
    """

    # main.main() function is a while true loop. 
    # Thus, test script needs to use "0" input value in main menu to close the while loop after checking the output.
    # Or else, test script will return index error.
    set_keyboard_input(["0"])
    
    # When using "0" to close the while loop, Dev Code will use exit() to exit the application, which will cause SystemExit error to the test script.
    # To solve this issue, pytest.raises(SystemExit) is used to check the SystemExit error in Test script that returns by the exit() used in the Dev Code.
    with pytest.raises(SystemExit) as e:
        test_application = main.main()  

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

    high_score_json_16 = {   
        "board_size": 3,
        "high_scores" : [
            {
                "name": "Jerry",
                "score": 48
            },
            {
                "name": "Mary",
                "score": 40
            },
            {
                "name": "Henry",
                "score": 36
            },
            {
                "name": "Johnson",
                "score": 34
            }
        ]
    }   

    high_score_Exist = os.path.exists('high_score_16.json')
    if high_score_Exist:
        os.remove('high_score_16.json')

    jsonString = json.dumps(high_score_json_16)
    jsonFile = open("high_score_16.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()



    # main.main() function is a while true loop. 
    # Thus, test script needs to use "0" input value in main menu to close the while loop after checking the output.
    # Or else, test script will return index error.
    set_keyboard_input(["3","0"])

    # When using "0" to close the while loop, Dev Code will use exit() to exit the application, which will cause SystemExit error to the test script.
    # To solve this issue, pytest.raises(SystemExit) is used to check the SystemExit error in Test script that returns by the exit() used in the Dev Code.
    with pytest.raises(SystemExit) as e:         
        test_application = main.main()  
           

    result = get_display_output()
    assert result == mainMenu + [""] + high_score_list_4x4_1 + mainMenuNoWelcome
     
    
   


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
    
       
    chosen_city_size_3x3 = [
        "--------- CHOSEN CITY SIZE ---------",
        "Width: 3",
        "Height: 3",
        "------------------------------------"
    ]

    
    high_score_json_16 = {   
        "board_size": 16,
        "high_scores" : [
            {
                "name": "Jerry",
                "score": 48
            },
            {
                "name": "Mary",
                "score": 40
            },
            {
                "name": "Henry",
                "score": 36
            },
            {
                "name": "Johnson",
                "score": 34
            }
        ]
    }   


    
    high_score_json_9 = {   
        "board_size": 9,
        "high_scores" : [
            {
                "name": "Shi Qing",
                "score": 20
            },
            {
                "name": "Zaidan",
                "score": 17
            },
            {
                "name": "Ken Liu",
                "score": 17
            },
            {
                "name": "Ting Ru",
                "score": 15
            },
            {
                "name": "Ya Ru",
                "score": 15
            }
        ]
    }   

    high_score_Exist = os.path.exists('high_score_16.json')
    if high_score_Exist:
        os.remove('high_score_16.json')

    jsonString = json.dumps(high_score_json_16)
    jsonFile = open("high_score_16.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

    high_score_Exist = os.path.exists('high_score_9.json')
    if high_score_Exist:
        os.remove('high_score_9.json')

    jsonString = json.dumps(high_score_json_9)
    jsonFile = open("high_score_9.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()


    # main.main() function is a while true loop. 
    # Thus, test script needs to use "0" input value in main menu to close the while loop after checking the output.
    # Or else, test script will return index error.
    set_keyboard_input(["3", "5", "3", "3", "3","0"])

    # When using "0" to close the while loop, Dev Code will use exit() to exit the application, which will cause SystemExit error to the test script.
    # To solve this issue, pytest.raises(SystemExit) is used to check the SystemExit error in Test script that returns by the exit() used in the Dev Code.
    with pytest.raises(SystemExit) as e:         
        test_application = main.main()  
           

    result = get_display_output()
    assert result == mainMenu + [""] + high_score_list_4x4_1 +  mainMenuNoWelcome + [""] + current_city_size_4x4 + [""] + choose_city_size_msg + [""] \
        + prompt_width + prompt_height + [""] + chosen_city_size_3x3 + mainMenuNoWelcome + [""] + high_score_list_3x3_1 +  mainMenuNoWelcome



def test_show_high_scores_empty_list():
    """
    Test whether the system will display high score list's header and footer with empty content 
    when the high score list is empty
    """


    
    chosen_city_size_6x1 = [
        "--------- CHOSEN CITY SIZE ---------",
        "Width: 6",
        "Height: 1",
        "------------------------------------"
    ]
    high_score_Exist = os.path.exists('high_score_6.json')
    if high_score_Exist:
        os.remove('high_score_6.json')

    # main.main() function is a while true loop. 
    # Thus, test script needs to use "0" input value in main menu to close the while loop after checking the output.
    # Or else, test script will return index error.
    set_keyboard_input(["5", "6", "1", "3","0"])

    # When using "0" to close the while loop, Dev Code will use exit() to exit the application, which will cause SystemExit error to the test script.
    # To solve this issue, pytest.raises(SystemExit) is used to check the SystemExit error in Test script that returns by the exit() used in the Dev Code.
    with pytest.raises(SystemExit) as e:         
        test_application = main.main()  
           

    result = get_display_output()
    assert result == mainMenu + [""] + current_city_size_4x4 + [""] + choose_city_size_msg + [""] \
                    + prompt_width + prompt_height + [""] + chosen_city_size_6x1 +  mainMenuNoWelcome \
                    + [""] + high_score_list_empty +  mainMenuNoWelcome


def test_show_high_score_file_corrupted():
    """
    Test whether the system will display error msg and continue working when reading the corrupted saved file.
    """ 
        
    chosen_city_size_7x1 = [
        "--------- CHOSEN CITY SIZE ---------",
        "Width: 7",
        "Height: 1",
        "------------------------------------"
    ]
    high_score_json_7 = {   
        "board_size": 1,
        "high" : [
            {
                "name": "HelloWorldHeyDevOps",
                "score": 16
            }
        ],
        "hell": 'well'        
    }   

    errorMsg = ["The current file is corrupt and will therefore be deleted."]
 

    high_score_Exist = os.path.exists('high_score_7.json')
    if high_score_Exist:
        os.remove('high_score_7.json')

    jsonString = json.dumps(high_score_json_7)
    jsonFile = open("high_score_7.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()


    set_keyboard_input(["5","1","1","3","0"])
    with pytest.raises(SystemExit) as e:        
        test_application = main.main()  
       
       
    result = get_display_output()
    assert result == mainMenu + [""] + current_city_size_4x4 + [""] + choose_city_size_msg + [""] \
                    + prompt_width + prompt_height + [""] + chosen_city_size_7x1 +  mainMenuNoWelcome \
                    + [""] + errorMsg + [""] + high_score_list_empty +  mainMenuNoWelcome