import random

create a character class
	define method initializer
		necessary attribute inclusions
			name = Ben
			hitPoints = 10
			hitChance = 50
			maxDamage = 5
			armor = 0
		super().init()
		self.name = name
		self.hitPoints = hitPoints
		self.hitChance = hitChance
		self.maxDamage = maxDamage
		self.armor = armor
		
	#This is just the character class
	#We now need to provide properties and setters for each attribute
	#For this I'm going to include a function you recommended for setting the bounds
	
	property
	define name of self
		return name of self (private)
		
	name setter
	define name of self + value
		name of self (private) = value
		
	#Name is by far the easiest property to set
	
	property
	define hitPoints of self
		return hitPoints of self (private)
	
	hitPoints setter
	define hitPoints of self + value
		check that value is an integer
		if it is
			newValue = value
		if it isn't
			newValue = 1
		hitPoints of self (private) = newValue
	
	#Bit more difficult but nothing arduous yet. The following properties require functions.
	
	property
	define hitChance of self
		return hitChance of self (private)
		
	hitChance setter
	define hitChance of self + value
		testInt(value) = newValue
		hitChance of self (private) = newValue
	
	#The testInt function makes this very easy because within the setter,
	#I don't need to think about how to set parameters. It does it for me.
	#Praise be to functions.
	
	property
	define maxDamage of self
		return maxDamage of self (private)
		
	maxDamage setter
	#I tossed around not allowing maxDamage to be negative but I allowed it just this once
	#as a treat
	define maxDamage of self + value
		check that value is an integer
		if it is
			newValue = value
		if it isn't
			newValue = 1
		maxDamage of self (private) = new value
		
	#Final stretch now, just armor left in the character attributes
	
	property
	define armor of self
		return armor of self (private)
	
	armor setter
	define armor of self + value
		testInt(value) = newValue
		armor of self (private) = newValue
	
	#That wraps up the attributes, now we need to get into the meat of the project.
	
	define printStats of self
		print
	name
	================
	Hit Points: hitPoints of self
	Hit Chance: hitChance of self
	Max Damage: maxDamage of self
	Armor:      armor of self
	
	#This should print a properly formatted stat table
	
	define hit function between self and enemy
		check if a random number between 1 and 100 is less than hitChance of self
		#This only works if it's less than, if you do greater than it breaks the 
		#Probability. Consider a hit chance of 60 in the greater than model only
		#hits if you pull the 40 numbers greater than 60.
			say that self hit enemy
			set variable damage to the a random damage between 1 and maxDamage
			say the damage dealt
			tell the viewer the damage that enemy's armor can take
			subtract enemy armor from damage variable
			check damage is greater than zero, if not set damage to zero
			subtract damage from enemy hitPoints

#Now we need to build a UserCharacter that is a subclass of character
class UserCharacter(Character)
	define the initializer again
		this time when you do the super().init() you include the inherited attributes
		
	#Super easy to create but now we need to give the UserCharacter the illusion of free will
	define userAction with self and enemy
		print that it's the user's turn and give them 3 options
		1) Attack
		2) Heal
		3) Embolden
		
		create userChoice variable and take input "Please select an option (1-3):"
		if userChoice is 1
			self.hit the enemy
		elif userChoice is 2
			create variable restore and set it a random number including (1-3)
			tell the player how much they've been healed
			self.hitPoints has restore added to it
		elif userChoice is 3
			create buff variable and set it a random number including (1-5)
			Tell the player they've gotten stronger
			self.maxDamage gets buff added to it
	
	#That's all of player choice, now we just need to create the fight mechanic for PvE

define playerFight with player and opponent
	keepGoing = True 
	while keepGoing
		player.userAction(UserCharacter, opponent)
		opponent.hit(UserCharacter)
		
		
		print player hitPoints
		print opponent hitPoints
		
		if opponent hitPoints <= 0
			tell the player they wins
			keepGoing false
		elif player hitPoints <= 0
			tell player they lose
			keepGoing false
	

#Now we need to start building the functions that aren't part of the character class

