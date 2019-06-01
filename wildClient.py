from socket import *
import sys
import threading
import random
import time

def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.02)

'''
SOCKET SETUP-------------------------------------------------------------------
'''
#create socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#take ip and port from command line
serverIP = str(sys.argv[1])
serverPort = int(sys.argv[2])

#connect to server
clientSocket.connect((serverIP, serverPort))

#helpful message :) 
print("Connected to server on port " + str(serverPort) + ". Say hello!")

#welcome message
print_slow("\n ~ Welcome to Trent & Matt's Wild [text] Adventure! ~")
print("\n")
print_slow("Waiting for both players to join...")
print("\n")

'''
INTIALIZING PREGAME/NAME-------------------------------------------------------
'''
#receive ok for starting
clientSocket.recv(1024)
print_slow("You find yourself in a prison, the door opens, and a gruff voice yells at you..")
print("\n")
print_slow("'Whats your name, prisoner?'\n")
userName = input()

#send over username to server
clientSocket.send(userName.encode('utf-8'))

#nice welcoming message
print_slow(("\nOkay, " + userName + ", get out there and fight for your life! Best of luck...\n"))

#initialize health
health = 0

'''
CHARACTER SELECT---------------------------------------------------------------
'''
#receive ok for character select
clientSocket.recv(1024)

print_slow("As you get up, the chains jangle, and you look down at yourself...\n")

#loop so the user can pick their class. if they type in something invalid the loop will start over
while(1):
	global userCode
	userClass = input("Choose your class (type the letter and hit enter):\na. fighter\nb. wizard\nc. ranger\n")

	if(userClass == "A" or userClass == "a" or userClass == "fighter" or userClass == "Fighter"):
		userCode = "A"
		fighterWeapon = "sword"
		fighterDMG = 3 #just adjust the random number generation for it to be easier to hit
		health = 50
		print("You feel your muscles strengthen and your hand clasps around the sword given to you...\n")
		break

	elif(userClass == "B" or userClass == "b" or userClass == "wizard" or userClass == "Wizard"):
		userCode = "B"
		wizWeapon = "wand"
		wizDMG = 5 #slightly harder to hit
		health = 35
		print("Arcane energy rushes through your veins and at the touch of your wand, you come to your magical senses...\n")
		break

	elif(userClass == "C" or userClass == "c" or userClass == "ranger" or userClass == "Ranger"):
		userCode = "C"
		rangerWeapon = "bow & arrow"
		rangerDMG = 7 #hardest to hit
		health = 30
		print("As you test the string of your bow, you feel the energy of the bows thwang reverberate within you...\n")
		break
	else:
		print("Your vision is foggy, and you can't quite see. As you rub your eyes you look down and see...\n")
		
#send over character code to server for processing	
clientSocket.send(userCode.encode('utf-8'))

'''
ENVIRONMENT SELECT-------------------------------------------------------------
'''
environment = random.randint(0,5)

if(environment == 1):
	print_slow("And as the door opens, you are nearly blinded with the sharp reflection of the sun on a sea of sand.")
	print_slow("The heat is draining, but in the distance an armed opponent is walking towards you...\n") 
elif(environment == 2):
	print_slow("And as the door opens, the superficial torch light becomes the brightest beacon in a dull forest.")
	print("As the wind howls and you see red eyes blink in the distance, a figure, with weapon in hand approaches...\n")
else:
	print_slow("And as the door slams open, a deafening roar of shouts and screams and song from a crowd cheer at your potential demise.")
	print_slow("Among the bloodthirsty fans and vendors trying to make a living, bets are tossed around and an armed opponent challenges you...\n")

