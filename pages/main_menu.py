# Red Dragon Rising Main Menu

from pywebio.output import put_buttons, put_text, put_markdown, put_html, clear
from pages.resume_game import resume_game
from pages.new_game import new_game

def main_menu():
    clear()
    put_html("<script>document.title = 'Red Dragon Rising - Main Menu'</script>")
    put_markdown("# Red Dragon Rising")
    put_buttons(["Start New Game", "Resume Game", "Exit"], 
                onclick=[new_game, resume_game, exit_game])

def exit_game():
    clear()
    put_text("Returning to the mundane world.")
