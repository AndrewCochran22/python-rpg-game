from character import Character
import random

class Hero(Character):
    def __init__(self, name = "Cartman", health = 100, power = 10):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        if random.randint(0, 100) < 20:
            enemy.health -= self.power * 2
            print("Critical Hit! %d damage to the %s." % (self.power * 2, enemy.name))
        else:
            enemy.health -= self.power
            print("You do %d damage to the %s." % (self.power, enemy.name))

    # def attack(self, zombie):
    #     zombie.health -= self.power
    #     # zombie.health += self.power
    #     print("You do %d damage to the zombie. " % self.power)
