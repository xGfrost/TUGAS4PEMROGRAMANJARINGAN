import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9900))
    
    while True:
        message = input("Enter your message (or 'quit' to exit): ")
        if message.lower() == 'quit':
            break
        
        # Mengirim data dengan batasan 32 karakter
        client.send(message[:32].encode('utf-8'))
        
        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")
    
    client.close()

if __name__ == "__main__":
    start_client()