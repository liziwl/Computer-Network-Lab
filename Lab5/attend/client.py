from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
num = input('Input a positive number for calculating factorial:')
clientSocket.send(num.encode())
modifiedSentence = clientSocket.recv(1024).decode()
print('From Server:', modifiedSentence)
clientSocket.close()
