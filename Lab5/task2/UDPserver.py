# Import socket module
from socket import *
import re


def receiver(ip, serverPort):
    # Assign a port number
    # Create a UDP server socket
    # (AF_INET is used for IPv4 protocols)
    # (SOCK_DGRAM) is used for UDP
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    # Bind the socket to server address and server port
    serverSocket.bind((ip, serverPort))
    print(('Server is ready to receive.'))
    # Server should be up and running and listening to the incoming connections
    while 1:
        # Receives the request message from the client
        message, clientAddress = serverSocket.recvfrom(2048)
        temp = parser(message.decode()).decode()
        print("{}: {}".format(temp[0], temp[1]))
        # sentence = input('Me: ')
        # serverSocket.sendto(sentence.encode(), (ip, serverPort))


# receiver('127.0.0.1', 12021)

class parser:
    def __init__(self, codes):
        self.codes = codes

    def decode(self):
        pattern = "^<identifier=\"(.*?)\"><content=\"(.*?)\">$"
        # print(re.findall(pattern,self.codes))
        return re.findall(pattern, self.codes)[0]
