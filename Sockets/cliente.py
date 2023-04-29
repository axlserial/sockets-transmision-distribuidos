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
        return self.client_socket.recv(102400).decode()
    
    def receive(self):
        return self.client_socket.recv(102400)
    
    def receiveFile(self, filename: str):
        # Recibimos el mensaje del servidor
        message = self.receive()

        # Verificamos si el archivo existe
        if message.decode() == "El archivo no existe":
            print(message.decode())
            self.client_socket.close()
            return False

        # Recibimos el archivo del servidor
        with open(filename, "wb") as file:
            file.write(message)
        
        return True
    
    def sendMessage(self, message: str):
        self.client_socket.send(message.encode())
    
    def close(self):
        self.client_socket.close()
