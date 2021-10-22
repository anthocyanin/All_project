# Single-threaded server that serves one client at a time; others must wait.
import zen_utils


if __name__ == '__main__':
    address = zen_utils.parse_command_line('simple single-threaded server')
    listener = zen_utils.creat_server_socket(address)
    zen_utils.accept_connections_forever(listener)

