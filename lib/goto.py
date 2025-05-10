# goto() Navigation  function and dictionary for Red Dragon Rising

from pywebio.output import put_buttons
from lib.character import get_char_stat

def goto(location):
    """Handles navigation using the centralized dictionary."""
    import importlib
    
    NAVIGATION_MAP = {
        "main_menu": importlib.import_module("pages.main_menu").main_menu,
        "exit_game": importlib.import_module("pages.main_menu").exit_game,
        "new_game": importlib.import_module("pages.new_game").new_game,
        "resume_game": importlib.import_module("pages.resume_game").resume_game,
        "town_square": importlib.import_module("pages.town_square").town_square,
        "bank": importlib.import_module("pages.bank").bank,
        "view_stats": importlib.import_module("pages.view_stats").view_stats,
    }

    return_function = NAVIGATION_MAP.get(location, goto_main_menu)  
    
    return_function() 

def goto_main_menu():
    """Handles returning the player to the main menu."""
    from pages.main_menu import main_menu  
    main_menu()

def go_back():
    """Creates a 'Go Back' button that returns the player to their last location."""
    back_to = get_char_stat("location") 
    put_buttons(["Go Back"], onclick=[lambda: goto(back_to)]) 
    