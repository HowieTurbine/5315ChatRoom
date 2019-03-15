import socket
import threading  # 导入多线程模块
import select
import logging
from Server.util.utils import data_parse, get_timestamp, data_encode


# print("Waitting to be connected......")
# HostPort = ('127.0.0.1', 9999)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket实例
# s.bind(HostPort)
# s.listen(1)
# conn, addr = s.accept()
# true = True
# addr = str(addr)
# print('Connecting by : %s ' % addr)


# def Receve(conn):  # 将接收定义成一个函数
#     global true  # 声明全局变量，当接收到的消息为quit时，则触发全局变量 true = False，则会将socket关闭
#     while true:
#         data = conn.recv(1024).decode('utf8')
#         if data == 'quit':
#             true = False
#         print("you have receve: " + data + " from" + addr)  # 当接收的值为'quit'时，退出接收线程，否则，循环接收并打印
#
#
# thrd = threading.Thread(target=Receve, args=(conn,))  # 线程实例化，target为方法，args为方法的参数
# thrd.start()  # 启动线程
# while true:
#     user_input = input('>>>')
#     conn.send(user_input.encode('utf8'))  # 循环发送消息
#     if user_input == 'quit':  # 当发送为‘quit’时，关闭socket
#         true = False
#     # conn.close()
# s.close()
#
#
# Function to broadcast chat messages to all connected clients
def broadcast_data(s, message):
    # Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != s:
            try:
                message = str.encode(message)
                socket.send(message)
            except Exception as e:
                print(e)
                # broken socket connection may be, chat client pressed ctrl+c for example
                print("error1")
                socket.close()
                CONNECTION_LIST.remove(socket)


# function for status code 201 data encapsulation
def data_201(daata_raw):
    usr = data_raw["content"]["name"]
    register_time = get_timestamp()
    logging.info("detail_msg: " + data_raw["msg"]["docs"])

    datadict = {"status": "ok", "content": {"name": usr, "time": register_time},
                "msg": {"code": "200", "docs": ""}}
    data = data_encode(datadict)
    return data


# function for status code 202 data encapsulation
def data_202(data_raw):
    sender = data_raw["content"]["from"]
    receiver = data_raw["content"]["to"]
    msg_time = data_raw["content"]["time"]
    d_msg = data_raw["content"]["content"]
    logging.info("detail_msg: " + data_raw["msg"]["docs"])

    datadict = {"status": "ok",
                "content": {"from": sender, "to": receiver, "time": msg_time, "content": d_msg},
                "msg": {"code": 202, "docs": ""}}
    data = data_encode(datadict)
    return data


if __name__ == '__main__':
    print("Waitting to be connected......")
    CONNECTION_LIST = []
    HostPort = ('127.0.0.1', 9999)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(HostPort)
    server_socket.listen(10)

    CONNECTION_LIST.append(server_socket)
    print("Chat server started on port " + str(HostPort))

    while 1:
        # Get the list sockets which are ready to be read through select
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

        # if not read_sockets or write_sockets or error_sockets:
        #     print("time out")
        #     break

        for s in read_sockets:
            # New connection
            if s == server_socket:
                # Handle the case in which there is a new connection received through server_socket
                conn, addr = server_socket.accept()
                addr = str(addr)
                CONNECTION_LIST.append(conn)
                print("Client %s connected" % addr)

                broadcast_data(conn, "%s entered room" % addr)

                # Some incoming message from a client
            else:
                # Data received from client, process it
                try:
                    # In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data_raw = data_parse(s.recv(1024))

                    status = data_raw["status"]
                    if data_raw and status == "ok":

                        status_code = str(data_raw["msg"]["code"])
                        if status_code == "201":
                            data = data_201(data_raw)

                        elif status_code == "202":
                            data = data_202(data_raw)

                        else:
                            data = ""

                        logging.info(data)
                        broadcast_data(s, data)
                    else:
                        pass

                except Exception as e:
                    logging.error(e)
                    broadcast_data(s, "Client %s is offline" % addr)
                    print("Client %s is offline" % addr)
                    s.close()
                    CONNECTION_LIST.remove(s)
                    continue

    server_socket.close()
