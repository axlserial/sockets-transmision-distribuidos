from PyQt5 import QtWidgets, uic 
import sys

class Servidor(QtWidgets.QMainWindow):
    def __init__(self):
        super(Servidor, self).__init__()
        uic.loadUi('UI/servidor.ui', self)
        self.iniciarServidor.clicked.connect(self.iniciarServidorClick)
        self.show()

    def iniciarServidorClick(self):
        print('Iniciar servidor')
        self.iniciarServidor.setText('Detener servidor')
        # self.detenerServidor.setEnabled(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Servidor()
    sys.exit(app.exec_())