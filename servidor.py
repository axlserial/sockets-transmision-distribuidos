from Sockets.servidor import Server
from PyQt5 import QtWidgets, uic
import sys


class Servidor(QtWidgets.QMainWindow):
    def __init__(self):
        super(Servidor, self).__init__()

        self.server = Server()
        self.isRunning = False

        uic.loadUi("UI/servidor.ui", self)
        self.toggleServidor.clicked.connect(self.toggleServidorClick)
        self.show()

    def toggleServidorClick(self):
        if self.isRunning:
            self.server.close()
            self.isRunning = False
            self.ipServidor.setText("Servidor detenido")
            self.toggleServidor.setText("Iniciar servidor")

        else:
            self.clientsCountLabel.setText("Clientes Conectados: 0")
            self.toggleServidor.setText("Detener servidor")
            self.ipServidor.setText(f"IP: {self.server.get_ip()}")
            self.isRunning = True
            self.server.run(
                lambda n: self.clientsCountLabel.setText(f"Clientes Conectados: {n}")
            )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Servidor()
    sys.exit(app.exec_())
