# Test message
from config import *
from Systems.utils import narrate
from Systems.player import is_player_alive, game_over
from Systems.save_system import load_save_data
from Systems.menu_system import menu_loop

def main_loop():
    narrate("\n  .  .  .  Initiating Program  .  .  .  \n", speed["slow"])

    load_save_data()

    while is_player_alive() == True:
        menu_loop()

    if is_player_alive() == False:
        game_over()
        
main_loop() 
