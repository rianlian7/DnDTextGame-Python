from character import *

players = []
enemies = []

playerTotal = int(input("Enter the number of players: "))
count = 1
while (count <= playerTotal):
    playerName = input(f"Enter player {count} Name: ")
    playerJob = input(f"Enter player {count} Job: ")
    players.append(character(playerName, playerJob, Const_MaxHp, Const_MaxArmor, True))
    count = count + 1

for player in players:
    print()
    print(player.status())
