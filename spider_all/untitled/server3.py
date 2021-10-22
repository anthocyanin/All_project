import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:
    data, addr = s.recvfrom(1024)
    # recvfrom()
    # 方法返回数据和客户端的地址与端口,所以这里addr是一个tuple类型。
    print(type(addr))
    print(addr)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)





