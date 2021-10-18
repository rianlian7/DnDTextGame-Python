from character import *
import random

class encounters:

    def __init__(self):
        randEncType = random.randint(1, 2)
        randEncTotal = random.randint(1, 3)
        randEncDiff = random.randint(1, 3)

        self.encType = randEncType # 1-Battle, 2-Item
        self.encTotal = randEncTotal # Things to do/battle/get
        self.encDiff = randEncDiff #difficulty:
        if self.encType == 1: # battle
            self.battle()
        elif self.encType == 2: # Item
            self.itemFound()
        # elif encType == 3: # chores
        #     self.chores()


    def battle(self):
        print("Battle commence!")
        print(f"You're fighting {self.encTotal} enemies with {self.encDiff} difficulty")
        #if self.encDiff == 1: # difficulty 1
        #    print("Easy enemy")

    def itemFound(self):
        print("Item Found")
        print(f"You have found {self.encTotal} items with {self.encDiff} usefulness")

    # def chores(self):
    #     print("You met some dude")
    #     print(f"You have found {self.encTotal} items with {self.encDiff} usefulness")
    #
