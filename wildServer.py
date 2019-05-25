from socket import *
import threading
import sys
import random


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

socket1.send("1".encode('utf-8'))
socket2.send("1".encode('utf-8'))