define testInt of value + min = 0 + max = 100 + default = 0
	create out and set it default
	if value is an integer
		and value is greater than min
			and value is less than Max
				set out to value
			otherwise
				say it's too large
		other wise
			say it's too small
	otherwise
		explain it must be an integer
	
	return out
	
define aifight with fighter1 and fighter2
	keepGoing true
	while keepGoing loop
		fighter 1 hits fighter 2
		fighter 2 hits fighter 1

		print fighter 1 hitPoints
		print fighter 2 hitPoints

		check if fighter 2 hitPoints are less than or equal to zero
			print fighter 1 wins
			keepGoing false
		otherwise if fighter 1 hitPoints are less than or equal to zero
			print fighter 2 wins
			keepGoing false
		
		input "Press ENTER to continue..."

#That should be basically everything for the blackbelt tbc module
#This was pretty basic improvements, the real special bit is what I plan to do with
#the combat module. We're redesigning this whole thing.

import the tbc module

define oldMain()
	create a hero with the tbc.Character()
	assign a name
	assign hitPoints
	assign hitChance
	assign maxDamage
	assign armor
	
	create a monster with the same stuff
	
	print hero stats
	print monster stats
	
	run the aifight function in the tbc module
	
#This is the only part that stays the same

create the main function
	create variable game with arbitrary value 0
	keepGoing True
	while keepGoing
		create variable userChoice to call the function getMenuChoice()
		if userChoice is 0
			keepGoing false
		elif userChoice is 1
			print that you're loading the ai fight
			game is set to oldMain function
		elif userChoice is 2
			print that you're loading player fight
			game is given playerFight module
		else
			tell them this is an invalid response
			
define getMenuChoice function
	print options
	0) Exit
	1) Load AI fight
	2) Load Player fight
	userChoice is set to the answer of "What will you do?"
	return userChoice
	
define playerFight function
	print options
	1) create new player
	2) use default player
	
	newplayer is set to the user's answer
	if newPlayer equals 1
		hero gets tbc.UserCharacter
		hero.name calls getName()
		hero.hitPoints calls getHitPoints()
		hero.hitChance callse getHitChance()
		hero.maxDamage calls getMaxDamage()
		hero.armor calls getArmor()
	elif newPlayer equals 2
		hero gets tbc.UserCharacter("Achilles", 1, 50, 5, 4)
		
	print options
	1) create new enemy
	2) use default enemy
	
	newEnemy gets the answer
	if newEnemy equals 1
		monster tbc.UserCharacter
		monster.name calls getName()
		monster.hitPoints calls getHitPoints()
		monster.hitChance callse getHitChance()
		monster.maxDamage calls getMaxDamage()
		monster.armor calls getArmor()
	elif newEnemy equals 2
		monster gets tbc.UserCharacter(""Hector", 20, 30, 5, 0)
		
	print hero stats
	print monster stats
	
	call the playerfight module with hero and monster
	
I then made the testInt function in the combat module

define getName() function
	while keepGoing
		name = input "what is the new name?"
		return name
		
define getHitPoints function
	while keepGoing loop
		try: 
			newHP gets the testInt result of "how much health does the character have?"
			if newHP is 0
				tell them that is outside the proper range
			else
				return newHP
		except ValueError
			print "please enter a valid integer"
			
define getHitChance function
	while keepGoing loop
		try: 
			newHC gets the testInt result of "how likely is the character to successfully hit?"
			if newHC is 0
				tell them that is outside the proper range
			else
				return newHC
		except ValueError
			print "please enter a valid integer"
			
define getMaxDamage function
	while keepGoing loop
		try: 
			newMD gets the testInt result of "What's the most damage the character can deal?"
			if newMD is 0
				tell them that is outside the proper range
			else
				return newMD
		except ValueError
			print "please enter a valid integer"
			
define getArmor function
	while keepGoing loop
		try: 
			return the testInt result of "how much armor is the character wearing"
		except ValueError
			print "please enter a valid integer"
			
if __name__ == "__main__":
	run main()