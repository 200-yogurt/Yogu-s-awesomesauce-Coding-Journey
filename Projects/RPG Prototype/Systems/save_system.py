import os
from config import *
from Systems.utils import narrate, intro_cutscene

def save_player_data():
    
    with open(saveFilePath, "w") as file:
        file.write("- - PLAYER DATA - -")
        
        file.write("\n\nPlayer Stats :\n")
        for key, value in playerData["stats"].items():
            file.write(f"   {key} :    {value}\n")

        file.write("\n\nPlayer Inventory :\n")
        for item in playerData["inventory"]:
                file.write(f"   {item}\n")

def load_save_data():

    if os.path.exists(saveFilePath):

        with open(saveFilePath, "r") as file:

            for line in file:

                if line == "Player Stats :":
                    print("Player data stats found")
                    key, value = line.replace(" ", "").strip().split(":")
                    if key in ("HEALTH", "GOLD"):
                        value = int(value)
                    playerData["stats"][key] = value
                    
                if line == "Player Inventory :":
                    print("Player data inventory found")
                    value = line.strip()
                    playerData["inventory"] = value
            
        print("\nSuccesfully Found & Loaded Save File")
        narrate("Loading. . .", speed["slow"])

        intro_cutscene("old")
    else:
        intro_cutscene("new")

        with open (saveFilePath, "x") as file:
            save_player_data()
