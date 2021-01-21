from character import Character
import random

class Medic(Character):
    def __init__(self, name = "Medic", health = 60, power = 5):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, my_hero):
        if random.randint(0, 100) < 20:
            self.health = self.health + 2
            print("The medic has recuperated 2 health %s!" % self.health)
        else:
            my_hero.health -= self.power
            print("The medic does %d damage to you." % self.power)

    # def print_status(self):
    #     print("The medic has %d health and %d power." % (self.health, self.power))
