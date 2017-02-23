"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
from character import Character
from hero import Hero
from monster import Goblin
from monster import Wizard
from monster import Zombie
from store import Shopping
from battle import Battle
import os

hero = Hero()
enemies = [Goblin(), Wizard(), Zombie()]
battle_engine = Battle()
shopping_engine = Shopping()
os.system("say --voice=Maged 'Welcome to this amazing game!!'")
for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        os.system("say --voive=Maged 'you loose sucker!!'")
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
os.system("say --voice=Maged 'you won the game!!'")
