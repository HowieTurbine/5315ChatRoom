import socket, select, sys


def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()


# main function
if __name__ == "__main__":

    if len(sys.argv) < 3:
        print('Usage : python Client.py hostname port')
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try:
        s.connect((host, port))
    except:
        print('Unable to connect')
        sys.exit()

    print('Connected to remote host. Start sending messages')
    prompt()

    while 1:
        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        # if not read_sockets or write_sockets or error_sockets:
        #     print("time out")
        #     break

        for sock in read_sockets:
            # incoming message from remote server
            if sock == s:
                data = sock.recv(1024).decode('utf-8')
                if not data:
                    print('\nDisconnected from chat server')
                    sys.exit()
                else:
                    # print data
                    sys.stdout.write(data)
                    prompt()

            # user entered a message
            else:
                msg = sys.stdin.readline()
                Msg = str.encode(msg, encoding='utf-8')
                s.send(Msg)
                prompt()
