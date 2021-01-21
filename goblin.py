from character import Character

class Goblin(Character):
    def __init__(self, name = "Goblin", health = 40, power = 2):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, my_hero):
        my_hero.health -= self.power
        print("The goblin does %d damage to you." % self.power)

    # def print_status(self):
    #     print("The goblin has %d health and %d power." % (self.health, self.power))
