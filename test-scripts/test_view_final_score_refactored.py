from classes.game import *
from classes.menu import *
from tud_test_base import set_keyboard_input, get_display_output
from io import StringIO 
from unittest.mock import Mock, patch
from unittest import mock
import sys
import pytest
import os
import random
import math
import statistics
import classes

pytestmark = pytest.mark.skipif("generate_remaining_building_string" not in dir(classes.game.Game), reason="view remaining buildings on side not implemented")

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
board1x1 = [
"     A           Building   Remaining",
"  +-----+        --------------------",
" 1|     |        HSE      | 0",
"  +-----+        FAC      | 36",
"                 SHP      | 0",
"                 HWY      | 2",
"                 BCH      | 0",
]

board1x1Filled = [
"     A  ",
"  +-----+",
" 1| FAC |",
"  +-----+",]

board2x2 = [
"     A     B           Building   Remaining",
"  +-----+-----+        --------------------",
" 1|     | FAC |        HSE      | 0",
"  +-----+-----+        FAC      | 36",
" 2| FAC | FAC |        SHP      | 0",
"  +-----+-----+        HWY      | 2"
"                       BCH      | 0",
]

board2x2Filled = [
"     A     B  ",
"  +-----+-----+",
" 1| FAC | FAC |",
"  +-----+-----+",
" 2| FAC | FAC |",
"  +-----+-----+",]

board3x3 = [
"     A     B     C           Building   Remaining",
"  +-----+-----+-----+        --------------------",
" 1|     | FAC | FAC |        HSE      | 0",
"  +-----+-----+-----+        FAC      | 36",
" 2| FAC | FAC | FAC |        SHP      | 0",
"  +-----+-----+-----+        HWY      | 2",
" 3| FAC | FAC | FAC |        BCH      | 0",
"  +-----+-----+-----+",
]

board3x3Filled = [
"     A     B     C  ",
"  +-----+-----+-----+",
" 1| FAC | FAC | FAC |",
"  +-----+-----+-----+",
" 2| FAC | FAC | FAC |",
"  +-----+-----+-----+",
" 3| FAC | FAC | FAC |",
"  +-----+-----+-----+",
]

board4x4 = [
"     A     B     C     D           Building   Remaining",
"  +-----+-----+-----+-----+        --------------------",
" 1|     | FAC | FAC | FAC |        HSE      | 0",
"  +-----+-----+-----+-----+        FAC      | 36",
" 2| FAC | FAC | FAC | FAC |        SHP      | 0",
"  +-----+-----+-----+-----+        HWY      | 2",
" 3| FAC | FAC | FAC | FAC |        BCH      | 0",
"  +-----+-----+-----+-----+",
" 4| FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+",]

board4x4Filled = [
"     A     B     C     D  ",
"  +-----+-----+-----+-----+",
" 1| FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+",
" 2| FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+",
" 3| FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+",
" 4| FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+",]

board5x5 = [
"     A     B     C     D     E           Building   Remaining",
"  +-----+-----+-----+-----+-----+        --------------------",
" 1|     | FAC | FAC | FAC | FAC |        HSE      | 0",
"  +-----+-----+-----+-----+-----+        FAC      | 36",
" 2| FAC | FAC | FAC | FAC | FAC |        SHP      | 0",
"  +-----+-----+-----+-----+-----+        HWY      | 2",
" 3| FAC | FAC | FAC | FAC | FAC |        BCH      | 0",
"  +-----+-----+-----+-----+-----+",
" 4| FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+",
" 5| FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+",]

board5x5Filled = [
"     A     B     C     D     E  ",
"  +-----+-----+-----+-----+-----+",
" 1| FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+",
" 2| FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+",
" 3| FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+",
" 4| FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+",
" 5| FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+",]

board6x6 = [
"     A     B     C     D     E     F           Building   Remaining",
"  +-----+-----+-----+-----+-----+-----+        --------------------",
" 1|     | FAC | FAC | FAC | FAC | FAC |        HSE      | 0",
"  +-----+-----+-----+-----+-----+-----+        FAC      | 36",
" 2| FAC | FAC | FAC | FAC | FAC | FAC |        SHP      | 0",
"  +-----+-----+-----+-----+-----+-----+        HWY      | 2",
" 3| FAC | FAC | FAC | FAC | FAC | FAC |        BCH      | 0",
"  +-----+-----+-----+-----+-----+-----+",
" 4| FAC | FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+-----+",
" 5| FAC | FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+-----+",
" 6| FAC | FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+-----+",]

