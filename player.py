import items
import world
import random
import pyglet

class Player:
    def __init__(self):
        self.inventory = [items.sharpStick(), items.HealingPotion(), items.CrustyBread(), items.lizardLeg(),
                          items.Eye(), items.Toe(), items.catHair(), items.owletWing()]
        self.cauldron = []

        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.gold = 66
        self.score = 0
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def transport_to_nine(self):
        self.move(dx=1, dy=3)

    def transport_to_six(self):
        self.move(dx=-1, dy=-3)

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('*' + str(item))
            print(item.description)
        print("Gold: {}".format(self.gold))
        print("Score: {}".format(self.score))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon is your {}".format(best_weapon))

    def print_score(self):
        print("Score: " + str(self.score))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {} for {} damage!".format(best_weapon.name,
                                              enemy.name, best_weapon.damage))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}.".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return
        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}.{}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice)-1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, try again.")

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)
    def getquest(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)
    def drop_item(self):
        quest_item = [item for item in self.inventory if isinstance(item, items.QuestItem)]
        if not quest_item:
            print("You don't have anything for the cauldron!")
            return
        for i, item in enumerate(quest_item, 1):
            print("Choose an item to drop into the pot: ")
            print("{}.{}".format(i, item))


        valid = False
        while not valid:
            choice = input("")
            try:
                to_drop = quest_item[int(choice)-1]
                print("You have dropped {} into the witches cauldron.".format(to_drop.name))
                self.cauldron.append(to_drop)
                self.inventory.remove(to_drop)
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, try again.")

    def pick_up_item(self):
        quest_item = [item for item in self.cauldron if isinstance(item, items.QuestItem)]
        if not quest_item:
            print("You don't have anything in the cauldron!")
            return
        for i, item in enumerate(quest_item, 1):
            print("Choose an item to pick out of the pot: ")
            print("{}.{}".format(i, item))
        valid = False
        while not valid:
            choice = input("")
            try:
                to_pick = quest_item[int(choice) - 1]
                print("You have plucked {} out of the witches cauldron. But, it's wet now... gross"
                      "and you have burns on your fingers,"
                      "and there is a bit of newt parts stuck to your forearm...".format(to_pick.name))
                self.cauldron.remove(to_pick)
                self.inventory.append(to_pick)
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, try again.")

    def look_around(self):
        print("You begin to search the cavern, turning over every stone looking behind every stalagmite... when...")
        rand = random.randrange(10)
        if rand < 4:
            print("You found a couple of worms, which you ate... No effect.")
        elif rand < 7:
            print("You got bit by giant centipedes.")
            sting = random.randrange(10)
            self.hp = self.hp - sting
            print("You lost {} and have {} life left.".format(sting, self.hp))
        else:
            print("You found a large geode, this may fetch a pretty penny."
                  "You put it in your inventory.")
            self.inventory.append(items.geode())

    def speak(self):
        spookywitch = pyglet.media.load("resources/witchgroan.wav", streaming=False)
        spookywitch.play()
        print("You get the feeling, the witches will not help further.")

    def help(self):
        print("""
        You don't have to kill the Dragon to beat the level. You just need to put the quest items from the goblins.
         The Dragon is get out of the cave and go to "the next level" but I haven't made one yet.
        I put one of all the quest items in your inventory, so you can test for VICTORY.
        Use the hotkeys to move around. And do actions.
        Look will look for gold in places you have found gold, but you might get hurt as well.
        The Boss is very hard. Almost a certain death.
        Improve your score by exploring new areas.
        The Items are in the Correct Rooms, you can "TAKE" them by speaking to mystic goblin. He will also take them
        back, you decide your recent acquisition of wet cat hair is no longer feasible.
        The map is build like a grid. I have players "warp" from 6 to 9 and back.
        Level Map:
        |  |05|VT|EN|EN|  |  |  |
        |02|02|03|04|EN|FG|FG|BL|
        |07|FG|ST|06|TT|  |  |  |
        |  |  |08|EN|EN|  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |10|09|  |  |  |
        Extra Features: 
        You can use healing potions.
        You can find cool weapons. If you find a stronger weapon it is equiped for you.
        There are some scary sound effects.
        There is a trader to buy items from. He only shows one item at a time though...(bug)
        
        
        """)
    def riddle(self):
        print("""Every night I do what I'm told,
        So it is in the morning,
        Yet, every morn when Master awakes,
        he hits me without warning.
        What am I?""")
        answer = "Alarm Clock" or "alarm clock" or "ALARM CLOCK"
        guess = input("What sayest thou?")
        if guess == answer:
            print("Right you are, please accept this gift. It is most rare, The Gawain Sword")
            fanfare = pyglet.media.load("resources/fanfare.wav", streaming=True)
            fanfare.play()
            self.inventory.append(items.gawainSword())
        else:
            self.hp = self.hp - 75
            return "Only the wise shall receive great power."


    def quit(self):
        quit()

