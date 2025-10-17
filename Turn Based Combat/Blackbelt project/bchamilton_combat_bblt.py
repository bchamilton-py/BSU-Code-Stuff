import bchamilton_tbc_bblt

def oldMain():
    hero = bchamilton_tbc_bblt.Character()
    hero.name = "Achilles"
    hero.hitPoints = 1
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 4

    monster = bchamilton_tbc_bblt.Character("Hector", 20, 30, 5, 0)

    hero.printStats()
    monster.printStats()

    bchamilton_tbc_bblt.aiFight(hero, monster)
    
def main():
    game = 0
    keepGoing = True
    while keepGoing:
        userChoice = getMenuChoice()
        if userChoice == "0":
            keepGoing = False
        elif userChoice == "1":
            print("Loading AI Fight")
            game = oldMain()
        elif userChoice == "2":
            print("Loading Player Fight")
            game = playerFight()
        else:
            print("Sorry, that wasn't a valid response")

def getMenuChoice():
    print (f"""
    0) Exit
    1) Load AI Fight
    2) Load Player Fight
    """)
    userChoice = input("What will you do? ")
    return userChoice

def playerFight():
    print("""
    You can:
    ======================
    1) Create a new player
    2) Use default player """)
    
    newPlayer = input("Which would you like? (1/2): ")
    if newPlayer == "1":
        hero = bchamilton_tbc_bblt.UserCharacter()
        hero.name = getName()
        hero.hitPoints = getHitPoints()
        hero.hitChance = getHitChance()
        hero.maxDamage = getMaxDamage()
        hero.armor = getArmor()
    elif newPlayer == "2":
        hero = bchamilton_tbc_bblt.UserCharacter("Achilles", 1, 50, 5, 4)
        
    print("""
    You can:
    =====================
    1) Create a new enemy
    2) Use default enemy """)
    
    newEnemy = input("Which would you like? (1/2): ")
    if newEnemy == "1":
        monster = bchamilton_tbc_bblt.Character()
        monster.name = getName()
        monster.hitPoints = getHitPoints()
        monster.hitChance = getHitChance()
        monster.maxDamage = getMaxDamage()
        monster.armor = getArmor()
    elif newEnemy == "2":
        monster = bchamilton_tbc_bblt.Character("Hector", 20, 30, 5, 0)

    hero.printStats()
    monster.printStats()

    bchamilton_tbc_bblt.playerFight(hero, monster)

def testInt(value, min = 0, max = 100, default = 0):
    out = default
    
    if type(value) == int:
        if value >= min:
            if value <= max:
                out = value
            else:
                print("That value is too large.")
        else:
            print("That value is too small.")
    else:
        print("The value must be an integer.")
    
    return out
            

def getName():
    keepGoing = True
    while keepGoing:
        name = input("What is the new name: ")
        return name
    
def getHitPoints():
    keepGoing = True
    while keepGoing:
        try:
            newHP = testInt(int(input("How much health does this character have? (1-100): ")))
            if newHP == 0:
                print("That is outside the proper range.")
            else:
                return newHP
        except ValueError:
            print("Please enter a valid integer.")
            
def getHitChance():
    keepGoing = True
    while keepGoing:
        try:
            newHC = testInt(int(input("How likely is the character to successfully hit? (1-100): ")))
            if newHC == 0:
                print("That is outside the proper range.")
            else:
                return newHC
        except ValueError:
            print("Please enter a valid integer.")
            
def getMaxDamage():
    keepGoing = True
    while keepGoing:
        try:
            newMD = testInt(int(input("What's the most damage the character can deal? (1-100): ")))
            if newMD == 0:
                print("That is outside the proper range.")
            else:
                return newMD
        except ValueError:
            print("Please enter a valid integer.")
            
def getArmor():
    keepGoing = True
    while keepGoing:
        try:
            return testInt(int(input("How much armor is the character wearing? (1-100): ")))
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()