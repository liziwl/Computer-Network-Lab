from socket import *

def client(ip,serverPort):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    while 1:
        sentence = input('Me: ')
        clientSocket.sendto(sentence.encode(), (ip, serverPort))
    # modifiedSentence, serverAddress = clientSocket.recvfrom(2048)
    # print(modifiedSentence.decode())
    clientSocket.close()

client('127.0.0.1',12000)