board6x6Filled = [
"     A     B     C     D     E     F  ",
"  +-----+-----+-----+-----+-----+-----+",
" 1| FAC | FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+-----+",
" 2| FAC | FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+-----+",
" 3| FAC | FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+-----+",
" 4| FAC | FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+-----+",
" 5| FAC | FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+-----+",
" 6| FAC | FAC | FAC | FAC | FAC | FAC |",
"  +-----+-----+-----+-----+-----+-----+",]

caseStudyBoardState = [
"     A     B     C     D           Building   Remaining",
"  +-----+-----+-----+-----+        --------------------",
" 1| SHP | SHP | HSE |     |        HSE      | 0",
"  +-----+-----+-----+-----+        FAC      | 36",
" 2| BCH | HSE | HSE | BCH |        SHP      | 0",
"  +-----+-----+-----+-----+        HWY      | 2",
" 3| BCH | SHP | HSE | HSE |        BCH      | 0",
"  +-----+-----+-----+-----+",
" 4| HWY | HWY | HWY | HWY |",
"  +-----+-----+-----+-----+",]

caseStudyBoardStateFilled = [
"     A     B     C     D  ",
"  +-----+-----+-----+-----+",
" 1| SHP | SHP | HSE | FAC |",
"  +-----+-----+-----+-----+",
" 2| BCH | HSE | HSE | BCH |",
"  +-----+-----+-----+-----+",
" 3| BCH | SHP | HSE | HSE |",
"  +-----+-----+-----+-----+",
" 4| HWY | HWY | HWY | HWY |",
"  +-----+-----+-----+-----+",]
    
score1x1 = [
"HSE: 0",
"FAC: 1 = 1",
"SHP: 0",
"HWY: 0",
"BCH: 0",
"Total score: 1"]

score2x2 = [
"HSE: 0",
"FAC: 4 + 4 + 4 + 4 = 16",
"SHP: 0",
"HWY: 0",
"BCH: 0",
"Total score: 16"]

score3x3 = [
"HSE: 0",
"FAC: 4 + 4 + 4 + 4 + 1 + 1 + 1 + 1 + 1 = 21",
"SHP: 0",
"HWY: 0",
"BCH: 0",
"Total score: 21"]

score4x4 = [
"HSE: 0",
"FAC: 4 + 4 + 4 + 4 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 28",
"SHP: 0",
"HWY: 0",
"BCH: 0",
"Total score: 28"]

score5x5 = [
"HSE: 0",
"FAC: 4 + 4 + 4 + 4 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 37",
"SHP: 0",
"HWY: 0",
"BCH: 0",
"Total score: 37"]

score6x6 = [
"HSE: 0",
"FAC: 4 + 4 + 4 + 4 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 48",
"SHP: 0",
"HWY: 0",
"BCH: 0",
"Total score: 48"]

scoreCaseStudy = [
"HSE: 1 + 5 + 5 + 3 + 3 = 17",
"FAC: 1 = 1",
"SHP: 2 + 2 + 3 = 7",
"HWY: 4 + 4 + 4 + 4 = 16",
"BCH: 3 + 3 + 3 = 9",
"Total score: 50"]

actualBoard4x4 = [
[Building(), Factory(1, 0), Factory(2, 0), Factory(3, 0)],
[Factory(0, 1), Factory(1, 1), Factory(2, 1), Factory(3, 1)],
[Factory(0, 2), Factory(1, 2), Factory(2, 2), Factory(3, 2)],
[Factory(0, 3), Factory(1, 3), Factory(2, 3), Factory(3, 3)]]

actualBoard1x1 = [
[Building()]
]

actualBoard2x2 = [
[Building(), Factory(1,0)],
[Factory(0,1), Factory(1,1)],
]

actualBoard3x3 = [
[Building(), Factory(1,0), Factory(2,0)],
[Factory(0,1), Factory(1,1), Factory(2,1)],
[Factory(0,2), Factory(1,2), Factory(2,2)]
]

