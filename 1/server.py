import socket
import threading

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    connected = True
    while connected:
        msg = conn.recv(1024).decode('utf-8')
        if msg == "quit":
            connected = False
        else:
            print(f"Message from client: {msg}")
            conn.send("Message received".encode('utf-8'))
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9900))
    server.listen()
    print("Server is listening on 127.0.0.1:9900")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()