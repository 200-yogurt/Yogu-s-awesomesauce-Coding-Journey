import os
from config import *
from Systems.utils import narrate, intro_cutscene

def load_save_data():
    if os.path.exists(saveFilePath):
        with open(saveFilePath, "r") as file:
            for line in file:
                key, value = line.replace(" ", "").strip().split(":")
                if key in ("HEALTH", "GOLD"):
                    value = int(value)
                playerData[key] = value
        print("\nSuccesfully Found & Loaded Save File")
        narrate("Loading. . .", speed["slow"])

        intro_cutscene("old")
    else:
        intro_cutscene("new")

        with open (saveFilePath, "x") as file:
            for key, value in playerData.items():
                file.write(f"{key} :    {value}\n")