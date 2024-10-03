import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9900))
    
    while True:
        message = input("Enter your message (or 'quit' to exit): ")
        client.send(message.encode('utf-8'))
        
        if message == "quit":
            break
        
        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")
    
    client.close()

if __name__ == "__main__":
    start_client()