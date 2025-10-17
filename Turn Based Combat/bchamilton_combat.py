import bchamilton_tbc

def main():
    hero = bchamilton_tbc.Character()
    hero.name = "Achilles"
    hero.hitPoints = 1
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 5

    monster = bchamilton_tbc.Character("Hector", 20, 30, 5, 0)

    hero.printStats()
    monster.printStats()

    bchamilton_tbc.fight(hero, monster)

if __name__ == "__main__":
    main()