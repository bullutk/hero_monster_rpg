from character import Character
import random

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 3

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = 5

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 10
        self.power = 3
        self.coins = 8