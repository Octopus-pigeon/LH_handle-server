# pip install websocket-server
from websocket_server import WebsocketServer


# 当新的客户端连接时会提示
from utils.csv_util import init_file


def new_client(client, server):
    print("当新的客户端连接时会提示:%s" % client['id'])
    # server.send_message_to_all("Hey all, a new client has joined us")


# 当旧的客户端离开
def client_left(client, server):
    print("客户端%s断开" % client['id'])


# 接收客户端的信息。
def message_received(client, server, message):
    # print("Client(%d) said: %s" % (client['id'], message))
    from ws_server.data_handle import message_handle
    message_handle(message)


if __name__ == '__main__':
    # 初始化文件
    init_file()
    server = WebsocketServer(8131, "0.0.0.0")
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    server.run_forever()
