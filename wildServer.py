from socket import *
import threading
import sys
import random

#process the user attack
def processAttack(attackCode, userCode, opponentCode):
	#roll the dice
	diceRoll = random.randint(1,20)
	modifier = 0
	#fighter
	if (userCode == "A"):
		#slash
		if (attackCode == "A1"):
			if (diceRoll >= 5):
				print("slash succeeded")
				damage = 3
				#increased dmg against ranger
				if (opponentCode == "C"):
					damage += 1
				return (damage, modifier)
			else:
				print("missed slash")
				return (damage, modifier)
		#block
		elif (attackCode == "A2"):
			if (diceRoll >= 14):
				print("roll succeeded")
				modifier = 1
				return (damage, modifier)
			else:
				print("roll failed")
				return (damage, modifier)
		#charge
		elif (attCode == "A3"):
			if (diceRoll >= 12):
				print("charge succeeded")
				damage = 5
				#increased dmg against ranger
				if (opponentCode == "C"):
					damage += 1
				return (damage, modifier)
			else:
				print("charge failed")
				return (damage, modifier)
	#mage 
	if (userCode == "B"):
		#attack spell
		if (attackCode == "B1"):
			if (diceRoll >= 4):
				print("attack spell succeeded")
				damage = 4
				#increased dmg against fighter
				if (opponentCode == "A"):
					damage += 1
				return (damage, modifier)
			else:
				print("missed attack spell")
				return (damage, modifier)
		#heal
		elif (attackCode == "B2"):
			if (diceRoll >= 3):
				print("healing succeeded")
				modifier = 2
				return (damage, modifier)
			else:
				print("healing failed")
				return (damage, modifier)
		#curse
		elif (attCode == "B3"):
			if (diceRoll >= 7):
				print("curse succeeded")
				modifier = 3
				return (damage, modifier)
			else:
				print("curse failed")
				return (damage, modifier)

	#ranger 
	if (userCode == "C"):
		#normal arrow
		if (attackCode == "C1"):
			if (diceRoll >= 10):
				print("normal arrow succeeded")
				damage = 7
				#increased dmg against mage
				if (opponentCode == "B"):
					damage += 1
				return (damage, modifier)
			else:
				print("missed normal arrow")
				return (damage, modifier)
		#fire arrow
		elif (attackCode == "C2"):
			if (diceRoll >= 16):
				print("fire arrow succeeded")
				damage = 9
				#increased dmg against mage
				if (opponentCode == "B"):
					damage += 1
				return (damage, modifier)
			else:
				print("fire arrow failed")
				return (damage, modifier)
		#dodge
		elif (attCode == "C3"):
			if (diceRoll >= 12):
				print("dodge succeeded")
				modifier = 1
				return (damage, modifier)
			else:
				print("dodge failed")
				return (damage, modifier)


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

#send over ready to go!
socket1.send("1".encode('utf-8'))
socket2.send("1".encode('utf-8'))

#1 is block/dodge, 2 is heal, 3 is curse
modifier = 0

#receive character codes
userCode1 = str(socket1.recv(1024))
userCode2 = str(socket2.recv(1024))

#receive attack codes
attackCode1 = str(socket1.recv(1024))
attackCode2 = str(socket2.recv(1024))

#process attacks
damage1, modifier1 = processAttack(attackCode1, userCode1, userCode2)
damage2, modifier2 = processAttack(attackCode1, userCode1, userCode2)

print("damage player 1 does: " + damage1)
print("damage player 2 does: " + damage2)
print("player 1's modifier: " + modifier1)
print("player 2's modifier: " + modifier2)





#figure out how much damage each attack does including if they hit
	#keep track of health in client, server sends damage done back to client
	#put in greater loop to repeat attacks


#update health for each player and send health back

#determine if a player is dead or not

#create gui