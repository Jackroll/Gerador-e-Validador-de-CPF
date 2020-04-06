import sys
from Gera_Valida_CPF.validador_cpf import valida_cpf
from Gera_Valida_CPF.gerador_cpf import gera_cpf

from Gera_Valida_CPF.design_cpf import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import *

#print(gera_cpf())
#print(valida_cpf('061.119.009-51'))

class Cpf (QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnGeraCPF.clicked.connect(self.gera_cpf)
        self.btnValidaCPF.clicked.connect(self.valida_cpf)
        self.setWindowIcon(QIcon('icone.png'))

    def gera_cpf(self):
        self.inputGeraCPF.setText(gera_cpf())

    def valida_cpf(self):
        cpf = valida_cpf(self.inputValidaCPF.text())
        if cpf:
            self.labelRetorno.setText('Válido')
            self.inputValidaCPF.setStyleSheet(
                'color: green ; background-color: #d4ffd6'
            )
            self.labelRetorno.setStyleSheet(
                'color: green; font-weight: bold'
            )
        else:
            self.labelRetorno.setText('Inválido')
            self.inputValidaCPF.setStyleSheet(
                'color: red; background-color: #ffc9c9;'
            )
            self.labelRetorno.setStyleSheet(
                'color: red; font-weight: bold'
            )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Cpf()
    app.show()
    qt.exec_()