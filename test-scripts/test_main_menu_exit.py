import pytest
from main import *
from tud_test_base import set_keyboard_input, get_display_output
from classes.menu import *
from classes.game import *


def test_main_menu_exit():
    """
    Tests the exit function of main menu. This checks if game exits out of console or out of the game completely if opened from console properly.
    """
    # set keyboard input to 0 (ignores first 0)
    set_keyboard_input(["0", "0"])
    # starts main menu
    # use pytest to raise a systemexit exception, then calls exit game function
    with pytest.raises(SystemExit) as e:
        main()
    # checks if exception type and value code are that of exit code. if different, test fails
    assert e.type == SystemExit
    assert e.value.code == 1