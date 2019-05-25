from socket import *
import threading
import sys
import random

serverSocket = socket(AF_INET, SOCK_STREAM) #TCP (reliable)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable
serverPort = 4000
serverSocket.bind(('10.1.10.175', serverPort))
serverSocket.listen(1)
print("Game ready to accept players on port " + str(serverPort))

while(1):
	conn, addr = serverSocket.accept()
	print("New client connected from address: " + str(addr))
