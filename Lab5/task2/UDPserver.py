# Import socket module
from socket import *

def receiver(ip, serverPort):
    # Assign a port number
    # Create a UDP server socket
    # (AF_INET is used for IPv4 protocols)
    # (SOCK_DGRAM) is used for UDP
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    # Bind the socket to server address and server port
    serverSocket.bind((ip, serverPort))
    print(('The server is ready to receive'))
    # Server should be up and running and listening to the incoming connections
    while 1:
        # Receives the request message from the client
        message, clientAddress = serverSocket.recvfrom(2048)
        print('Client: ' + message.decode())

receiver('127.0.0.1', 12000)
