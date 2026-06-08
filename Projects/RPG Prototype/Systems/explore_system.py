import random
from config import *
from Systems.utils import narrate

def explore():
    def find_gold():
        print("\nYou explored in search for Gold and...")
        narrate("", speed["slow"])

        randomNum = random.randint(0, 50)

        if randomNum > 0:
            playerData["GOLD"] += randomNum

            print("You found Gold!")
            narrate("", speed["fast"])
            print(f"- CONGRATULATIONS ADVENTURER, YOU HAVE FOUND {randomNum:03} GOLD")
        else:
            print("found nothing...")
            narrate("", speed["moderate"])
            print("- . . . UNLUCKY")
    def lose_health():
        print("\nYou explored in the wilderness and...")
        narrate("", speed["slow"])

        randomNum = random.randint(0, playerData["HEALTH"])

        if randomNum > 0:
            playerData["HEALTH"] -= randomNum

            print("You got attacked by a creature!")
            narrate("", speed["fast"])
            print(f"- OUCH. . . YOU HAVE LOST {randomNum} HP")
        else:
            print("Nothing happened")
    def healing_herb():
        print("\nYou explored in the wilderness and...")
        narrate("", speed["slow"])

        randomNum = round(random.uniform(1, playerData["HEALTH"] * 0.87))

        playerData["HEALTH"] += randomNum

        print("You found a Healing Herb!")
        narrate("", speed["fast"])
        print(f"- CONGRATULATIONS ADVENTURER, YOU HAVE GAINED {randomNum} HP")
    def nothing_happens():
        print("\nYou explored...")
        narrate("", speed["slow"])
        print("but nothing relevant happened")

    events = [
        find_gold,
        lose_health,
        healing_herb,
        nothing_happens
    ]

    choosenEvent = random.choice(events)
    choosenEvent()
