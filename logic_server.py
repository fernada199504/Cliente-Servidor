import socket
import json

def get_users_from_data_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5001))
    client_socket.send("GET_USERS".encode())
    data = client_socket.recv(1024).decode()
    client_socket.close()
    return json.loads(data)

def start_logic_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(1)
    print("Logic server is listening on port 5000...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        data = conn.recv(1024).decode()
        if data == "REQUEST_USERS":
            users = get_users_from_data_server()
            response = json.dumps(users)
            conn.send(response.encode())
        conn.close()

if __name__ == "__main__":
    start_logic_server()