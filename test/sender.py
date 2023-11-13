import socket

def send_message(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))

        client_socket.sendall(message.encode())
        print(f"Sent message to {host}:{port}")

    except Exception as e:
        print(f"An error occured: {e}")

    finally:
        client_socket.close()


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 3099
    MESSAGE = 'Hello from the sender!'

    send_message(HOST, PORT, MESSAGE)