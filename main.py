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
		global userCode
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
	
	while(1):
		#fighter options
		if(userCode == "A"):
			#prompt
			fighterAction = input("Act with a:\nA. Slash?\nB. Roll?\nC. Charge?\n\n")
			#slash
			if(fighterAction == "A" or fighterAction == "a" or fighterAction == "Slash" or fighterAction == "slash"):
				print("SLASH wurk")
				fighterCode = "A"
				break
			#roll
			elif(fighterAction == "B" or fighterAction == "b" or fighterAction == "Roll" or fighterAction == "roll"):
				fighterCode = "B"
				print("RICKROLL")
				##NEGATE ALL DAMAGE? PERHAPS JUST DONT CHANGE THEIR HEALTH?
				break
			#charge
			elif(fighterAction == "C" or fighterAction == "c" or fighterAction == "charge" or fighterAction == "charge"):
				fighterCode = "C"
				print("CHARGE WORKD")
				#MAKE IT SO THAT THEY TAKE EXTRA DAMAGE
				break

		#wizard options
		elif(userCode == "B"):
			#prompt
			wizAction = input("Cast a(n):\nA. Attack spell?\nB. Healing spell?\nC. Curse spell?\n\n")
			#attack spell
			if(wizAction == "A" or wizAction == "a" or wizAction == "Attack Spell" or wizAction == "attack spell"):
				wizCode = "A"
				print("ATTACK WORK")
				break
			#healing spell
			elif(wizAction == "B" or wizAction == "b" or wizAction == "Roll" or wizAction == "roll"):
				wizCode = "B"
				print("HEALING GOOD")
				#restore health if past DC 15
				break
			#curse spell
			elif(wizAction == "C" or wizAction == "c" or wizAction == "charge" or wizAction == "charge"):
				wizCode = "C"
				print("CURSE GOOD")
				#DC 10 to hit, but if under 10, takes damage
				break

		#ranger options
		elif(userCode == "C"):
			#prompt
			rangeAction = input("Choose to:\nA. Shoot a normal arrow?\nB. Dodge?\nC. Shoot a fire arrow?\n\n")
			#normal
			if(rangeAction == "A" or rangeAction == "a" or rangeAction == "Shoot a normal arrow" or rangeAction == "shoot a normal arrow"):				
				rangeCode = "A"
				print("NORMAL ARROW")
				break
			#dodge
			elif(rangeAction == "B" or rangeAction == "b" or rangeAction == "Dodge" or rangeAction == "dodge"):
				rangeCode = "B"
				print("DODGE")
				#restore health if past DC 15
				break
			#fire 
			elif(rangeAction == "C" or rangeAction == "c" or rangeAction == "Shoot a fire arrow" or rangeAction == "shoot a fire arrow"):
				rangeCode = "C"
				print("FIRE")
				#DC 10 to hit, but if under 10, takes damage
				break						
		else:
			print("The nerves hit and you take a second, time slows down and you choose to...\n")

# 	#print(userAttack)

welcome()
charSelect()
#chooses the setting for the game
environment = random.randint(0,5)
environSelect(environment)
userAction()