actualBoard5x5 = [
[Building(), Factory(1, 0), Factory(2, 0), Factory(3, 0), Factory(4,0)],
[Factory(0, 1), Factory(1, 1), Factory(2, 1), Factory(3, 1), Factory(4, 1)],
[Factory(0, 2), Factory(1, 2), Factory(2, 2), Factory(3, 2), Factory(4, 2)],
[Factory(0, 3), Factory(1, 3), Factory(2, 3), Factory(3, 3), Factory(4, 3)],
[Factory(0, 4), Factory(1, 4), Factory(2, 4), Factory(3, 4), Factory(4, 4)],]

actualBoard6x6 = [
[Building(), Factory(1, 0), Factory(2, 0), Factory(3, 0), Factory(4,0), Factory(5, 0)],
[Factory(0, 1), Factory(1, 1), Factory(2, 1), Factory(3, 1), Factory(4, 1), Factory(5, 1)],
[Factory(0, 2), Factory(1, 2), Factory(2, 2), Factory(3, 2), Factory(4, 2), Factory(5, 2)],
[Factory(0, 3), Factory(1, 3), Factory(2, 3), Factory(3, 3), Factory(4, 3), Factory(5, 3)],
[Factory(0, 4), Factory(1, 4), Factory(2, 4), Factory(3, 4), Factory(4, 4), Factory(5, 4)],
[Factory(0, 5), Factory(1, 5), Factory(2, 5), Factory(3, 5), Factory(4, 5), Factory(5, 5)],]

actualBoardCaseStudy = [
[Shop(0,0), Shop(1, 0), House(2, 0), Building()],
[Beach(0, 1), House(1, 1), House(2, 1), Beach(3, 1)],
[Beach(0, 2), Shop(1, 2), House(2, 2), House(3, 2)],
[Highway(0, 3), Highway(1, 3), Highway(2, 3), Highway(3, 3)]]


@pytest.mark.parametrize("input, boardState, turnNumber, scoreBoard, heightWidth, actualBoard, boardStateFilled",
[(["1", "a1", "0"], board1x1, 1, score1x1, [1,1], actualBoard1x1, board1x1Filled), (["1", "a1", "0"], board2x2, 4, score2x2, [2,2], actualBoard2x2, board2x2Filled),
(["1", "a1", "0"], board3x3, 9, score3x3, [3,3], actualBoard3x3, board3x3Filled),
(["1", "a1", "0"], board4x4, 16, score4x4, [4,4], actualBoard4x4, board4x4Filled),
(["1", "a1", "0"], board5x5, 25, score5x5, [5,5], actualBoard5x5, board5x5Filled), (["1", "a1", "0"], board6x6, 36, score6x6, [6,6], actualBoard6x6, board6x6Filled),
(["1", "d1", "0"], caseStudyBoardState, 16, scoreCaseStudy, [4,4], actualBoardCaseStudy, caseStudyBoardStateFilled),])
def test_view_final_score(input, boardState, turnNumber, scoreBoard, heightWidth, actualBoard, boardStateFilled):
    """
    Test script to check viewing final score computation, final total score and whether main menu is displayed after final turn.
    """
    turnNumberArray = ["Turn " + str(turnNumber)]

    set_keyboard_input(input)

    test_game = Game(width = heightWidth[0], height = heightWidth[1])
    test_game.turn_num = turnNumber
    test_game.board = actualBoard
    test_game.randomized_building_history = {"1": ["FAC", "FAC"], "4": ["FAC", "FAC"], "9": ["FAC", "FAC"], "16": ["FAC", "FAC"], "25": ["FAC", "FAC"], "36": ["FAC", "FAC"]}
    test_game.building_pool = {"HSE": 0, "FAC": 36, "SHP": 0, "HWY": 2, "BCH": 0}
    test_game.start_new_turn()
    main_menu(True)

    result = get_display_output()

    expectedOutputArray = [""] + turnNumberArray + boardState + gameMenu + ["Build where? ", "", "Final layout of Simp City:"] + boardStateFilled + scoreBoard+  mainMenuNoWelcome
    check =  all(item in result for item in expectedOutputArray)

    assert check == True