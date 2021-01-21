class Character:

    def alive(self):
        if self.health <= 0:
            print("Dead! ")
            return False
        elif self.health > 0:
            return True

    def print_status(self, name = " "):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print("You do %d damage to the %s." % (self.power, enemy))

    # def attack(self, my_hero):
    #     my_hero.health -= self.power
    #     print("The goblin does %d damage to you." % self.power)