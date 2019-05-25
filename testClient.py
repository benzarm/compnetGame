from socket import *
import sys
import threading

clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
serverPort = 4000
clientSocket.connect(('10.1.10.175', serverPort))
print("Connected to server on port " + str(serverPort) + ". Say hello!")

while(1):
		sendMessage = input()
		clientSocket.send(sendMessage)