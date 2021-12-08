import pytest
from tud_test_base import set_keyboard_input, get_display_output
from classes.menu import *
from classes.game import *


def test_main_menu_exit():
    set_keyboard_input(["0", "0"])
    main_menu()
    with pytest.raises(SystemExit) as e:
        exit_game()
    assert e.type == SystemExit
    assert e.value.code == 1