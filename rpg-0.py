from hero import Hero
from goblin import Goblin
from zombie import Zombie
from medic import Medic
from shadow import Shadow
"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    my_hero = Hero()
    goblin = Goblin()
    zombie = Zombie()
    medic = Medic()
    shadow = Shadow()

    while (goblin.alive() or zombie.alive()) and my_hero.alive():
        my_hero.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. fight zombie")
        print("3. fight medic")
        print("4. fight shadow")
        print("5. do nothing")
        print("6. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            goblin.print_status()
            # my_hero attacks goblin
            my_hero.attack(goblin)
            if goblin.health > 0:
            # Goblin attacks my_hero
                goblin.attack(my_hero)
        elif user_input == "2":
            zombie.print_status()
            my_hero.attack(zombie)
            zombie.attack(my_hero)
            zombie.alive()   
        elif user_input == "3":
            medic.print_status()
            my_hero.attack(medic)
            medic.attack(my_hero)
            medic.alive()
        elif user_input == "4":
            shadow.print_status()
            shadow.attack(my_hero)
            my_hero.attack(shadow)
            shadow.alive()
        elif user_input == "5":
            pass
        elif user_input == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        
main()