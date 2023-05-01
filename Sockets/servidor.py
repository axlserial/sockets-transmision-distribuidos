import socket
from _thread import *


def get_ip_address():
    """Obtiene la dirección IP de la máquina"""
    # return "192.168.195.179"

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


class Server:
    def __init__(self):
        # Creamos un socket para el servidor
        self.servidor = None
        self.puerto = 2000
        self.clientsCount = 0

    def get_ip(self):
        return f"{get_ip_address()}:{self.puerto}"

    def _multi_threaded_client(self, connection: socket.socket, callback):
        # Espera de mensajes del cliente
        while True:
            # Recibimos el nombre del archivo que solicita el cliente
            try:
                filename = connection.recv(1024).decode("utf-8")
            except:
                break

            # Cliente desconectado
            if not filename:
                break

            # Imprimimos el nombre del archivo solicitado
            print(f"El cliente solicita el archivo: {filename}")

            # Abrimos el archivo solicitado por el cliente
            try:
                with open(f"Files/{filename}", "rb") as file:
                    # Enviamos el archivo al cliente
                    line = file.read(1024)
                    while line:
                        connection.send(line)
                        line = file.read(1024)

                    # Enviamos una bandera de finalización de archivo
                    connection.send(b"<END>")

            # Si el archivo no existe, se envía un mensaje de error al cliente
            except FileNotFoundError:
                connection.send(b"<NOEXIST>")

        # Cerramos la conexión
        self.clientsCount -= 1
        callback(self.clientsCount)
        connection.close()

    def run(self, callback):
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Asignamos una dirección IP y un puerto al socket
        self.servidor.bind((get_ip_address(), self.puerto))

        # Ponemos el socket en modo escucha
        self.servidor.listen(5)

        def run_thread(serverSocket: socket.socket):
            try:
                while True:
                    client, address = serverSocket.accept()
                    print("Conectado a: " + address[0] + ":" + str(address[1]))
                    start_new_thread(self._multi_threaded_client, (client, callback))
                    self.clientsCount += 1
                    callback(self.clientsCount)

            except:
                pass

        start_new_thread(run_thread, (self.servidor,))

    def close(self):
        self.servidor.close()
