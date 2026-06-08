from config import *
from Systems.utils import narrate
from Systems.player import player_status, game_over
from Systems.save_system import load_save_data
from Systems.menu_system import menu_loop

def main_loop():
    narrate("\n  .  .  .  Initiating Program  .  .  .  \n", speed["slow"])

    load_save_data()

    if player_status() == True:
        while player_status():
            menu_loop()
    else:
        game_over()
        
main_loop() 
