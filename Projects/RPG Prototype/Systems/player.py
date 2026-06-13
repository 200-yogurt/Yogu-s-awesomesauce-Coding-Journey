import os
from config import *
from Systems.utils import narrate

def is_player_alive():
    if playerData["stats"]["HEALTH"] > 0:
        isAlive = True
    else:
        isAlive = False

    return isAlive
def game_over():
    narrate(".....", speed["fast"])
    narrate("- IT SEEMS LIKE WE LOST YOU... \n", speed["moderate"])
    print(f"- {playerData["stats"]["NAME"]}! IT WAS NICE TO MEET YOU!")
    narrate(".....", speed["moderate"])

    narrate("\n\n  .  .  .  Game Over  .  .  . \n\n", speed["slow"])

    choice = input("Would you like to start over?  (y/n)\n")
    narrate("Loading. . .", speed["slow"])
    if "y" in choice:
        if os.path.exists(saveFilePath):
            os.remove(saveFilePath)
        print("\nCome back soon. . .\n")
    elif "n" in choice:
        narrate(". . .", speed["moderate"])
        print("But aren't you dead?")
    narrate("", speed["slow"])
