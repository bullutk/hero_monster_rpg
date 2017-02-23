import os

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)
        os.system("say --voice=Maged 'health increased' &")
class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)
        os.system("say --voice=Maged 'power increased' &")
class Shopping(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Shopping.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        os.system("say --voice=Maged 'Welcome to the store!!' &")
        while True:
            
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "Your health is %d and your power is %d." % (hero.health, hero.power)
            print "Do you want to buy anything?"
            for i in xrange(len(Shopping.items)):
                item = Shopping.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                os.system("say --voice=Maged 'Goodbye' &")
                break
            else:
                ItemToBuy = Shopping.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)