# Red Dragon Rising
# Version 1.0 Alpha 2 (04/25/2025)
# By Gary Hartzell

from pages.main_menu import main_menu
from pywebio.session import run_async
from pywebio import start_server

if __name__ == "__main__":
    start_server(main_menu, port=8082, auto_open_webbrowser=True)
