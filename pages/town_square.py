# Red Dragon Rising Town Square

from pywebio.output import put_buttons, put_text, put_markdown, put_html, clear
from lib.goto import goto
from lib.character import set_char_stat

def town_square():
    clear()
    set_char_stat("location", "town_square")
    put_html("<script>document.title = 'Red Dragon Rising - Robinson Hills Town Square'</script>")
    put_markdown("""
        # Robinson Hills Town Square")
        
        The cobbled streets hum with the rhythm of daily life. Merchants hawk their wares from stalls draped in rich fabrics, the scent of roasted meats mingling with the crisp bite of morning air. A towering fountain stands at the center—its worn stone whispering tales of ancient rulers and forgotten legends. The laughter of children mixes with the murmurs of traders, and somewhere, a bard plucks a lively tune.
        
        What would you like to do next?
    """)
    put_buttons(["Ye Old Bank", "View Stats", "Quit"],
        onclick=[lambda: goto('bank'), lambda: goto("view_stats"), lambda: goto("main_menu")])
        