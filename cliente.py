from Sockets.cliente import Client
from PyQt5 import QtWidgets, uic
from Dialog import Dialog
import sys

class Cliente(QtWidgets.QMainWindow):
    def __init__(self):
        super(Cliente, self).__init__()
        
        self.client = Client()

        # Cargar la interfaz de usuario
        uic.loadUi('UI/cliente.ui', self)

        # Bind de los botones
        self.button_ip.clicked.connect(self.iniciar_con)
        self.solicitar_btn.clicked.connect(self.solicitar_archivo)
        
        self.show()

    def iniciar_con(self):
        # IP del servidor
        ip = self.input_ip.text()
        
        # Campo vacio
        if ip == "":
            Dialog("Ingrese una dirección IP", self).exec_()
            return

        # obtenemos la ip y el puerto
        ip, port = ip.split(":")

        # Conectamos con el servidor
        try:
            self.client.connect(ip, int(port))
        except:
            Dialog("No se pudo conectar con el servidor", self).exec_()
            return

    def solicitar_archivo(self):
        pass


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = Cliente()
	sys.exit(app.exec_())