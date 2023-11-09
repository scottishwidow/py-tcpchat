import socket
import threading

def handle_client(client_socket):
    try:
        with client_socket as sock:
            request = sock.recv(1024)
            print(f"Received: {request.decode('utf-8')}")
    except Exception as e:
        print(f"An error occurred: {e}")

def server_loop():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 3099))
    server.listen(5)
    print("Listening on 127.0.0.1:3099")

    try:
        while True:
            client, addr = server.accept()
            print(f"Accepted connection from: {addr[0]}:{addr[1]}")
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server.close()

if __name__ == "__main__":
    server_loop()
