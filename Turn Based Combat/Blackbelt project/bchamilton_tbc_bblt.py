import random

class Character(object):
    def __init__(self, name = "Ben",
                 hitPoints = 10,
                 hitChance = 50,
                 maxDamage = 5,
                 armor = 0):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            newValue = value
        else:
            newValue = 1
        self.__hitPoints = newValue
        
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        newValue = testInt(value)
        self.__hitChance = newValue
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        if type(value) == int:
            newValue = value
        else:
            newValue = 1
        self.__maxDamage = newValue
    
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        newValue = testInt(value)
        self.__armor = newValue
        
    def printStats(self):
        print(f"""
    {self.name}
    ==================
    Hit Points: {self.hitPoints}
    Hit Chance: {self.hitChance}
    Max Damage: {self.maxDamage}
    Armor:      {self.armor} """)
        
        print()
        
    def hit(self, enemy):
        if random.randint(1, 100) < self.hitChance:
            print(f"{self.name} hits {enemy.name}...")
            
            damage = random.randint(1, self.maxDamage)
            print(f" for {damage} points of damage.")
            
            print(f" {enemy.name}'s armor can absorb {enemy.armor} points of damage.")
            damage -= enemy.armor
            
            if damage <= 0:
                damage = 0
            enemy.hitPoints -= damage
            
class UserCharacter(Character):
    def __init__(self, name = "Ben",
                 hitPoints = 10,
                 hitChance = 50,
                 maxDamage = 5,
                 armor = 0):
        super().__init__(name, hitPoints, hitChance, maxDamage, armor)
        
    def userAction(self, enemy):
        print(f"""{self.name}'s Turn:
        1) Attack
        2) Heal
        3) Embolden """)
        
        userChoice = input("Please select an option (1-3): ")
        if userChoice == "1":
            self.hit(enemy)
        elif userChoice == "2":
            restore = random.randint(1, 3)
            print(f"You healed {restore} points.")
            self.hitPoints += restore
        elif userChoice == "3":
            buff = random.randint(1, 5)
            print("You feel stronger and more confident.")
            self.maxDamage += buff
        
            
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

def playerFight(player, opponent):
    keepGoing = True
    while keepGoing:
        player.userAction(opponent)
        opponent.hit(player)
        
        print(f"{player.name}: {player.hitPoints}")
        print(f"{opponent.name}: {opponent.hitPoints}")
        
        if opponent.hitPoints <= 0:
            print(f"{player.name} wins!")
            keepGoing = False
        elif player.hitPoints <= 0:
            print(f"{opponent.name} wins!")
            keepGoing = False
            

def aiFight(fighter1, fighter2):
    keepGoing = True
    while keepGoing:
        fighter1.hit(fighter2)
        fighter2.hit(fighter1)
        
        print(f"{fighter1.name}: {fighter1.hitPoints}")
        print(f"{fighter2.name}: {fighter2.hitPoints}")
        
        if fighter2.hitPoints <= 0:
            print(f"{fighter1.name} wins!")
            keepGoing = False
        elif fighter1.hitPoints <= 0:
            print(f"{fighter2.name} wins!")
            keepGoing = False
            
        input("Press ENTER to continue...")