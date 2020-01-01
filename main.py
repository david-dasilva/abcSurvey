#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from datetime import datetime
import gui  # import du fichier gui.py généré par pyuic5

from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QMainWindow):
    fw = open("data.csv", "a+")

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.choix1.clicked.connect(lambda: self.onClickBtn("Renseignements"))
        self.ui.choix2.clicked.connect(lambda: self.onClickBtn("Inscriptions"))
        self.ui.choix3.clicked.connect(lambda: self.onClickBtn("Borne internet"))
        self.ui.choix4.clicked.connect(lambda: self.onClickBtn("Boite aux lettres"))

        self.fw.seek(0)
        first_char = self.fw.read(1)
        if not first_char:
            self.fw.write("date,motif\n")
            self.fw.flush()

        self.ui.resultLabel.setText("")

    def onClickBtn(self, motif):
        print(motif)
        now = datetime.now()
        time = now.strftime('%H:%M')

        self.fw.write(f'{now},{motif}\n')
        self.fw.flush()

        self.ui.resultLabel.setText(f'Dernière visite : <strong>{motif}</strong> à <strong>{time}</strong>')

    def __del__(self):
        self.fw.close()

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
