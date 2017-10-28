from socket import *
import threading

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

def client(ip,serverPort):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    while 1:
        sentence = input('Me: ')
        clientSocket.sendto(sentence.encode(), (ip, serverPort))
    # modifiedSentence, serverAddress = clientSocket.recvfrom(2048)
    # print(modifiedSentence.decode())
    clientSocket.close()

threads = []
ip1 = '127.0.0.1'
port = 12000
# serverSocket = socket(AF_INET, SOCK_DGRAM)
t1 = threading.Thread(target=receiver, args=(ip1, port))
t2 = threading.Thread(target=client, args=(ip1, port))

threads.append(t1)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)  # # 将线程声明为守护线程，必须在 start() 方法前调用，不设置会被无限挂起
        t.start()
        # t.join()

    for t in threads:
        t.join()  # 在子线程完成运行之前，这个子线程的父线程将一直被阻塞
    # serverSocket.close()
