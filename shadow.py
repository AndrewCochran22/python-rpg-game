from character import Character
import random

class Shadow(Character):
    def __init__(self, name = "Shadow", health = 100, power = 10):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, my_hero):
        if random.randint(0, 100) < 90:
            self.health == 1
            my_hero.health -= self.power
            print("The shadow does %d damage to you." % self.power)

