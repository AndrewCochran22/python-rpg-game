class Zombie:
    def __init__(self, name = "Zombie", health = 20, power = 1):
        self.health = health
        self.power = power
        self.name = name

    def attack(self, my_hero):
        my_hero.health -= self.power
        print("The zombie does %d damage to you." % self.power)

    def print_status(self):
        print("The zombie has %d health and %d power." % (self.health, self.power))

    def alive(self):
        if self.health >= 0:
            return True
        elif self.health < 0:
            print("Zombie is still moving! ")