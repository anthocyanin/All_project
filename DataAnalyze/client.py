import argparse
import random
import socket
import zen_utils


def client(address, cause_error=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    aphorisms = list(zen_utils.aphorisms)  # list(字典对象),则返回一个由字典对象所有键组成的列表
    if cause_error:
        sock.sendall(aphorisms[0][:-1])
        return
    for aphorism in random.sample(aphorisms, 3):  # 从list中随机获取3个元素，作为一个片断返回
        sock.sendall(aphorism)
        print(aphorism, zen_utils.recv_until(sock, b'.'))
    sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Exeample client')
    parser.add_argument('host', help='Ip or hostname')
    # parser.add_argument('-e', action='store_true', help='cause an error')
    parser.add_argument('-p', metavar='port', type=int, default=1060, help='TCP port default(1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    # client(address, args.e)
    client(address)




