# Uncomment this to pass the first stage
import socket


def main():
    print("Logs from your program will appear here!")

    pong = "+PONG\r\n"
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, address = server_socket.accept()

    with server_socket:
        with connection:
            while True: 
                data = connection.recv(1024)
                if not data: 
                    break
                connection.send(pong.encode())


if __name__ == "__main__":
    main()
