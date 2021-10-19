import time
from character import *
from encounters import *
from campaign import *
players = []
mainCampaign = Const_Linear

while True:
    print('''
    Welcome to the DND-inspired text-based game or something...

    Anyway, this is still in development. I create this just for the fun of practicing OOP.

    Anyhow, there are 3 types of campaign, which would you like to take a journey on?
    1. Linear
    2. Semi-linear (Not working)
    3. Open-world  (Not working)

    Enter your input with the number selection: ''')
    try:
        inputCampaign = int(input())
        if inputCampaign == 1:
            mainCampaign = campaign(Const_Linear)
            break
        elif inputCampaign == 2:
            mainCampaign = campaign(Const_Semi_Linear)
            break
        elif inputCampaign == 3:
            mainCampaign = campaign(Const_Openworld)
            break
        else:
            print("Please select the campaign using the numbers...")
    except ValueError:
        print("Please enter the campaign name using numbers")

while True:
    try:
        playerTotal = int(input("Enter the number of players: "))
        count = 1
        print()
        while (count <= playerTotal):
            playerName = input(f"Enter player {count} Name: ")
            playerJob = input(f"Enter player {count} Job: ")
            players.append(character(playerName, playerJob, Const_MaxHp, Const_MaxArmor, True))
            count = count + 1
            print()
        for player in players:
            print(player.status())

        break
    except ValueError:
        print("Please enter the number of players.")

print(f"Let's begin on a journey on our {mainCampaign.type} campaign.")
time.sleep(1)


if mainCampaign.type == Const_Linear:
    event = False
    for seq, stage in enumerate(mainCampaign.stageList):
        print(f"Stage {seq+1} : We are now in {stage} area.")
        time.sleep(1)
        event = encounters().randomEncounter(players)
        if event == True:
            print("Battle has won!")
        elif not event: # lose battle
            print("Battle has lost. GAMES END!")
            input("Press enter to end the game")
            break
        elif event == "item":
            print("Continuing journey")

        input("Please enter to go to the next stage")
    if event:
        print("Congratulation! You have reach to the end of the game")


