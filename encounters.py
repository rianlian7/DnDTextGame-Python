from character import *
import random
import time


class encounters:

    def __init__(self):
        randEncType = random.randint(1, 2)
        randEncTotal = random.randint(1, 3)
        randEncDiff = random.randint(1, 3)

        self.encType = 1  # 1-Battle, 2-Item
        self.encTotal = 2  # Things to do/battle/get
        self.encDiff = 1  # difficulty

    def randomEncounter(self, players):
        if self.encType == 1:  # battle
            result = self.battle(players)
            return result
        elif self.encType == 2:  # Item
            self.itemFound()
        # elif encType == 3: # chores
        #      self.chores()
        #

    def battle(self, players):
        print("Battle commence!")
        print(f"You're fighting {self.encTotal} enemies with {self.encDiff} difficulty")
        enemies = []
        for i in range(0, self.encTotal):
            enemies.append(character(f"Enemy {i + 1}", "Enemy", random.randint(3, 7), 0, False))

        print("Players:")
        for player in players:
            print(player.status())

        print("Enemies:")
        for enemy in enemies:
            print(enemy.status())
        time.sleep(1)

        while True:  # Battle phase
            print()
            while True:
                try:
                    for player in players:
                        print(player.status())
                        action = player.action()
                        if action == 1:  # attack
                            if len(enemies)>1:
                                for id, enemy in enumerate(enemies):
                                    print(f"{id + 1}. {enemy.status()}")
                                selection = int(input("Enter the enemy number to attack: "))
                            else:
                                selection = 1
                            enemies[selection - 1].damage(random.randint(1, 5))
                        elif action == 2:  # heal
                            if len(players)>1:
                                for id, player in enumerate(players):
                                    print(f"{id + 1}. {player.status()}")
                                selection = int(input("Enter the player number to heal: "))
                            else:
                                selection = 1
                            players[selection - 1].heal(random.randint(1, 3))
                        elif action == 3:  # fortify (add armor)
                            if len(players) > 1:
                                for id, player in enumerate(players):
                                    print(f"{id + 1}. {player.status()}")
                                selection = int(input("Enter the player number to fortify: "))
                            else:
                                selection = 1
                            players[selection - 1].fortify(random.randint(1, 3))
                        self.checkDead(enemies)
                        if self.checkBattle(enemies, "enemies"):
                            return True  ## battle has won
                    break
                except:
                    print("Please enter the right input. Press enter key to continue")
                    input()

            print("Enemies turn now...")
            time.sleep(1)
            for enemy in enemies:
                print(enemy.status())
                # action = enemy.action()
                action = 1
                if action == 1:  # attack
                    attackPlayer = random.randint(0, len(players) - 1)
                    print(f"{enemy.name} is attacking {players[attackPlayer].name}.")
                    time.sleep(1)
                    players[attackPlayer].damage(random.randint(1, 3))
                elif action == 2:  # heal
                    enemy.heal(random.randint(1, 3))
                elif action == 3:  # fortify (add armor)
                    enemy.fortify(random.randint(1, 3))
                self.checkDead(players)
                if self.checkBattle(players, "player"):
                    return False  ## battle has lost

    def itemFound(self):
        print("Item Found")
        print(f"You have found {self.encTotal} items with {self.encDiff} usefulness")

    # def chores(self):
    #     print("You met some dude")
    #     print(f"You have found {self.encTotal} items with {self.encDiff} usefulness")
    #

    def checkDead(self, characters):
        for person in characters:
            if person.hp == 0:
                print(f"{person.name} is dead!")
                time.sleep(1)
                characters.remove(person)

    def checkBattle(self, characters, type):
        if len(characters) == 0:
            print(f"All {type} are now dead!")
            time.sleep(1)
            print("Battle Ends")
            time.sleep(1)
            return True
        return False
