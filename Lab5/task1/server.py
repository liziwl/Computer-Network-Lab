from socket import *
import os


def send404(connectionSocket):
    head = ''
    head += 'http/1.1 404 Not Found\n'
    head += 'Content-Type: text/html; charset=utf-8\n'
    head += 'Connection: Keep-Alive\n'
    connectionSocket.send(head.encode())

    f = open('404.html', 'r', encoding='UTF-8')
    outputdata = f.read()
    print(outputdata)
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode('utf-8'))
    # connectionSocket.send('\n'.encode('utf-8'))

def sendFile(filename, connectionSocket):
    head = ''
    head += 'HTTP/1.1 200 OK\n'
    head += 'Content-Type: text/plain; charset=utf-8\n'
    head += 'Connection: Keep-Alive\n'
    connectionSocket.send(head.encode())

    f = open(filename, 'r', encoding='UTF-8')
    outputdata = f.read()
    print(outputdata)

    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
    # connectionSocket.send('\n'.encode('utf-8'))


def main():
    # Prepare a sever socket This is on page 167
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('127.0.0.1', 12380))
    serverSocket.listen(1)  # listen for 1 connection

    while True:

        # Establish the connection
        print('Ready to serve…')
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024).decode()
        print(message)

        form = message.split()
        print(form)
        if len(form) != 0 and form[0] == 'GET':
            filename = form[1][1:]

            if os.path.exists(filename):
                print('Send the File.')
                sendFile(filename, connectionSocket)
                connectionSocket.close()

            else:  # if IOError
                print('IOERROR. Cannot find the file.')
                send404(connectionSocket)
                connectionSocket.close()

    serverSocket.close()


if __name__ == '__main__':
    main()
