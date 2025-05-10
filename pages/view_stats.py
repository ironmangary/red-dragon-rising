# Red Dragon Rising - View Stats

from pywebio.output import put_text, put_markdown, put_html, clear, put_collapse
from lib.character import get_char_stat
from lib.goto import goto, go_back

def view_stats():
    clear()
    put_html("<script>document.title = 'Red Dragon Rising - View Stats'</script>")
    put_markdown("## View Your Stats")
    
    put_collapse("Character Stats", [
        put_markdown(f"""
        ## Current Stats
        * **Name:** {get_char_stat('name')}
        * **Experience:** {get_char_stat('xp')}
        * **Level:** {get_char_stat('level')}
        * **Rank:** {get_char_stat('rank')}
        * **Health:** {get_char_stat('hp')}/{get_char_stat('max_hp')}
        * **Stamina:** {get_char_stat('stamina')}
        * **Offense:** {get_char_stat('offense')}
        * **Defense:** {get_char_stat('defense')}
        * **Gender:** {get_char_stat('gender')}
        * **Charm:** {get_char_stat('charm')}
        """)
    ])
    
    put_collapse("Inventory", [
        put_markdown(f"""
        - **Gold On Hand:** {get_char_stat('gold_hand')}
        - **Gold In Bank:** {get_char_stat('gold_bank')}
        - **Gems On Hand:** {get_char_stat('gems_hand')}
        - **Gems In Bank:** {get_char_stat('gems_bank')}
        - **Weapon:** None
        - **Armor:** None
        - **Horse:** None
        - **Healing Potions:** {get_char_stat('healing_potions')}
        """)
    ])
    
    go_back()
    