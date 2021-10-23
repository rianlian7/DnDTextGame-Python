import time
import random
import actions
Const_MaxHp = 10
Const_MaxArmor = 5




class character:

    def __init__(self, name, job, hp, ap, isPlayer):
        self.name = name
        self.job = job
        self.hp = hp  # health point
        self.ap = ap  # armor point
        self.isPlayer = isPlayer  # player or npc

    def description(self):
        return f"{self.name} is a {self.job}"

    def status(self):
        # return {"name": self.name,
        #         "health": self.hp,
        #         "armor": self.ap
        #         }
        return f"{self.name} ({self.job}): " \
               f" Health : {self.hp}" \
               f" | Armor : {self.ap} |"

    def selectJob(self):
        jobList = ["Paladin", "Assassin", "Archer"]
        for seq, job in enumerate(jobList):
            print(f"{seq+1} : {job}")
        while True:
            try:
                selectedJob = int(input("Enter the number to select your job: "))
                if selectedJob in range(1, len(jobList)+1):
                    self.job = jobList[selectedJob-1]
                    break
                else:
                    print("Please select job from the number above.")
            except ValueError:
                print("Please use number")

    def loadActionList(self):
        def loadActions(actionList):
            for seq, action in enumerate(actionList):
                print(f"{seq + 1}. {action.name} : {action.desc}")
        if self.job == "Paladin":
            loadActions(actions.PaladinActions)
        if self.job == "Assassin":
            loadActions(actions.AssassinActions)
        if self.job == "Archer":
            loadActions(actions.ArcherActions)



    def damage(self, dmgAmount):
        print(f"{self.name} received {dmgAmount} damages.")
        time.sleep(1)
        if self.ap > 0:  # check shield
            if dmgAmount > self.ap:
                dmgAmount = dmgAmount - self.ap
                self.ap = 0
                self.hp = self.hp - dmgAmount  # remove hp after remove all of shield
                print(f"{self.name}'s armor is broken!")
                time.sleep(1)

            else:
                self.ap = self.ap - dmgAmount
        else:  # damage health
            self.hp = self.hp - dmgAmount
            if self.hp < 0:
                self.hp = 0

        if self.ap > 0:
            print(f"{self.name} now has {self.hp} health points and {self.ap} shield left!")
            time.sleep(1)
        else:
            print(f"{self.name} now has {self.hp} health points left!")
            time.sleep(1)


    def heal(self, healAmount):
        print(f"{self.name} is healing by {healAmount}.")
        time.sleep(1)
        if self.hp < Const_MaxHp:
            self.hp = self.hp + healAmount
            if self.hp >= Const_MaxHp:
                self.hp = 10
            print(f"{self.name} health is now {self.hp} ")
            time.sleep(1)
        else:
            print(f"{self.name} health is already full! (HP: {self.hp})")
            time.sleep(1)

    def action(self):
        if self.isPlayer:
            try:
                print('''
                1. Attack
                2. Heal
                3. Fortify
                ''')
                action = int(input())
            except:
                print("Please enter the right input.")
            return action
        else:
            return random.randint(1,3)

    def fortify(self, armorAmount):
        print(f"{self.name} is adding {armorAmount} armor.")
        time.sleep(1)
        if self.ap < Const_MaxArmor:
            self.ap = self.ap + armorAmount
            if self.ap >= Const_MaxArmor:
                self.ap = Const_MaxArmor
            print(f"{self.name} now has +{self.ap} armor. ")
            time.sleep(1)
        else:
            print(f"{self.name}'s armor is full! (Armor: {self.ap})")
            time.sleep(1)

