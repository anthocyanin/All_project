import zen_utils
from threading import Thread
# Using multiple threads to serve several clients in parallel.


def start_threads(listener, workers=4):
    t = (listener,)
    for i in range(workers):
        Thread(target=zen_utils.accept_connections_forever, args=t).start()


if __name__ == '__main__':
    address = zen_utils.parse_command_line('multi-threaded server')
    listener = zen_utils.creat_server_socket(address)
    start_threads(listener)

