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
        return f"{self.name} the {self.job} status: " \
               f"\nHealth : {self.hp}" \
               f"\nArmor : {self.ap}"

    def damage(self, dmgAmount):
        print(f"{self.name} received {dmgAmount} damages.")
        if self.ap > 0: # check shield
            if dmgAmount > self.ap:
                dmgAmount = dmgAmount - self.ap
                self.ap = 0
                self.hp = self.hp - dmgAmount # remove hp after remove all of shield
                print(f"{self.name}'s armor is broken!")
            else:
                self.ap = self.ap - dmgAmount
        else: # damage health
            self.hp = self.hp - dmgAmount
            if self.hp < 0:
                self.hp = 0

        print(f"{self.name} now has {self.hp} health points left!")
        if self.ap > 0:
            print(f"{self.name} now has {self.ap} shield left!")

    def heal(self, healAmount):
        print(f"{self.name} is healing by {healAmount}.")
        if self.hp < Const_MaxHp:
            self.hp = self.hp + healAmount
            if self.hp >= Const_MaxHp:
                self.hp = 10
            print(f"{self.name} health is now {self.hp} ")
        else:
            print(f"{self.name} health is already full! (HP: {self.hp})")

    def addArmor(self, armorAmount):
        print(f"{self.name} is adding {armorAmount} armor.")
        if self.ap < Const_MaxArmor:
            self.ap = self.hp + armorAmount
            if self.ap >= Const_MaxArmor:
                self.ap = Const_MaxArmor
            print(f"{self.name} armor is now {self.ap} ")
        else:
            print(f"{self.name}'s armor is full! (Armor: {self.ap})")
