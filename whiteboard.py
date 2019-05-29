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

def actionOutcome(actionCode, username, enemyName):
	comm = random.randint(1,3)

	if(userCode == "A")	#fighter
		if(actionCode == 'A1S'):
			if(comm == 1):
				print("Blood spurts as you slash through their worn armor...\n")
			if(comm == 2):
				print("A deft slash cuts across " + enemyName + "'s chest...\n")
			if(comm == 3):
				print("As the adrenaline pumps through your veins, you slash down on" + enemyName + "...\n")	#DONE
		elif(actionCode == 'A1F'):
			if(comm == 1):
				print("With a whistle of your blade in the wind, you miss " + enemyName + "...\n")
			if(comm == 2):
				print("With a grin and a chuckle " + enemyName + " yells at you: Is that all you got, " + userName + "? ...\n")
			if(comm == 3):
				print("A swing, and... a miss! Sorry, " + userName + "...\n")	#DONE
		elif(actionCode == 'A2S'):
			if(comm == 1):
				print("With a shockingly easy pivot... like very easily, you dodge out of " + enemyName + "'s attack! ...\n")
			if(comm == 2):
				print("A tuck and a roll is all you needed to escape" + enemyName + "'s harm! ...\n")
			if(comm == 3):
				print("With catlike reflexes, you quickly evade their attack...\n")	#DONE
		elif(actionCode == 'A2F'):
			if(comm == 1):
				print(enemyName + " scoffs: '" + userName " great job stumbling away from me' as you fail your evasion...\n")
			if(comm == 2):
				print("With a poorly timed dodge tactic, you can't succesfully dodge...\n")
			if(comm == 3):
				print("A misplaced twig trips you on your attempt to evade their advances...\n")	#DONE
		elif(actionCode == 'A3S'):
			if(comm == 1):
				print("With an air of beligerance like no other, you see the fear in" + enemyName + "'s eyes as you charge and strike! ...\n")
			if(comm == 2):
				print("Almost as if a barbarian's spirit came upon you, you charge and assail " + enemyName + "...\n")
			if(comm == 3):
				print("Somewhere in between anger and determination, a charge and swing like no other strike true! ...\n")		#DONE
		elif(actionCode == 'A3F'):
			if(comm == 1):
				print(enemyName + "easily escapes your raging charge and attack...\n")
			if(comm == 2):
				print("With a big belly laugh, " + enemyName + " yells at you: Is that actually all you've got, " + userName + "? ...\n")
			if(comm == 3):
				print("With a lunge backwards, " + enemyName + " defty escapes your charging blow...\n")	#DONE
	elif(userCode == "B")	#mage
		if(actionCode == 'B1S'):
			if(comm == 1):
				print("Bright flashes of magical blue streaks pierce " + enemyName + "! ...\n") 
			if(comm == 2):
				print("With a strong jolt, yellow arcane energy outbursts from your wand...\n")
			if(comm == 3):
				print("With a precise recitation, you see " + enemyName + " be struck with a powerful spell...\n")	#DONE	#DONE
		elif(actionCode == 'B1F'):
			if(comm == 1):
				print("A blasted spell misses your enemy!...\n")
			if(comm == 2):
				print("A searing spot remains in the ground from your spell where your enemy lept from! ...\n")
			if(comm == 3):
				print(enemyName + "Can't even hit a spell, " + userName + "? ...\n")		#DONE
		elif(actionCode == 'B2S'):
			if(comm == 1):
				print("You feel arcane healing restore you as you see the cuts on your body mend back together! ...\n")
			if(comm == 2):
				print("Much to the surprise of " + enemyName + " , you are feeling much better from your healing! ...\n")
			if(comm == 3):
				print("The strength re-enters your body as you see a red healing energy spiral though your veins! ...\n")		#DONE
		elif(actionCode == 'B2F'):
			if(comm == 1):
				print("You step aside, seeking to heal yourself, but amidst the stress of the fight, your incantation doesn't work! ...\n")
			if(comm == 2):
				print(enemyName + " has an intimidating presence that caused you to trip up on your healing spell! ...\n")
			if(comm == 3):
				print("As you cast your healing spell, it seems like you've dropped your wand! ...\n")		#DONE
		elif(actionCode == 'B3S'):
			if(comm == 1):
				print("With a harsh tone and unkind heart, you lay a curse upon " + enemyName + "...\n")
			if(comm == 2):
				print("Unlike the rest of your spells, a black smoke emerges from your wand, and you see a weakening within" + enemyName + "...\n")
			if(comm == 3):
				print("With a need for self preservation, you cast a harsh curse of weakening...\n")			#DONE
		elif(actionCode == 'B3F'):
			if(comm == 1):
				print(enemyName + "easily evades the black slow moving smoke of the curse...\n")
			if(comm == 2):
				print("With a jeer, " + enemyName + " yells at you: You can't curse me, " + userName + "...\n")
			if(comm == 3):
				print("A slip up in the harsh words of the curse lead to it the ground, and your enemy evades it! ...\n")	#DONE
	elif(userCode == "C")	#ranger
		if(actionCode == 'B1S'):
			if(comm == 1):
				print("With a quick zip and a sudden shriek, an arrow pierces " + enemyName + "! ...\n") 
			if(comm == 2):
				print("As the bow twangs next to you, you see your arrow has caused a limp in your enemy as they run towards you! ...\n")
			if(comm == 3):
				print("With a precise eye and a steady hand, you catch " + enemyName + " with an arrow to the knee...\n")	#DONE
		elif(actionCode == 'B1F'):
			if(comm == 1):
				print("A quick as lightning arrow misses your enemy!...\n")
			if(comm == 2):
				print(enemyName + "narrowly dodged your arrow and left it there in the ground...\n")
			if(comm == 3):
				print("Shooting on a moving target is quite difficult, you think, as your arrow zips by! ...\n")			
				print("Shooting on a moving target is quite difficult, you think, as your arrow zips by! ...\n")			#DONE
		elif(actionCode == 'B2S'):
			if(comm == 1):
				print("You feel arcane healing restore you as you see the cuts on your body mend back together! ...\n")
			if(comm == 2):
				print("Much to the surprise of " + enemyName + " , you are feeling much better from your healing! ...\n")
			if(comm == 3):
				print("The strength re-enters your body as you see a red healing energy spiral though your veins! ...\n")		#DONE
		elif(actionCode == 'B2F'):
			if(comm == 1):
				print("You step aside, seeking to heal yourself, but amidst the stress of the fight, your incantation doesn't work! ...\n")
			if(comm == 2):
				print(enemyName + " has an intimidating presence that caused you to trip up on your healing spell! ...\n")
			if(comm == 3):
				print("As you cast your healing spell, it seems like you've dropped your wand! ...\n")		#DONE
		elif(actionCode == 'B3S'):
			if(comm == 1):
				print("With a harsh tone and unkind heart, you lay a curse upon " + enemyName + "...\n")
			if(comm == 2):
				print("Unlike the rest of your spells, a black smoke emerges from your wand, and you see a weakening within" + enemyName + "...\n")
			if(comm == 3):
				print("With a need for self preservation, you cast a harsh curse of weakening...\n")			#DONE
		elif(actionCode == 'B3F'):
			if(comm == 1):
				print(enemyName + "easily evades the black slow moving smoke of the curse...\n")
			if(comm == 2):
				print("With a jeer, " + enemyName + " yells at you: You can't curse me, " + userName + "...\n")
			if(comm == 3):
				print("A slip up in the harsh words of the curse lead to it the ground, and your enemy evades it! ...\n")	#DONE















welcome()
charSelect()
#chooses the setting for the game
environment = random.randint(0,5)
environSelect(environment)
userAction()