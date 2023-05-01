import socket


class Client:
    def __init__(self) -> None:
        self.client_socket = None
    
    def connect(self, ip, port: int):
        # Creamos un socket para el cliente
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectamos el socket a la dirección IP y el puerto del servidor
        self.client_socket.connect((ip, port))
    
    def receiveMessage(self):
        return self.client_socket.recv(1024).decode()
    
    def receive(self):
        return self.client_socket.recv(1024)
    
    def receiveFile(self, filename: str):
        # Recibimos el archivo del servidor
        data = self.client_socket.recv(1024)

        # Salidos si el archivo no existe
        if data == b"<NOEXIST>":
            return False

        with open(filename, "wb") as file:
            while data:
                if data.endswith(b"<END>"):
                    file.write(data[:-5])
                    break
                else:
                    file.write(data)
                    data = self.client_socket.recv(1024)

        return True
    
    def sendMessage(self, message: str):
        self.client_socket.send(message.encode())
    
    def close(self):
        self.client_socket.close()
