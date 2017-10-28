from socket import *

serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()
    num = int(connectionSocket.recv(1024).decode())
    if num <0:
        sten = 'Factorial not defined for negative values.'
        connectionSocket.send(sten.encode())
        connectionSocket.close()
    else:
        sum = 1
        for i in range(1, num+1):
            sum=sum*i
        connectionSocket.send(str(sum).encode())
        connectionSocket.close()

