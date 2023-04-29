from Sockets.cliente import Client
from PyQt5 import QtWidgets, uic 
import sys

class Cliente(QtWidgets.QMainWindow):
    def __init__(self):
        super(Cliente, self).__init__()
        
        self.client = Cliente()

        uic.loadUi('UI/cliente.ui', self)
        self.show()


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = Cliente()
	sys.exit(app.exec_())