from config import *
from Systems.utils import narrate
from Systems.explore_system import explore

def display_stats():
    narrate("- HAVE A PEEK AT YOUR STATS . . .\n", speed["fast"])

    for key, value in playerData.items():
        print(f"{key} : {value}")
def rest():
    restGoldCost = 10
    restHealAmount = 25 # Adding unique variables for the Rest feature since I plan to expand further upon this in the future

    if playerData["GOLD"] >= restGoldCost:
        playerData["HEALTH"] += restHealAmount 
        playerData["GOLD"] = playerData["GOLD"] - restGoldCost 

        print("\nSuccesfully Rested")
    else:
        print("- YOU DON'T SEEM TO HAVE ENOUGH RESOURCES, ADVENTURER...")
def save_progress():
    choice = input(f"- ARE YOU SURE YOU WANT TO REWRITE YOUR SAVE, ADVENTURER?  (y/n)\n").strip().lower()
    narrate("Loading. . .", speed["slow"])

    if "y" in choice:
        with open(saveFilePath, "w") as file:
            for key, value in playerData.items():
                file.write(f"{key} :    {value}\n")

        print("Saved Succesfully")
    elif "n" in choice:
        print("Aborted Save File Rewritting")
    else:
        print("Invalid Option")
def quit():
    saveChoice = True
    while saveChoice:
        choice = input("Save Before Quitting?   (y/n)\n").strip().lower()
        narrate("Loading. . .", speed["slow"])

        if "y" in choice:
            with open(saveFilePath, "w") as file:
                for key, value in playerData.items():
                    file.write(f"{key} :    {value}\n")

            saveChoice = False
            print("Saved Succesfully")
        elif "n" in choice:
            saveChoice = False
        else:
            print("Invalid Option, try again")
        
        narrate("Loading. . .", speed["slow"])

    narrate("- UNTIL NEXT TIME, ADVENTURER", speed["slow"])
    narrate("\n\n  .  .  .  Terminating Program  .  .  . \n\n", speed["slow"])

    exit()


def menu_loop():
    print(f"""
- WELCOME TO THE MENU, {playerData["NAME"]}

    1- View Stats
    2- Rest (costs 10$)
    3- Explore
    4- Save
    5- Quit

- WHAT DO YOU DESIRE THIS TIME, ADVENTURER?
          """)
    narrate("Loading. . .", speed["fast"])

    choice = input("Please choose a number between 1 and 5 in order to continue: \n").strip()
    if choice == "1":
        display_stats()
    elif choice == "2":
        rest()
    elif choice == "3":
        explore()
    elif choice == "4":
        save_progress()
    elif choice == "5":
        quit()
    else:
        print("Invalid Option")

    narrate("", speed["slow"])