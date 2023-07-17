# Uncomment this to pass the first stage
import socket
from concurrent.futures import ThreadPoolExecutor

def reply(connection):
    pong = "+PONG\r\n"
    utf = "utf-8"

    while True:
        if not connection.recv(1024):
            break
        connection.send(bytes(pong, utf))
    print("Client disconnected")


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    thread_pool_executor = ThreadPoolExecutor(max_workers=3)

    while True:
        connection, address = server_socket.accept()
        thread_pool_executor.submit(reply, connection)
        



if __name__ == "__main__":
    main()
