class actions:

    def __init__(self, name, desc, heal, damage, armor):
        self.name = name
        self.desc = desc
        self.heal = heal
        self.damage = damage
        self.armor = armor


PalActions = [
    actions("Sword of Hope!", "Deal 3 damage", 0, 3, 0),
    actions("Friendship is power!", "Heal 3 HP", 0, 3, 0),
    actions("Ultimate shield!", "Fortify 5 Armor", 0, 0, 5)

]