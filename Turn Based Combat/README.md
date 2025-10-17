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
	
define fight with fighter 1 and fighter 2
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

#That should be basically everything for the basic fight