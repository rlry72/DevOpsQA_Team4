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
import json

gameMenu = ['1. Build a FAC',
            '2. Build a FAC', 
            '3. See remaining buildings',
            '4. See current score',
            '', 
            '5. Save game', 
            '0. Exit to main menu', 
            'Your choice? ']

board = [
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

boardPlaced = [
"     A     B     C     D  ",
"  +-----+-----+-----+-----+",
" 1| FAC |     |     |     |",
"  +-----+-----+-----+-----+",
" 2|     |     |     |     |",
"  +-----+-----+-----+-----+",
" 3|     |     |     |     |",
"  +-----+-----+-----+-----+",
" 4|     |     |     |     |",
"  +-----+-----+-----+-----+",]

board3x3 = [
"     A     B     C  ",
"  +-----+-----+-----+",
" 1|     |     |     |",
"  +-----+-----+-----+",
" 2|     |     |     |",
"  +-----+-----+-----+",
" 3|     |     |     |",
"  +-----+-----+-----+",
]

board3x3Placed = [
"     A     B     C  ",
"  +-----+-----+-----+",
" 1| FAC |     |     |",
"  +-----+-----+-----+",
" 2|     |     |     |",
"  +-----+-----+-----+",
" 3|     |     |     |",
"  +-----+-----+-----+",
]

board5x5 = [
"     A     B     C     D     E  ",
"  +-----+-----+-----+-----+-----+",
" 1|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 2|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 3|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 4|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 5|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",]

board5x5Placed = [
"     A     B     C     D     E  ",
"  +-----+-----+-----+-----+-----+",
" 1| FAC |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 2|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 3|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 4|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",
" 5|     |     |     |     |     |",
"  +-----+-----+-----+-----+-----+",]

@pytest.mark.parametrize("input, citySize, boardState, boardStatePlaced",
[(["1", "a1", "5", "0"], 4, board, boardPlaced), (["1", "a1", "5", "0"], 5, board5x5, board5x5Placed), (["1", "a1", "5", "0"], 3, board3x3, board3x3Placed), 
(["1", "a1", "5", "0"], 4, board, boardPlaced)]) #Existing Save File 
def test_save_game(input, citySize, boardState, boardStatePlaced):
    """
    Test script to save game
    """
    set_keyboard_input(input)

    testGame = Game(width = citySize, height = citySize)
    testGame.randomized_building_history = {"1": ["FAC", "FAC"], "2": ["FAC", "FAC"]}
    testGame.start_new_turn()

    result = get_display_output()

    f = open('game_save.json')
    data = json.load(f)

    assert result == ["", "Turn 1"] + boardState + gameMenu + ["Build where? ", "", "Turn 2"] + boardStatePlaced + gameMenu + ["","Game saved!", "", "Turn 2"] + boardStatePlaced + gameMenu
    assert data["turn_num"] == 2
    assert data["board"] == { "0,0": "FAC"}
    assert data["height"] == citySize
    assert data["width"] == citySize

def test_save_game_empty_board():
    """
    Test script to save game without placing anything on the board.
    """
    set_keyboard_input(["5", "0"])
    testGame = Game()
    testGame.randomized_building_history = {"1": ["FAC", "FAC"], "2": ["FAC", "FAC"]}
    testGame.start_new_turn()
    
    result = get_display_output()

    f = open('game_save.json')
    data = json.load(f)

    assert result == ["", "Turn 1"] + board + gameMenu + ["","Game saved!", "", "Turn 2"] + board + gameMenu
    assert data["turn_num"] == 2
    assert data["board"] == {}
    assert data["height"] == 4
    assert data["width"] == 4

def test_save_game_existing_save():
    """
    Test script to save game without placing anything on the board.
    """
    set_keyboard_input([["1", "a1", "5", "0"]])
    testGame = Game()
    testGame.randomized_building_history = {"1": ["FAC", "FAC"], "2": ["FAC", "FAC"]}
    testGame.start_new_turn()
    
    result = get_display_output()

    f = open('game_save.json')
    tempData = json.load(f)
    tempHeight = tempData["board"]
    f.close()

    set_keyboard_input([["5", "0"]])
    newGame = Game()
    newGame.randomized_building_history = {"1": ["FAC", "FAC"], "2": ["FAC", "FAC"]}
    newGame.start_new_turn()

    newResult = get_display_output()



    fileOpen = open('game_save.json')
    data = json.load(fileOpen)

    assert result == ["", "Turn 1"] + board + gameMenu + ["","Game saved!", "", "Turn 2"] + board + gameMenu
    assert data["turn_num"] == 2
    assert data["board"] == {}
    assert data["board"] != tempHeight
    assert data["height"] == 4
    assert data["width"] == 4