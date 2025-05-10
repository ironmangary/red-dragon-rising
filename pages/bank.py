# Red Dragon Rising Ye Old Bank

from pywebio.output import put_buttons, put_text, put_markdown, put_html, clear
from pywebio.input import input, NUMBER
from lib.goto import goto, go_back
from lib.character import set_char_stat, get_char_stat

def bank():
    clear()
    set_char_stat("location", "bank")
    put_html("<script>document.title = 'Red Dragon Rising - Ye Old Bank'</script>")
    put_markdown("""
    # Ye Old Bank
    
    A sturdy stone building sits just off the Town Square, its heavy doors leading into a quiet space where fortunes are kept safe—if only temporarily.
    Inside, clerks scribble figures into ledgers, recording deposits, withdrawals, and the occasional plea for a loan. Stacks of coin rest behind iron bars, guarded not just by locks but by the ever-watchful eyes of the Bank’s staff.

    Whether you’re securing your savings for the future or drawing funds for your next adventure, the Bank stands ready.

    """)
    put_markdown(f"""
    You currently have {get_char_stat("gold_hand")} gold and {get_char_stat("gems_hand")} gems on hand.  The teller informs you that you have a balance of {get_char_stat("gold_bank")} gold and {get_char_stat("gems_bank")} gems in the bank.
    
    What would you like to do next?
    
    ### Gold
    """)
    put_buttons(["Deposit", "Deposit All", "Withdrawl", "Withdrawl All"],
        onclick=[deposit_gold, lambda: deposit_all('gold'), withdraw_gold, lambda: withdraw_all('gold')])
    put_markdown("### Gems")
    if get_char_stat("gem_vault") == 1:
        put_buttons(["Deposit", "Deposit All", "Withdrawl", "Withdrawl All"],
            onclick=[deposit_gems, lambda: deposit_all('gems'), withdraw_gems, lambda: withdraw_all('gems')])
    else:
        put_buttons(["Open a Gem Vault"], onclick=[open_gem_vault])
    put_markdown("### Other")
    put_buttons(["View Stats", "Leave Bank", "Quit"],
        onclick=[lambda: goto('view_stats'), lambda: goto('town_square'), lambda: goto('main_menu')])

def deposit_gold():
    deposit_amount = input("How much gold do you want to deposit?", type=NUMBER)
    put_buttons(["Confirm", "Cancel"], onclick=[lambda: finalize_deposit("gold", deposit_amount), bank])

def withdraw_gold():
    withdraw_amount = input("How much gold do you want to withdraw?", type=NUMBER)
    put_buttons(["Confirm", "Cancel"], onclick=[lambda: finalize_withdraw("gold", withdraw_amount), bank])

def deposit_gems():
    deposit_amount = input("How many gems do you want to deposit?", type=NUMBER)
    put_buttons(["Confirm", "Cancel"], onclick=[lambda: finalize_deposit("gems", deposit_amount), bank])

def withdraw_gems():
    withdraw_amount = input("How many gems do you want to withdraw?", type=NUMBER)
    put_buttons(["Confirm", "Cancel"], onclick=[lambda: finalize_withdraw("gems", withdraw_amount), bank])

def finalize_deposit(currency, amount):
    hand_balance = get_char_stat(f"{currency}_hand")
    bank_balance = get_char_stat(f"{currency}_bank")

    if amount > hand_balance:
        put_text(f"You don't have enough {currency} to deposit.")
        go_back()
        return

    set_char_stat(f"{currency}_hand", hand_balance - amount)  # Remove from hand
    set_char_stat(f"{currency}_bank", bank_balance + amount)  # Add to bank
    put_text(f"{amount} {currency.capitalize()} deposited successfully.")
    go_back()
    return

def deposit_all(currency):
    hand_balance = get_char_stat(f"{currency}_hand")
    
    if hand_balance == 0:
        put_text(f"You have no {currency} to deposit.")
        go_back()
        return
    
    set_char_stat(f"{currency}_hand", 0)  # Empty hand balance
    set_char_stat(f"{currency}_bank", get_char_stat(f"{currency}_bank") + hand_balance)  # Transfer to bank
    
    put_text(f"All {currency.capitalize()} deposited successfully.")
    go_back()
    return

def finalize_withdraw(currency, amount):
    bank_balance = get_char_stat(f"{currency}_bank")
    hand_balance = get_char_stat(f"{currency}_hand")

    if amount > bank_balance:
        put_text(f"You don't have enough {currency} in the bank.")
        go_back()
        return

    set_char_stat(f"{currency}_bank", bank_balance - amount)  # Remove from bank
    set_char_stat(f"{currency}_hand", hand_balance + amount)  # Add to hand
    put_text(f"{amount} {currency.capitalize()} withdrawn successfully.")
    go_back()
    return

def withdraw_all(currency):
    bank_balance = get_char_stat(f"{currency}_bank")
    
    if bank_balance == 0:
        put_text(f"You have no {currency} in the bank to withdraw.")
        return
    
    set_char_stat(f"{currency}_bank", 0)  # Empty bank balance
    set_char_stat(f"{currency}_hand", get_char_stat(f"{currency}_hand") + bank_balance)  # Transfer to hand
    
    put_text(f"All {currency.capitalize()} withdrawn successfully.")
    return

def open_gem_vault():
    set_char_stat("gem_vault", 1)
    return "You’ve successfully opened a Gem Vault! You can now store gems in the bank."
