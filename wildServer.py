from socket import *
import threading
import sys
import random
import time

#process the user attack
def processAttack(attackCode, userCode, opponentCode, userNameAttacker, userNameDefender, socket):
	
	#roll the dice
	diceRoll = random.randint(1,20)
	comm = random.randint(1,3)

	#modifier: 1 for block/roll, 2 for heal, 3 for curse
	modifier = 0

	#to keep track of how much health someone has
	damage = 0

	##################################################
	#                    FIGHTER                     #
	##################################################
	if (userCode == "A"):

		###SLASH###
		if (attackCode == "A1"):
			#if slash succeeds
			if (diceRoll >= 5):

				#send one of three preset messages
				if(comm == 1):
					socket.send(("Blood spurts as you slash through their worn armor...\n").encode('utf-8'))
				elif(comm == 2):
					socket.send(("A deft slash cuts across " + userNameDefender + "'s chest...\n").encode('utf-8'))
				elif(comm == 3):
					socket.send(("As the adrenaline pumps through your veins, you slash down on" + userNameDefender + "...\n").encode('utf-8'))

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
			if (diceRoll >= 14):
				#send one of three preset messages
				if(comm == 1):
					socket.send(("With a shockingly easy pivot... like very easily, you dodge out of " + userNameDefender + "'s attack! ...\n").encode('utf-8'))
				elif(comm == 2):
					socket.send(("A tuck and a roll is all you needed to escape" + userNameDefender + "'s harm! ...\n").encode('utf-8'))
				elif(comm == 3):
					socket.send(("With catlike reflexes, you quickly evade their attack...\n").encode('utf-8'))

				#set modifier to dodge
				modifier = 1

				return damage, modifier

			#if block fails
			else:
				#send one of three preset messages
				if(comm == 1):
					socket.send((userNameDefender + " scoffs: '" + userNameAttacker + " great job stumbling away from me' as you fail your evasion...\n").encode('utf-8'))
				if(comm == 2):
					socket.send(("With a poorly timed dodge tactic, you can't succesfully dodge...\n").encode('utf-8'))
				if(comm == 3):
					socket.send(("A misplaced twig trips you on your attempt to evade their advances...\n").encode('utf-8'))

				return damage, modifier

		###CHARGE###
		elif (attackCode == "A3"):
			#if charge succeeds
			if (diceRoll >= 12):

				#send one of three preset messages
				if(comm == 1):
					socket.send(("With an air of beligerance like no other, you see the fear in" + userNameDefender + "'s eyes as you charge and strike! ...\n").encode('utf-8'))
				elif(comm == 2):
					socket.send(("Almost as if a barbarian's spirit came upon you, you charge and assail " + userNameDefender + "...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("Somewhere in between anger and determination, a charge and swing like no other strike true! ...\n").encode('utf-8'))

				#set dmg
				damage = 5

				#increased dmg against ranger
				if (opponentCode == "C"):
					damage += 1

				return damage, modifier

			#if charge fails
			else:
				#send one of three preset messages
				if(comm == 1):
					socket.send((userNameDefender + "easily escapes your raging charge and attack...\n").encode('utf-8'))
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
					socket.send((userNameDefender + "Can't even hit a spell, " + userNameAttacker + "? ...\n").encode('utf-8'))	

				return damage, modifier

		###HEAL###
		elif (attackCode == "B2"):

			#if heal succeeds
			if (diceRoll >= 3):
				#send one of three preset messages
				if(comm == 1):
					socket.send(("You feel arcane healing restore you as you see the cuts on your body mend back together! ...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("Much to the surprise of " + userNameDefender + " , you are feeling much better from your healing! ...\n").encode('utf-8'))	
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
					socket.send(("Unlike the rest of your spells, a black smoke emerges from your wand, and you see a weakening within" + userNameDefender + "...\n").encode('utf-8'))	
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
					socket.send((userNameDefender + "easily evades the black slow moving smoke of the curse...\n").encode('utf-8'))	
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
			if (diceRoll >= 10):
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
					socket.send((userNameDefender + "narrowly dodged your arrow and left it there in the ground...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("Shooting on a moving target is quite difficult, you think, as your arrow zips by! ...\n").encode('utf-8'))

				return damage, modifier

		###DODGE###
		elif (attackCode == "C2"):

			#if dodge succeeds
			if (diceRoll >= 12):
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
			if (diceRoll >= 16):
				#send one of three preset messages
				if(comm == 1):
					socket.send(("With a blazing arrow, you hear the searing strike wound " + userNameDefender + "! ...\n").encode('utf-8'))	
				elif(comm == 2):
					socket.send(("With a smoke trail behind it, a flaming blast greatly harms your enemy...\n").encode('utf-8'))	
				elif(comm == 3):
					socket.send(("With crackles of heat and a zipping sound, you hear" + userNameDefender + "exclaim in pain from your flaming shot...\n").encode('utf-8'))	

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
		
###MAIN###		
serverSocket = socket(AF_INET, SOCK_STREAM) #TCP (reliable)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable
serverIP = str(sys.argv[1])
serverPort = int(sys.argv[2])
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)
print("Game ready to accept players on port " + str(serverPort))

#initial stuff
print("Waiting to accept first player...")
socket1, addr1 = serverSocket.accept()
print("Player 1 joined, waiting to accept second player...")
socket2, addr2 = serverSocket.accept()
print("Player 2 joined, ready to begin!")

###receive everything from client###
###everything is staggered here to remove issues of ordering###

#send over ok
socket1.send("1".encode('utf-8'))
#receive
userName1 = socket1.recv(1024).decode('utf-8')

#send over ok
socket2.send("1".encode('utf-8'))
#receive
userName2 = socket2.recv(1024).decode('utf-8')

#send over ok
socket1.send("1".encode('utf-8'))
#receive
userCode1 = socket1.recv(1024).decode('utf-8')

#send over ok
socket2.send("1".encode('utf-8'))
#receive
userCode2 = socket2.recv(1024).decode('utf-8')

while(1):
	#send over ok
	time.sleep(0.01)
	socket1.send("1".encode('utf-8'))
	#receive
	time.sleep(0.01)
	attackCode1 = socket1.recv(1024).decode('utf-8')

	#send over ok
	time.sleep(0.01)
	socket2.send("1".encode('utf-8'))
	#receive
	time.sleep(0.01)
	attackCode2 = socket2.recv(1024).decode('utf-8')

	#process attacks
	damage1, modifier1 = processAttack(attackCode1, userCode1, userCode2, userName1, userName2, socket1)
	damage2, modifier2 = processAttack(attackCode2, userCode2, userCode1, userName2, userName1, socket2)

	#for testing purposes
	print("damage player 1 does: " + str(damage1))
	print("damage player 2 does: " + str(damage2))
	print("player 1's modifier: " + str(modifier1))
	print("player 2's modifier: " + str(modifier2) + "\n")

	#send over damage and modifiers to server to keep track of health clientside
	time.sleep(0.01)
	socket1.send(str(damage2).encode('utf-8'))
	time.sleep(0.01)
	socket2.send(str(damage1).encode('utf-8'))
	time.sleep(0.01)
	socket1.send(str(modifier1).encode('utf-8'))
	time.sleep(0.01)
	socket2.send(str(modifier2).encode('utf-8'))

	#reset modifier	
	modifier = 0