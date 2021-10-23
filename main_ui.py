#for testing

import actions
from character import  *

players = []
while True:
    try:
        count = 1
        print()
        while (count <= 1):
            playerName = input(f"Enter player {count} Name: ")
            # playerJob = input(f"Enter player {count} Job: ")
            setupPlayer = character(playerName, "", Const_MaxHp, Const_MaxArmor, True)
            setupPlayer.selectJob()
            players.append(setupPlayer)

            count = count + 1
            print()
        for player in players:
            print(player.status())

        break
    except ValueError:
        print("Please enter the number of players.")


players[0].loadActionList()
input("Please select")
