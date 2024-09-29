import socket
import json

users = {
    1: {"name": "Fernanda", "age": 29,"telefono": "3145925118",},
    2: {"name": "Stiven", "age": 23 ,"telefono":  "3145223893",},
    3: {"name": "Yaneth", "age": 49 ,"telefono": "3123866199",},
    4: {"name": "Jualian", "age": 18 ,"telefono": "3208025598",}
}

def start_data_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5001))
    server_socket.listen(1)
    print("Data server is listening on port 5001...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        data = conn.recv(1024).decode()
        if data == "GET_USERS":
            response = json.dumps(users)
            conn.send(response.encode())
        conn.close()

if __name__ == "__main__":
    start_data_server()