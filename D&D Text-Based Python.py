import random
import os

os.system('cls') 
nPlayer = int(input("Enter number of players: "))
player_list = []
player_score = []
regPlayer = {}
levels = []

def player_stats():
    for x in regPlayer:
        print(regPlayer[x]["Name"] + ": " + 
        regPlayer[x]["Class"] + 
        " HP:" + str(regPlayer[x]["HP"]) + 
        " Str:" + str(regPlayer[x]["Str"]) + 
        " Int:" + str(regPlayer[x]["Int"]) + 
        " Agi:" + str(regPlayer[x]["Agi"]) + 
        " DMG:" + str(regPlayer[x]["DMG"]))

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
                                                "Agi" : 13,
                                                "DMG" : 15}
                i = 1
            elif pClass == "2":
                print(player_list[x] + " have selected ROGUE")
                regPlayer["Player " +str(x+1)] = {"Name" : player_list[x],
                                                "Class" : "Rogue",
                                                "HP" : 15,
                                                "Str" : 13,          
                                                "Int" : 10,
                                                "Agi" : 15,
                                                "DMG" : 15}
                i = 1
            elif pClass == "3":
                print(player_list[x] + " have selected MAGE")
                regPlayer["Player " +str(x+1)] = {"Name" : player_list[x],
                                                "Class" : "Mage",
                                                "HP" : 15,                                          
                                                "Str" : 10,
                                                "Int" : 15,
                                                "Agi" : 13,
                                                "DMG" : 15}
                i = 1 
            else:
                print("There's no such class, please select the class provided\n1:Warrior\n2:Rogue\n3:Mage")

def listPlayers():    
    for x in range(nPlayer):
        y = x+1
        player_list.append(str(input("Player " + str(y) + " name:")))
        player_score.append(int(0))
    
    print("The champions: ", end = '')
    for y in range(len(player_list)):
        print('|' + player_list[y], end = '| ')

    print("\n")
        
def deLevel():
    min = 1
    max = 12
    diceNum = 2
    i = 1
    totalLevel = 0
    input("\nPress Enter to roll dices...")
    print("rolling dices...")
    while i <= int(diceNum):
        diceRe = random.randint(min, max)
        print("Dice " + str(i) + ": " + (str(diceRe)))
        i += 1
        totalLevel += diceRe
    print("There will be " + str(totalLevel) + " levels")
    
    for x in range(levels):
        levels.append = x

listPlayers()
chooseClass()
player_stats()
deLevel()


    

    
