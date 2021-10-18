from character import *

players = []

players.append(character("Lian", "Archer", Const_MaxHp, Const_MaxArmor, True))
players.append(character("Mien", "Mage", Const_MaxHp, Const_MaxArmor, True))

players[0].damage(11)
#players[1].damage(5)

players[0].heal(3)
players[0].addArmor(3)
players[0].damage(2)

print(players[0].status())