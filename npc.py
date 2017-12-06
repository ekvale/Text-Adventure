import items

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 1000
        self.inventory = [items.Toe(),
                          items.Eye(),
                          items.owletWing(),
                          items.catHair(),
                          items.lizardLeg(),
                          items.ironaxe(),
                          items.ironaxe(),
                          items.CrustyBread(),
                          items.CrustyBread(),
                          items.HealingPotion()
                          ]

class QuestGiver10(NonPlayableCharacter):
    def __init__(self):
        self.name = "Onoki: The Cat Groomer"
        self.gold = 500
        self.inventory = [items.catHair()]
class QuestGiver4(NonPlayableCharacter):
    def __init__(self):
        self.name = "Shisu: The Lizard Leg tickler"
        self.gold = 500
        self.inventory = [items.lizardLeg()]
class QuestGiver8(NonPlayableCharacter):
    def __init__(self):
        self.name = "Nakamora: The Owl plucker"
        self.gold = 500
        self.inventory = [items.owletWing()]
class QuestGiver7(NonPlayableCharacter):
    def __init__(self):
        self.name = "Satoshi: The Frog pickler"
        self.gold = 500
        self.inventory = [items.Toe()]
class QuestGiver2(NonPlayableCharacter):
    def __init__(self):
        self.name = "Larry: The one who has an eye for things."
        self.gold = 500
        self.inventory = [items.Eye()]
class QuestGiver3(NonPlayableCharacter):
    def __init__(self):
        self.name = "Hinter: The one who hints... Beware of Fields of Gold, beyond there lies great danger..."
        self.gold = 500
        self.inventory = [items.CrustyBread()]