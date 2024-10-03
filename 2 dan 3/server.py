import socket
import threading

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    connected = True
    while connected:
        try:
            data = conn.recv(32).decode('utf-8')
            if not data:
                break
            print(f"Received from {addr}: {data}")
            
            # Proses pengiriman data
            if len(data) < 8:
                response = "Data kurang dari 8 karakter"
            elif len(data) > 8 and len(data) <= 32:
                response = "Data lebih dari 8 karakter"
            else:
                response = "Data diterima"
            
            conn.send(response.encode('utf-8'))
        except:
            break
    print(f"Connection closed from {addr}")
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9900))
    server.listen(1)  # Backlog diubah menjadi 1
    print("Server is listening on localhost:9900")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()