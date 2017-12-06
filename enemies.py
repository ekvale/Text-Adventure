import random
import player
import items

class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Kikimora(Enemy):

    def __init__(self):
        self.name = "Kikimora"
        self.hp = 10
        self.damage = random.randrange(5)
class GingerBreadMan(Enemy):
    def __init__(self):
        self.name = "The Gingerbread Man"
        self.hp = 25
        self.damage = random.randrange(25)


class ToNoMe(Enemy):
    def __init__(self):
        self.name = "To-No-Me"
        self.hp = 3
        self.damage = random.randrange(10)

class Tesso(Enemy):
    def __init__(self):
        self.name = "Tesso"
        self.hp = 10
        self.damage = random.randrange(15)


class Tsuchinoko(Enemy):
    def __init__(self):
        self.name = "Tsuchinoko"
        self.hp = 80
        self.damage = random.randrange(30)

class WhiteDragon(Enemy):
    def __init__(self):
        self.name = "Xichulu, The Blood-Letter"
        self.hp = 800
        self.damage = random.randrange(125)