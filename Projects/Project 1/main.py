# -- Importing Modules
import os
import time
import random

# -- Variables & Misc. Functions
isRunning = True
saveFilePath = "Projects/Project 1/save_file.txt"
playerData = {
    "NAME" : "",
    "HEALTH" : 100,
    "GOLD" : 0
}
speed = {
    "fast" : 0.5,
    "moderate" : 1,
    "slow" : 2.5
}
def loading_time(text, amount):
    print(text)
    time.sleep(amount)

# -- Functions
# - Starting functions
def intro_cutscene(type):
    if "new" in type:
        print("- WELCOME . . . TO THIS EXCITING NEWADVENTURE \n")
        loading_time("", speed["fast"])
        print("- BEFORE WE CONTINUE, I'D LIKE TO KNOW MORE ABOUT YOU...\n")
        loading_time("", speed["fast"])

        playerData["NAME"] = input("* * Type your username: * *\n")
        loading_time("", speed["fast"])

        print("     EXCELLENT . . . \n- SHALL WE CONTINUE?")
        loading_time("", speed["slow"])
    elif "old" in type:
        print(f"- WELCOME BACK, {playerData["NAME"]}") 
        loading_time("", speed["moderate"])
def load_save_data():
    if os.path.exists(saveFilePath):
        with open(saveFilePath, "r") as file:
            for line in file:
                key, value = line.replace(" ", "").strip().split(":")
                if key in ("HEALTH", "GOLD"):
                    value = int(value)
                playerData[key] = value
        print("Succesfully Found & Loaded Save File")
        loading_time("", speed["moderate"])

        intro_cutscene("old")
    else:
        intro_cutscene("new")

        with open (saveFilePath, "x") as file:
            for key, value in playerData.items():
                file.write(f"{key} :    {value}\n")

# - Menu functions
def display_stats():
    print("- HAVE A PEEK AT YOUR STATS . . .\n\n")
    loading_time("", speed["fast"])

    for key, value in playerData.items():
        print(f"{key} : {value}")
def rest():
    restGoldCost = 10
    restHealAmount = 25 # Adding unique variables for the Rest feature since I plan to expand further upon this in the future

    if playerData["GOLD"] >= restGoldCost:
        playerData["HEALTH"] += restHealAmount 
        playerData["GOLD"] = playerData["GOLD"] - restGoldCost 

        print("Succesfully Rested")
    else:
        print("- YOU DON'T SEEM TO HAVE ENOUGH RESOURCES, ADVENTURER...")
def explore():
    def find_gold():
        print("You explored in search for Gold and...")
        loading_time("", speed["slow"])

        randomNum = random.randint(0, 50)

        if randomNum > 0:
            playerData["GOLD"] += randomNum
            print(playerData["GOLD"])

            print("You found Gold!")
            loading_time("", speed["fast"])
            print(f"- CONGRATULATIONS ADVENTURER, YOU HAVE FOUND {randomNum:03} GOLD")
        else:
            print("found nothing...")
            loading_time("", speed["moderate"])
            print("- . . . UNLUCKY")
    def lose_health():
        print("You explored in the wilderness and...")
        loading_time("", speed["slow"])

        randomNum = random.randint(0, playerData["HEALTH"])

        if randomNum > 0:
            playerData["HEALTH"] -= randomNum
            print(playerData["HEALTH"])

            print("You got attacked by a creature!")
            loading_time("", speed["fast"])
            print(f"- OUCH. . . YOU HAVE LOST {randomNum} HP")
        else:
            print("Nothing happened")
    def healing_herb():
        print("You explored in the wilderness and...")
        loading_time("", speed["slow"])

        randomNum = round(random.uniform(1, playerData["HEALTH"] * 0.87))

        playerData["HEALTH"] += randomNum
        print(playerData["HEALTH"])

        print("You found a Healing Herb!")
        loading_time("", speed["fast"])
        print(f"- CONGRATULATIONS ADVENTURER, YOU HAVE GAINED {randomNum} HP")
    def nothing_happens():
        print("You explored...")
        loading_time("", speed["slow"])
        print("but nothing relevant happened")

    events = [
        find_gold,
        lose_health,
        healing_herb,
        nothing_happens
    ]

    choosenEvent = random.choice(events)
    choosenEvent()
def save_progress():
    choice = input(f"- ARE YOU SURE YOU WANT TO REWRITE YOUR SAVE, ADVENTURER?  (y/n)\n").strip().lower()
    loading_time("", speed["moderate"])

    if "y" in choice:
        with open(saveFilePath, "w") as file:
            for key, value in playerData.items():
                file.write(f"{key} :    {value}\n")

        print("Saved Succesfully")
    elif "n" in choice:
        print("Aborted Save File Rewritting")
    else:
        print("Invalid Option")
    
    print()
def quit():
    saveChoice = True
    while saveChoice:
        choice = input("Save Before Quitting?   (y/n)\n").strip().lower()

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
        
        loading_time("", speed["slow"])

    print("- UNTIL NEXT TIME, ADVENTURER")
    loading_time("", speed["moderate"])
    print("\n\n  .  .  .  Terminating Program  .  .  . \n\n")

    exit()

# - Other functions
def game_over():
    print(f"- IT SEEMS LIKE WE LOST YOU... \n- {playerData["NAME"]}! IT WAS NICE TO MEET YOU!")
    loading_time("", speed["fast"])
    print("\n\n  .  .  .  Game Over  .  .  . \n\n")
    loading_time("", speed["moderate"])

    choice = input("Would you like to start over?  (y/n)\n")
    loading_time("", speed["fast"])
    if "y" in choice:
        if os.path.exists(saveFilePath):
            os.remove(saveFilePath)
        print("\nCome back soon. . .\n")
    elif "n" in choice:
        loading_time(". . .", speed["moderate"])
        print("But aren't you dead?")
def player_status():
    if playerData["HEALTH"] > 0:
        isAlive = True
    else:
        isAlive = False

    return isAlive

# - Main functions
def menu_loop():
    print(f"""
- WELCOME TO THE MENU, {playerData["NAME"]}\n- WHAT WOULD YOU LIKE TO DO?

    1- View Stats
    2- Rest (costs 10$)
    3- Explore
    4- Save
    5- Quit

- WHAT DO YOU DESIRE THIS TIME, ADVENTURER?
          """)
    loading_time("", speed["moderate"])

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

    loading_time("", speed["slow"])
def main_loop():
    print("\n  .  .  .  Initiating Program  .  .  .  \n")
    loading_time("", speed["moderate"])

    load_save_data()

    if player_status() == True:
        while player_status():
            menu_loop()
    else:
        game_over()
        
# -- Main Function Callings
main_loop() 