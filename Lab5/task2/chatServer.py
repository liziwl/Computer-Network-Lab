import UDPchat
import threading

threads = []
ip1 = '127.0.0.1'

t1 = threading.Thread(target=UDPchat.receiver, args=(ip1, 12020))  # 接收端口
t2 = threading.Thread(target=UDPchat.client, args=("Tom", ip1, 12025))  # 用户名，发送端口

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
