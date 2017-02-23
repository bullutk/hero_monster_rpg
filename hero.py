from character import Character
import time
import os

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        os.system("say --voice=Maged 'Health restored'")
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

    def won_coins(self, enemy):
        self.coins += enemy.coins