# Import socket module
from socket import *
import re


def receiver(ip, serverPort):
    """
    :param ip: to serverIP where is sent.
    :param serverPort: Server Post
    :return: none
    """
    # Create a UDP server socket (AF_INET is used for IPv4 protocols) (SOCK_DGRAM) is used for UDP
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind((ip, serverPort))  # 绑定端口
    print(('Server is ready to receive.'))
    while 1:
        # Receives the request message from the client
        data, clientAddress = serverSocket.recvfrom(2048)
        temp = Parser(data.decode()).decode()  # 用自定义parser类打包数据
        print("{}: {}".format(temp[0], temp[1]))
        # sentence = input('Me: ')
        # serverSocket.sendto(sentence.encode(), (ip, serverPort))


def client(id, ip, serverPort):
    """
    :param id: identifier as user name.
    :param ip: to serverIP where is sent.
    :param serverPort: Server Post
    :return: none
    """
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    print("Client is started.")
    while 1:
        sentence = input()
        clientSocket.sendto(Message(id, sentence).encode(), (ip, serverPort))  # 用自定义message类打包数据
        # server_message, serverAddress = clientSocket.recvfrom(2048)
        # print('Server: '+server_message.decode())
    clientSocket.close()


class Message:
    """
    message formatter
    """
    def __init__(self, identifier, content):
        self.identifier = str(identifier)
        self.content = str(content)

    def __str__(self):  # 格式化数据便于传输
        return "<identifier=\"{}\"><content=\"{}\">".format(self.identifier, self.content)

    def __repr__(self):
        return str(self)

    def encode(self):
        # print(self)
        return str(self).encode()


class Parser:
    """
        message decoder and parser
    """
    def __init__(self, codes):
        self.codes = codes

    def decode(self):
        # 正则获取数据
        pattern = "^<identifier=\"(.*?)\"><content=\"(.*?)\">$"
        # print(re.findall(pattern,self.codes))
        return re.findall(pattern, self.codes)[0]
