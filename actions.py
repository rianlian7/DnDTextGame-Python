class actions:

    def __init__(self, name, desc, heal, damage, armor, mod=0):
        self.name = name
        self.desc = desc
        self.heal = heal
        self.damage = damage
        self.armor = armor
        self.mod = mod # for normal damage





PaladinActions = [
    actions("Sword of Hope!", "Deal 3 damage", 0, 3, 0),
    actions("Friendship is power!", "Heal 3 HP", 3, 0, 0),
    actions("Ultimate shield!", "Fortify 5 Armor", 0, 0, 5)
]

AssassinActions = [
    actions("Sneak Attack!", "Deal 3 damage", 0, 3, 0),
    actions("Hide and heal!", "Heal 3 HP", 3, 0, 0),
    actions("Put on more clothes!", "Fortify 5 Armor", 0, 0, 5)
]

ArcherActions = [
    actions("Shoot from afar!", "Deal 3 damage", 0, 3, 0),
    actions("Eating some herbs!", "Heal 3 HP", 3, 0, 0),
    actions("Taking cover!", "Fortify 5 Armor", 0, 0, 5)
]
