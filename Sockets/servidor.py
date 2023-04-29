import socket
from _thread import *


def get_ip_address():
    """Obtiene la dirección IP de la máquina"""

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


class Server:
    def __init__(self):
        # Creamos un socket para el servidor
        self.servidor = None
        self.puerto = 2000
        self.ThreadCount = 0

    def get_ip(self):
        return f"{get_ip_address()}:{self.puerto}"

    def _multi_threaded_client(self, connection: socket.socket):
        # Mensaje de conexión
        connection.send(str.encode("Servidor conectado"))

        # Espera de mensajes del cliente
        while True:
            # Recibimos el nombre del archivo que solicita el cliente
            filename = connection.recv(2048).decode("utf-8")

            # Si el cliente no envía un nombre de archivo, se cierra la conexión
            if not filename:
                break

            # Abrimos el archivo solicitado por el cliente
            try:
                with open(f"Files/{filename}", "rb") as file:
                    # Enviamos el archivo al cliente
                    connection.send(file.read())

            # Si el archivo no existe, se envía un mensaje de error al cliente
            except FileNotFoundError:
                connection.send(str.encode("El archivo no existe"))

        # Cerramos la conexión
        connection.close()

    def run(self):
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Asignamos una dirección IP y un puerto al socket
        self.servidor.bind(("localhost", self.puerto))

        # Ponemos el socket en modo escucha
        self.servidor.listen(5)

        def run_thread(serverSocket: socket.socket):
            try:
                while True:
                    client, address = serverSocket.accept()
                    print("Conectado a: " + address[0] + ":" + str(address[1]))
                    start_new_thread(self._multi_threaded_client, (client,))
                    self.ThreadCount += 1
                    print("Número de clientes: " + str(self.ThreadCount))

            except Exception as e:
                pass

        start_new_thread(run_thread, (self.servidor,))

    def close(self):
        self.servidor.close()
