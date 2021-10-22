import sys, socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

serversocket.bind((host, port))

serversocket.listen(5)

while True:
    clientsocket, addrs = serversocket.accept()
    print('连接到地址 %s' % str(addrs))
    msg = '欢迎访问菜鸟教程！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