'''
ATTACK SELECT------------------------------------------------------------------
'''
while(1):
	#receive ok for attack select
	clientSocket.recv(1024)

	#loop for selecting (again will repeat until a valid input is entered)
	while(1):
		print("\n")

		#fighter options
		if(userCode == "A"):
			#prompt
			fighterAction = input("Choose an attack (type the letter and hit enter):\na. Slash\nb. Roll\nc. Charge\n")
			#slash
			if(fighterAction == "A" or fighterAction == "a" or fighterAction == "Slash" or fighterAction == "slash"):
				attackCode = "A1"
				break
			#roll
			elif(fighterAction == "B" or fighterAction == "b" or fighterAction == "Roll" or fighterAction == "roll"):
				attackCode = "A2"
				##NEGATE ALL DAMAGE? PERHAPS JUST DONT CHANGE THEIR HEALTH?
				break
			#charge
			elif(fighterAction == "C" or fighterAction == "c" or fighterAction == "Charge" or fighterAction == "charge"):
				attackCode = "A3"
				#MAKE IT SO THAT THEY TAKE EXTRA DAMAGE
				break

		#wizard options
		elif(userCode == "B"):
			#prompt
			wizAction = input("Choose a spell to cast (type the letter and hit enter):\na. Attack spell\nb. Healing spell\nc. Curse spell\n")
			#attack spell
			if(wizAction == "A" or wizAction == "a" or wizAction == "Attack Spell" or wizAction == "attack spell"):
				attackCode = "B1"
				break
			#healing spell
			elif(wizAction == "B" or wizAction == "b" or wizAction == "Roll" or wizAction == "roll"):
				attackCode = "B2"
				#restore health if past DC 15
				break
			#curse spell
			elif(wizAction == "C" or wizAction == "c" or wizAction == "charge" or wizAction == "charge"):
				attackCode = "B3"
				#DC 10 to hit, but if under 10, takes damage
				break

		#ranger options
		elif(userCode == "C"):
			#prompt
			rangeAction = input("Choose an attack (type the letter and hit enter):\na. Shoot a normal arrow\nb. Dodge\nc. Shoot a fire arrow\n\n")
			#normal
			if(rangeAction == "A" or rangeAction == "a" or rangeAction == "Shoot a normal arrow" or rangeAction == "shoot a normal arrow"):				
				attackCode = "C1"
				break
			#dodge
			elif(rangeAction == "B" or rangeAction == "b" or rangeAction == "Dodge" or rangeAction == "dodge"):
				attackCode = "C2"
				#restore health if past DC 15
				break
			#fire 
			elif(rangeAction == "C" or rangeAction == "c" or rangeAction == "Shoot a fire arrow" or rangeAction == "shoot a fire arrow"):
				attackCode = "C3"
				#DC 10 to hit, but if under 10, takes damage
				break						
		else:
			print("The nerves got to you and you selected an invalid attack, try again...\n")

	#send attack code back to server for processing
	clientSocket.send(attackCode.encode('utf-8'))

	#attack message from server so the user knows if their attack hit the opponent or not
	attackMessage = clientSocket.recv(1024).decode('utf-8')
	print_slow(("\n" + attackMessage + "\n"))

	#receive damage taken and modifier from the server
	damage = int(clientSocket.recv(1024).decode('utf-8'))
	modifier = int(clientSocket.recv(1024).decode('utf-8'))

	#modifier stuff: if modifier is 1, a dodge has succeeded so no damage it 
	#taken. If modifier is 2, healing has succeeded so health should increase
	#by 5. If modifier is 3, curse has succeeded so reduce damage taken by 5
	if (modifier == 1):
		damage = 0
	elif (modifier == 2):
		health += 5
	elif (modifier == 3):
		damage -= 5
		if (damage < 0):
			damage = 0

	#subtract damage from health
	health -= damage

	#receive ok for sending over health
	clientSocket.recv(1024)
	#send over health
	clientSocket.send(str(health).encode('utf-8'))

	#receive message that either says how much health you have or that you have
	#won/lost the game
	healthMessage = clientSocket.recv(1024).decode('utf-8')

	print_slow(("damage taken: " + str(damage) + "\n"))

	print_slow((healthMessage + "\n"))

	#these message signify the end of the game, so we can close the socket
	#and exit the loop once we receive one of these
	if (healthMessage == "You win!" or healthMessage == "You lose!"):
		clientSocket.close()
		break


	#reset modifier
	modifier = 0