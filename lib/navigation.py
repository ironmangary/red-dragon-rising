# Navigation functions for Red Dragon Rising

import importlib
from pywebio.output import clear

def go_main_menu():
    clear()
    main_menu_module = importlib.import_module("pages.main_menu")
    main_menu_module.main_menu()

def go_resume_game():
    clear()
    resume_game_module = importlib.import_module("pages.resume_game")
    resume_game_module.resume_game()

def go_exit_game():
    clear()
    exit_game_module = importlib.import_module("pages.main_menu")
    exit_game_module.exit_game()
