from socket import *
import sys
import threading

clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
serverIP = str(sys.argv[1])
serverPort = int(sys.argv[2])
clientSocket.connect((serverIP, serverPort))
print("Connected to server on port " + str(serverPort) + ". Say hello!")

print("\n ~ Welcome to Trent & Matt's Wild [text] Adventure! ~")
print("Waiting for both players to join...")
ready = int(clientSocket.recv(1024))
if (ready):
	print("You find yourself in a prison, the door opens, and a gruff voice yells at you..")
	userName = input("'Whats your name, prisoner?'\n\n")
	print("\nOkay,", userName, "get out there and fight for your life\nBest of luck *wink*\n...\n")

	