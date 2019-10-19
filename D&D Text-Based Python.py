import random
import os


## Display player stats
def player_stats():
    for x in regPlayer:
        print(regPlayer[x]["Name"] + ": " + 
        regPlayer[x]["Class"] + 
        " HP:" + str(regPlayer[x]["HP"]) + 
        " Str:" + str(regPlayer[x]["Str"]) + 
        " Int:" + str(regPlayer[x]["Int"]) + 
        " Agi:" + str(regPlayer[x]["Agi"]))

## Decides Class
def chooseClass():
    for x in range(len(player_list)):
        print("\n"+ player_list[x] + ", Select your class")
        print("1:Warrior\n2:Rogue\n3:Mage")
        pClass = 0
        i = 0
        while i != 1:
            pClass = input()
            if pClass == "1":
                print(player_list[x] + " have selected WARRIOR")
                regPlayer["Player " +str(x+1)] = {"Name" : player_list[x],
                                                "Class" : "Warrior",
                                                "HP" : 15,
                                                "Str" : 15,
                                                "Int" : 10,
                                                "Agi" : 13}
                i = 1
            elif pClass == "2":
                print(player_list[x] + " have selected ROGUE")
                regPlayer["Player " +str(x+1)] = {"Name" : player_list[x],
                                                "Class" : "Rogue",
                                                "HP" : 13,
                                                "Str" : 13,          
                                                "Int" : 10,
                                                "Agi" : 15}
                i = 1
            elif pClass == "3":
                print(player_list[x] + " have selected MAGE")
                regPlayer["Player " +str(x+1)] = {"Name" : player_list[x],
                                                "Class" : "Mage",
                                                "HP" : 10,                                          
                                                "Str" : 10,
                                                "Int" : 15,
                                                "Agi" : 13}
                i = 1 
            else:
                print("There's no such class, please select the class provided\n1:Warrior\n2:Rogue\n3:Mage")

## List players
def listPlayers():    
    for x in range(nPlayer):
        y = x+1
        player_list.append(str(input("Player " + str(y) + " name:")))
        player_score.append(int(0))
    
    print("The champions: ", end = '')
    for y in range(len(player_list)):
        print('|' + player_list[y], end = '| ')

    print("\n")

## Decides numbers of levels     
def deLevel():
    min = 1
    max = 12
    diceNum = 2
    totalLevel = 0
    i = 1
    input("\nPress Enter to roll dices...")
    print("rolling dices...")
    while i <= int(diceNum):
        diceRe = random.randint(min, max)
        print("Dice " + str(i) + ": " + (str(diceRe)))
        i += 1
        totalLevel += diceRe

    for x in range(totalLevel):
        x += 1
        levels.append(x)

## Need Refining
def delevelCond():
    min = 1
    max = 6
    input("Press enter to roll dice for level condition")
    print("rolling dice...")
    levelCond = random.randint(min, max)
    currentCond = levelCond
    if currentCond == 1:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] -= 5
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] -= 3
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] -= 3
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] -= 3

    if currentCond == 2:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] -= 3
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] -= 2
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] -= 2
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] -= 2
    
    if currentCond == 3:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] += 0
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] -= 1
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] -= 1
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] -= 1

    if currentCond == 4:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] += 1
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] += 0
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] += 0
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] += 0
    
    if currentCond == 5:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] += 3
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] += 1
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] += 1
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] += 1
    
    if currentCond == 6:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] += 5
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] += 2
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] += 2
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] += 2

    player_stats()

## reset player stats after every level
def resetLevelCond():
    resCond = currentCond
    if resCond == 1:
        for x in regPlayer:
            regPlayer[x]["HP"] += 5
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] += 3
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] += 3
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] += 3

    if resCond == 2:
        for x in regPlayer:
            regPlayer[x]["HP"] += 3
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] += 2
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] += 2
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] += 2
    
    if resCond == 3:
        for x in regPlayer:
            regPlayer[x]["HP"] += 0
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] += 1
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] += 1
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] += 1

    if resCond == 4:
        for x in regPlayer:
            regPlayer[x]["HP"] -= 1
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] -= 0
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] -= 0
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] -= 0
    
    if resCond == 5:
        for x in regPlayer:
            regPlayer[x]["HP"] -= 2
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] -= 1
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] -= 1
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] -= 1
    
    if resCond == 6:
        for x in regPlayer:
            regPlayer[x]["HP"] -= 3
            if regPlayer[x]["Class"] == "Warrior":
                regPlayer[x]["Str"] -= 2
            if regPlayer[x]["Class"] == "Rogue":
                regPlayer[x]["Agi"] -= 2
            if regPlayer[x]["Class"] == "Mage":
                regPlayer[x]["Int"] -= 2
    player_stats()

## Decides what player encounter in every level
def player_encounter():
    min = 1
    max = 6
    input("Press 'Enter' to know what you have encountered")
    print("walking...")
    encounters = random.randint(min, max)
    
    if encounters == 1:
        print("Encounter 1")

    if encounters == 2:
        print("Encounter 2")

    if encounters == 3:
        print("Encounter 3")

    if encounters == 4:
        print("Encounter 4")

    if encounters == 5:
        print("Encounter 5")

    if encounters == 6:
        print("Encounter 6")



os.system('cls') 
nPlayer = int(input("Enter number of players: "))
player_list = []
player_score = []
regPlayer = {}
levels = []
currentLevel = 1
currentCond = 0


# Intro
listPlayers()
chooseClass()
player_stats()
deLevel()

print("There will be " + str(len(levels)) + " levels")
input("Let the quest begin!")

## Begin Quest
while currentLevel <= len(levels):    
    print("\nThe champions are now at Level " + str(currentLevel))
    currentLevel += 1
    delevelCond()
    player_encounter()
    resetLevelCond()





print("Congratulation! You have completed your quest!")
    

    
