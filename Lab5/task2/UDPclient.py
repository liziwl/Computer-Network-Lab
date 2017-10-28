from socket import *


def client(id, ip, serverPort):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    print("Client is started.")
    while 1:
        sentence = input()
        # out = "<identifier=\"{}\"><content=\"{}\">".format(id,sentence)
        clientSocket.sendto(message(id, sentence).encode(), (ip, serverPort))
        # server_message, serverAddress = clientSocket.recvfrom(2048)
        # print('Server: '+server_message.decode())
    clientSocket.close()


# client('127.0.0.1',12021)

class message:
    def __init__(self, identifier, content):
        self.identifier = str(identifier)
        self.content = str(content)

    def __str__(self):
        return "<identifier=\"{}\"><content=\"{}\">".format(self.identifier, self.content)

    def __repr__(self):
        return str(self)

    def encode(self):
        # print(self)
        return str(self).encode()
