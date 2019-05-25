#Trent + Matt's wild [text] adventure

import random

def welcome():
	print("\n ~ Welcome to Trent & Matt's Wild [text] Adventure! ~\n")
	print("You find yourself in a prison, the door opens, and a gruff voice yells at you..")
	userName = input("'Whats your name, prisoner?'\n\n")
	print("\nOkay,", userName, "get out there and fight for your life\nBest of luck *wink*\n...\n")

def charSelect():
	print("As you get up, the chains jangle, and you look down at yourself\n")

	while(1):
		userClass = input("Are you be a:\nA. fighter\nB. wizard\nC. ranger?\n\n")

		if(userClass == "A" or userClass == "a" or userClass == "fighter" or userClass == "Fighter"):
			userCode = "A"
			fighterWeapon = "sword"
			fighterDMG = 3 #just adjust the random number generation for it to be easier to hit
			fighterHealth = 50
			print("You feel your muscles strengthen and your hand clasps around the sword given to you...\n")
			break

		elif(userClass == "B" or userClass == "b" or userClass == "wizard" or userClass == "Wizard"):
			userCode = "B"
			wizWeapon = "wand"
			wizDMG = 5 #slightly harder to hit
			wizHealth = 35
			print("Arcane energy rushes through your veins and at the touch of your wand, you come to your magical senses...\n")
			break

		elif(userClass == "C" or userClass == "c" or userClass == "ranger" or userClass == "Ranger"):
			userCode = "C"
			rangerWeapon = "bow & arrow"
			rangerDMG = 7 #hardest to hit
			rangerHealth = 30
			print("As you test the string of your bow, you feel the energy of the bows thwang reverberate within you...\n")
			break
		else:
			print("Your vision is foggy, and you can't quite see. As you rub your eyes you look down and see...\n")

def environSelect(val):
	if(val == 1):
		print("And as the door opens, you are nearly blinded with the sharp reflection of the sun on a sea of sand.")
		print("The heat is draining, but in the distance an armed opponent is walking towards you...\n") 
	elif(val == 2):
		print("And as the door opens, the superficial torch light becomes the brightest beacon in a dull forest.")
		print("As the wind howls and you see red eyes blink in the distance, a figure, with weapon in hand approaches...\n")
	else:
		print("And as the door slams open, a deafening roar of shouts and screams and song from a crowd cheer at your potential demise.")
		print("Among the bloodthirsty fans and vendors trying to make a living, bets are tossed around and an armed opponent challenges you...\n")

def userAction():
	#fighter options
	while(1):
		if(userCode == "A"):
			#prompt
			fighterAction = input("Will you:\nA. Slash?\nB. Roll?\nC. Charge?\n\n")
			#slash
			if(fighterAction == "A" or userClass == "a" or userClass == "Slash" or userClass == "slash"):
				fighterCode = "A"
				break
			#roll
			elif(userClass == "B" or userClass == "b" or userClass == "Roll" or userClass == "roll"):
				fighterCode = "B"
				##NEGATE ALL DAMAGE? PERHAPS JUST DONT CHANGE THEIR HEALTH?
				break
			#charge
			elif(userClass == "C" or userClass == "c" or userClass == "charge" or userClass == "charge"):
				fighterCode = "C"
				#MAKE IT SO THAT THEY TAKE EXTRA DAMAGE
				break
			else:
				print("The nerves hit and you take a second, time slows down and you choose to...\n")

	# #wizard options
	# elif(userCode == "B"):
	# 	#attack spell
	# 	#healing spell
	# 	#
	# #ranger options
	# else:
	# 	#fire arrow
	# 	#dodge
	# 	#normal arrow

# 	#userAction = input("How will you attack?\n")
# 	#print(userAttack)

welcome()
charSelect()
#chooses the setting for the game
environment = random.randint(0,5)
environSelect(environment)