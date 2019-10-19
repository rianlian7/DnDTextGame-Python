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
                                                "HP" : 15,
                                                "Str" : 13,          
                                                "Int" : 10,
                                                "Agi" : 15}
                i = 1
            elif pClass == "3":
                print(player_list[x] + " have selected MAGE")
                regPlayer["Player " +str(x+1)] = {"Name" : player_list[x],
                                                "Class" : "Mage",
                                                "HP" : 15,                                          
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

    if levelCond == 1:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] -= 5

    if levelCond == 2:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] -= 3
    
    if levelCond == 3:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] += 0
    
    if levelCond == 4:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] += 1
    
    if levelCond == 5:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] += 3

    if levelCond == 6:
        print("You have entered " + str(levelCond))
        for x in regPlayer:
            regPlayer[x]["HP"] += 5

    player_stats()

## In progress
def battleMode():
    
    HP = 15
    for x in regPlayer:
        DMG = regPlayer[x]["Str"]*0.75

    HP -= DMG
    

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


print("Congratulation! You have completed your quest!")
    

