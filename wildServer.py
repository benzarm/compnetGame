#Matt and Trent's WILD [text] Fighter
#Computer Networks w/ Dr. Dingler 
#Server
from socket import *
import threading
import sys
import random
import time

'''
PROCESS USER ATTACK

PARAMETERS: This function takes in the attack code of the attack, the userCode
which tells us the class of the person  attacking, the opponent code which is
the class of the user defending, the username of both for messages, and finally
the socket of the person attacking so they know if their attack hits.

RETURNS: Returns the damage done and modifier of the attack. First, the "dice" 
is rolled to determine if the attack hits. Then, the the usercode and 
attackcode are used to get the right attack. Additions are added since certain
classes have advantages over other classes. Finally, a modifier is associated 
with some special attacks which are also returned so we can process them client 
side later.
'''
def processAttack(attackCode, userCode, opponentCode, userNameAttacker, userNameDefender, socket):

	#roll the dice so later we can determine if an attack hits
	diceRoll = random.randint(1,20)

	#random number between 1 and 3 for randomizing attack messages (more variety)
	comm = random.randint(1,3)

	#modifier: 0 by default, 1 for block/roll, 2 for heal, and 3 for curse
	modifier = 0

	#damage the attack does to be sent to the client later for health calculation
	damage = 0

	##################################################
	#                    FIGHTER                     #
	##################################################
	if (userCode == "A"):

		###SLASH###
		if (attackCode == "A1"):
			#if slash succeeds
			if (diceRoll >= 6):

				#send one of three preset messages
				if(comm == 1):
					socket.send(("Blood spurts as you slash through their worn armor...\n").encode('utf-8'))
				elif(comm == 2):
					socket.send(("A deft slash cuts across " + userNameDefender + "'s chest...\n").encode('utf-8'))
				elif(comm == 3):
					socket.send(("As the adrenaline pumps through your veins, you slash down on " + userNameDefender + "...\n").encode('utf-8'))

				#set dmg
				damage = 3

				#increased dmg against ranger
				if (opponentCode == "C"):
					damage += 1

				return damage, modifier

			#if slash fails
			else:

				#send one of three preset messages
				if(comm == 1):
					socket.send(("With a whistle of your blade in the wind, you miss " + userNameDefender + "...\n").encode('utf-8'))
				elif(comm == 2):
					socket.send(("With a grin and a chuckle " + userNameDefender + " yells at you: Is that all you got, " + userNameAttacker + "? ...\n").encode('utf-8'))
				elif(comm == 3):
					socket.send(("A swing, and... a miss! Sorry, " + userNameAttacker + "...\n").encode('utf-8'))

				return damage, modifier

		###BLOCK###
		elif (attackCode == "A2"):

			#if block succeeds
			if (diceRoll >= 9):

				#send one of three preset messages
				if(comm == 1):
					socket.send(("You plant your feet firmly and hold up your shield, blocking all incoming attacks from " + userNameDefender + "...\n").encode('utf-8'))
				elif(comm == 2):
					socket.send(("A quick block is all you needed to escape " + userNameDefender + "'s harm! ...\n").encode('utf-8'))
				elif(comm == 3):
					socket.send(("With catlike reflexes, you quickly at the last second whip out your shield for a clutch block...\n").encode('utf-8'))

				#set modifier to dodge for later processing
				modifier = 1

				return damage, modifier

			#if block fails
			else:

				#send one of three preset messages
				if(comm == 1):
					socket.send((userNameDefender + " scoffs: '" + userNameAttacker + ", great job trying to block my attack, lo$er...\n").encode('utf-8'))
				elif(comm == 2):
					socket.send(("With a poorly timed block, you can't succesfully defend yourself...\n").encode('utf-8'))
				elif(comm == 3):
					socket.send(("A misplaced twig trips you and you fail to bring up your shield in time...\n").encode('utf-8'))

				return damage, modifier

		###CHARGE###
		elif (attackCode == "A3"):
			#if charge succeeds
			if (diceRoll >= 13):

				#send one of three preset messages
				if(comm == 1):
					socket.send(("With an air of beligerance like no other, you see the fear in " + userNameDefender + "'s eyes as you charge and strike! ...\n").encode('utf-8'))
				elif(comm == 2):
					socket.send(("Almost as if a barbarian's spirit came upon you, you charge and assail " + userNameDefender + "...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("Somewhere in between anger and determination, a charge and swing like no other strike true! ...\n").encode('utf-8'))

				#set dmg
				damage = 6

				#increased dmg against ranger
				if (opponentCode == "C"):
					damage += 1

				return damage, modifier

			#if charge fails
			else:

				#send one of three preset messages
				if(comm == 1):
					socket.send((userNameDefender + " easily escapes your raging charge and attack...\n").encode('utf-8'))
				elif(comm == 2):
					socket.send(("With a big belly laugh, " + userNameDefender + " yells at you: Is that actually all you've got, " + userNameAttacker + "? ...\n").encode('utf-8'))
				elif(comm == 3):
					socket.send(("With a lunge backwards, " + userNameDefender + " defty escapes your charging blow...\n").encode('utf-8'))

				return damage, modifier

	##################################################
	#                      MAGE                      #
	##################################################
	if (userCode == "B"):

		###ATTACK SPELL###
		if (attackCode == "B1"):

			#if attack spell succeeds
			if (diceRoll >= 4):

				#send one of three preset messages
				if(comm == 1):
					socket.send(("Bright flashes of magical blue streaks pierce " + userNameDefender + "! ...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("With a strong jolt, yellow arcane energy outbursts from your wand...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("With a precise recitation, you see " + userNameDefender + " be struck with a powerful spell...\n").encode('utf-8'))	

				damage = 4

				#increased dmg against fighter
				if (opponentCode == "A"):
					damage += 1

				return damage, modifier

			#if attack spells fails
			else:

				#send one of three preset messages
				if(comm == 1):
					socket.send(("A blasted spell misses your enemy!...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("A searing spot remains in the ground from your spell where your enemy lept from! ...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send((userNameDefender + ": 'Can't even hit a spell, " + userNameAttacker + "?' ...\n").encode('utf-8'))	

				return damage, modifier

		###HEAL###
		elif (attackCode == "B2"):

			#if heal succeeds
			if (diceRoll >= 6):

				#send one of three preset messages
				if(comm == 1):
					socket.send(("You feel arcane healing restore you as you see the cuts on your body mend back together! ...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("Much to the surprise of " + userNameDefender + ", you are feeling much better from your healing! ...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("The strength re-enters your body as you see a red healing energy spiral though your veins! ...\n").encode('utf-8'))	
				modifier = 2
				return damage, modifier

			#if heal fails
			else:

				#send one of three preset messages
				if(comm == 1):
					socket.send(("You step aside, seeking to heal yourself, but amidst the stress of the fight, your incantation doesn't work! ...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send((userNameDefender + " has an intimidating presence that caused you to trip up on your healing spell! ...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("As you cast your healing spell, it seems like you've dropped your wand! ...\n").encode('utf-8'))	
				return damage, modifier

		###CURSE###
		elif (attackCode == "B3"):

			#if curse succeeds
			if (diceRoll >= 7):

				#send one of three preset messages
				if(comm == 1):
					socket.send(("With a harsh tone and unkind heart, you lay a curse upon " + userNameDefender + "...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("Unlike the rest of your spells, a black smoke emerges from your wand, and you see a weakening within " + userNameDefender + "...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("With a need for self preservation, you cast a harsh curse of weakening...\n").encode('utf-8'))	

				#curse does dmg
				damage = 2

				#set modifier for curse
				modifier = 3

				return damage, modifier

			#if curse fails
			else:

				#send one of three preset messages
				if(comm == 1):
					socket.send((userNameDefender + " easily evades the black slow moving smoke of the curse...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("With a jeer, " + userNameDefender + " yells at you: You can't curse me, " + userNameAttacker + "...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("A slip up in the harsh words of the curse lead to it the ground, and your enemy evades it! ...\n").encode('utf-8'))

				return damage, modifier

	##################################################
	#                     RANGER                     #
	##################################################
	if (userCode == "C"):

		###NORMAL ARROW###
		if (attackCode == "C1"):

			#if normal arrow succeeds
			if (diceRoll >= 9):

				#send one of three preset messages
				if(comm == 1):
					socket.send(("With a quick zip and a sudden shriek, an arrow pierces " + userNameDefender + "! ...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("As the bow twangs next to you, you see your arrow has caused a limp in your enemy as they run towards you! ...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("With a precise eye and a steady hand, you catch " + userNameDefender + " with an arrow to the knee...\n").encode('utf-8'))

				#set dmg
				damage = 7

				#increased dmg against mage
				if (opponentCode == "B"):
					damage += 1

				return damage, modifier

			#if normal arrow fails
			else:

				#send one of three preset messages
				if(comm == 1):
					socket.send(("A quick as lightning arrow misses your enemy!...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send((userNameDefender + " narrowly dodged your arrow and left it there in the ground...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("Shooting on a moving target is quite difficult, you think, as your arrow zips by! ...\n").encode('utf-8'))

				return damage, modifier

		###DODGE###
		elif (attackCode == "C2"):

			#if dodge succeeds
			if (diceRoll >= 7):

				#send one of three preset messages
				if(comm == 1):
					socket.send(("With a deft tuck and roll, you quickly dodge your enemy's advance...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("With an agile roll, you dodge " + userNameDefender + "'s advance! ...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("Adrenaline and energy pump through your veins as you jump to the side to dodge the enemy's attack...\n").encode('utf-8'))	

				#set modifier to dodge
				modifier = 1

				return damage, modifier

			#if dodge fails
			else:

				#send one of three preset messages
				if(comm == 1):
					socket.send(("After an attempt to escape the attack, " + userNameDefender + " caught your intentions and prevented you from dodging...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("With a grin, " + userNameDefender + " spits at you and yells: you can't run away, " + userNameAttacker + "! ...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("With a failed dodge, you take the consequences of your mistake...\n").encode('utf-8'))	

				return damage, modifier

		###FIRE ARROW###
		elif (attackCode == "C3"):

			#if fire arrow succeeds
			if (diceRoll >= 13):

				#send one of three preset messages
				if(comm == 1):
					socket.send(("With a blazing arrow, you hear the searing strike wound " + userNameDefender + "! ...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("With a smoke trail behind it, a flaming blast greatly harms your enemy...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("With crackles of heat and a zipping sound, you hear " + userNameDefender + " exclaim in pain from your flaming shot...\n").encode('utf-8'))	

				#set dmg
				damage = 9

				#increased dmg against mage
				if (opponentCode == "B"):
					damage += 1

				return damage, modifier

			#if fire arrow fails
			else:

				#send one of three preset messages
				if(comm == 1):
					socket.send(("As the flaming arrow zips by, " + userNameDefender + " evades your shot...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("With a hiss, the ground where the arrow hit sizzles as you miss your shot...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("With the weighty head of the arrow, the flaming arrow flails and you miss your target...\n").encode('utf-8'))

				return damage, modifier

'''
SOCKET SETUP-------------------------------------------------------------------
'''
#set up a tcp socket
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 

#take IP and port from command line arguments (first is ip, second is port)
serverIP = str(sys.argv[1])
serverPort = int(sys.argv[2])

#bind user entered ip and port to the socket
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)

'''
PREGAME SETUP/STARTUP MESSAGES-------------------------------------------------
'''
print("Game ready to accept players on port " + str(serverPort))

#starts at 0, goes to 1 when game is over
gameOver = 0

#print some helpful messages server side so we know when players have connected
print("Waiting to accept first player...")
socket1, addr1 = serverSocket.accept()
print("Player 1 joined, waiting to accept second player...")
socket2, addr2 = serverSocket.accept()
print("Player 2 joined, ready to begin!")

'''
NAMES/CLASSES SETUP------------------------------------------------------------
'''
#NOTE: through the rest of the program, we send a simple "1" message from
#the server so that the client knows when it can continue going through the 
#rest of the program. The client waits at a .recv until it gets the 1. This 
#allows us to control the order of everything. Everything following is 
#staggered in such a way that only one player is sending a message at once.

#send over ok
socket1.send("1".encode('utf-8'))
#receive username from player 1
userName1 = socket1.recv(1024).decode('utf-8')

#send over ok
socket2.send("1".encode('utf-8'))
#receive username from player 2
userName2 = socket2.recv(1024).decode('utf-8')

#send over ok
socket1.send("1".encode('utf-8'))
#receive class code from player 1
userCode1 = socket1.recv(1024).decode('utf-8')

#send over ok
socket2.send("1".encode('utf-8'))
#receive class code from player 2
userCode2 = socket2.recv(1024).decode('utf-8')

'''
ATTACK LOOP--------------------------------------------------------------------
'''
while(1):
	#NOTE: time.sleep statements are used to fix a strange problem we were 
	#having with the program getting stuck. Otherwise the same staggering 
	#from previously is used

	#send over ok
	time.sleep(0.01)
	socket1.send("1".encode('utf-8'))
	#receive attack code from player 1
	time.sleep(0.01)
	attackCode1 = socket1.recv(1024).decode('utf-8')

	#send over ok
	time.sleep(0.01)
	socket2.send("1".encode('utf-8'))
	#receive attack code from player 2
	time.sleep(0.01)
	attackCode2 = socket2.recv(1024).decode('utf-8')

	#process attacks from both users!
	damage1, modifier1 = processAttack(attackCode1, userCode1, userCode2, userName1, userName2, socket1)
	damage2, modifier2 = processAttack(attackCode2, userCode2, userCode1, userName2, userName1, socket2)

	#display all the values for damage and modifiers server side just for information purposes
	print("damage player 1 does: " + str(damage1))
	print("damage player 2 does: " + str(damage2))
	print("player 1's modifier: " + str(modifier1))
	print("player 2's modifier: " + str(modifier2) + "\n")

	#send over damage and modifiers to server to keep track of health clientside
	time.sleep(2)
	socket1.send(str(damage2).encode('utf-8'))
	time.sleep(0.01)
	socket2.send(str(damage1).encode('utf-8'))
	time.sleep(2)
	socket1.send(str(modifier1).encode('utf-8'))
	time.sleep(0.01)
	socket2.send(str(modifier2).encode('utf-8'))

	#get healths from clients so we can determine if the game is over

	#send over ok
	time.sleep(0.01)
	socket1.send("1".encode('utf-8'))
	#receive health from player 1
	time.sleep(0.01)
	health1 = socket1.recv(1024).decode('utf-8')

	#send over ok 
	time.sleep(0.01)
	socket2.send("1".encode('utf-8'))
	#receive health from player 2
	time.sleep(0.01)
	health2 = socket2.recv(1024).decode('utf-8')

	#display healths server side again for information purposes
	print("Player 1's health: " + str(health1))
	print("Player 2's health: " + str(health2))

	#big ol' if statement to determine if someone won, if there was a tie,
	#or if nothing happens and we just continue. Within each we set a message
	#to send back to the clients. Finally, if the game is over, we set our
	#game over variable to 1 so that later we can close all the sockets.
	if (int(health1) <= 0 and int(health2) <= 0):
		gameOver = 1
		healthMessage1 = "Game over, it's a draw!"
		healthMessage2 = "Game over, It's a draw!"
	elif (int(health1) <= 0 and int(health2) > 0):
		gameOver = 1
		healthMessage1 = "You lose!"
		healthMessage2 = "You win!"
	elif (int(health1) > 0 and int(health2) <= 0):
		gameOver = 1
		healthMessage1 = "You win!"
		healthMessage2 = "You lose!"
	else:
		healthMessage1 = "Your current health is " + health1 + " and your opponent's health is " + health2
		healthMessage2 = "Your current health is " + health2 + " and your opponent's health is " + health1

	#send over the old health messages
	socket1.send(healthMessage1.encode('utf-8'))
	socket2.send(healthMessage2.encode('utf-8'))

	#if game over variable is 1, that means one player has won, so we can
	#close the sockets and exit the loop, ending the program
	if(gameOver == 1):
		print("game over, shutting down...")
		socket1.close()
		socket2.close()
		break

	#reset modifier	
	modifier = 0