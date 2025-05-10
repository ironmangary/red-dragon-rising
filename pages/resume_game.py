# Resume Game for Red Dragon Rising

from lib.character import get_char_stat
from lib.goto import goto
from pywebio.output import put_buttons, put_text, clear

def resume_game():
    if get_char_stat("awake") == "dead":
        put_text("You are alive again.")
        put_buttons(["Continue"], onclick=[lambda: goto("main_menu")])
    elif get_char_stat("status") == "asleep_inn":
        put_text("You are sleeping at the Knight Fall Inn.")
        put_buttons(["Continue"], onclick=[lambda: goto("main_menu")])
    else: 
        goto("town_square")
    