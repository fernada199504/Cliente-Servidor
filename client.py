import socket
import json

def request_users_from_logic_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))
    client_socket.send("REQUEST_USERS".encode())
    data = client_socket.recv(1024).decode()
    client_socket.close()
    return json.loads(data)

if __name__ == "__main__":
    print("Client is requesting user data...")
    users = request_users_from_logic_server()
    for user_id, user_info in users.items():
        print(f"User ID: {user_id}, Name: {user_info['name']}, Age: {user_info['age']},Telefono: {user_info['telefono']}")