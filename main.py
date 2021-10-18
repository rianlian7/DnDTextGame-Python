
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
    2. Semi-linear
    3. Open-world

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

#
#
# playerTotal = int(input("Enter the number of players: "))
# count = 1
# while (count <= playerTotal):
#     print()
#     playerName = input(f"Enter player {count} Name: ")
#     playerJob = input(f"Enter player {count} Job: ")
#     players.append(character(playerName, playerJob, Const_MaxHp, Const_MaxArmor, True))
#     count = count + 1
#
# for player in players:
#     print()
#     print(player.status())
#
#
#
#
# event = encounters()
