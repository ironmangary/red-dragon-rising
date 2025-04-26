# New Game - Character Creation

from pywebio.output import put_buttons, put_text, put_markdown, put_html, clear, toast
from pywebio.input import input, radio, select, actions
from lib.character import set_char_stat
import os
from lib.navigation import go_main_menu, go_resume_game

def create_character(name, gender, specialty):
    set_char_stat("name", name)
    set_char_stat("gender", gender)
    set_char_stat("specialty", specialty)
    set_char_stat("xp", 1)
    set_char_stat("level", 1)
    set_char_stat("rank", "Apprentice")
    set_char_stat("max_hp", 25)
    set_char_stat("hp", 25)
    set_char_stat("offense", 10)
    set_char_stat("defense", 10)
    set_char_stat("stamina", 0)
    set_char_stat("charm", 0)
    set_char_stat("gold_hand", 50)
    set_char_stat("gold_bank", 0)
    set_char_stat("weapon", 101)  # Default weapon (Fists)
    set_char_stat("armor", 201)   # Default armor (T-Shirt)
    set_char_stat("horse", 0)   # No horse by default
    set_char_stat("healing_potions", 1)
    set_char_stat("days", 0)
    set_char_stat("kills", 0)
    
    # Successful character creation
    toast(f"Character Created! Welcome, {name}.", duration=3, color="green")

    put_markdown(f"### Welcome, {name}!")
    put_text("Now what do you want to do?")

    put_buttons(["Start Playing", "Return to Main Menu"], 
        onclick=[go_resume_game, go_main_menu])

def new_game():
    # Check if character.json exists
    if os.path.exists(os.path.join("assets", "character.json")):
        result = actions("Warning: Starting a new game will erase existing character data!",
                         ["Continue Anyway", "Cancel"])
        if result == "Cancel":
            return
            
    clear()
    put_html("<script>document.title = 'Red Dragon Rising - Main Menu'</script>")
    put_markdown("""
    ## Welcome to the Realm

    You wander into a foreign land with 50 gold to your name, looking for fame, glory, and riches.  Oh, a hot meal and companionship would be nice, too!

    ## About You
    """)

    name = input("How will you be known to this world?")
    if not name:
        toast("Warning: You must enter a name!", duration=3, color="red")  # Shows a warning popup
    gender = radio("Choose your gender:", options=["Male", "Female"])
    put_markdown("""
    Next, we need to know which specialty you wish to pursue.  Your options are:

        - ** Warrior** - Warriors are tough, disciplined combatants who excel in direct confrontation and battlefield endurance.
        - **Assassin** - Assassins are stealthy killers who strike from the shadows with lethal precision.
        - **Thief** - Agile and cunning, thieves specialize in misdirection, speed, and opportunistic strikes.
    """)

    specialty = select("Choose your specialty:", ["Warrior", "Assassin", "Thief"])
    
    put_buttons(["Create Character"], onclick=[lambda: create_character(name, gender, specialty)])

        