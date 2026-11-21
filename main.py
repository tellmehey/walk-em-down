# wow look at me im here lol...
import darkgui as dark
import random

dayEvents = []
day = 0
level = 1

gameStat = int(input("Walk Em Down Winters\n1. [New Game]\n2. [Settings]\n > "))

def hellSpawn(demon, level, skill, fat):
    demon.health = 2 * (fat - 1) + 5
    demon.dmg = 1 + level + (skill // 3)

if gameStat == 2:
    print("Settings are not available yet.")
elif gameStat == 1:
    for i in range(365):
        dayEvents.append(random.randint(10))
    while gameStat == 1:
        input("demo")
    print("Goodbye.")