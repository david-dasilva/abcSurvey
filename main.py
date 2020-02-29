#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from datetime import datetime
import gui  # import du fichier gui.py généré par pyuic5
from consts import Consts
from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QMainWindow):
    fw = open("data.csv", "a+")

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)


        # Remplissage des labels
        self.ui.choix1.setText(Consts.MOTIF_CHOIX1)
        self.ui.choix2.setText(Consts.MOTIF_CHOIX2)
        self.ui.choix3.setText(Consts.MOTIF_CHOIX3)
        self.ui.choix4.setText(Consts.MOTIF_CHOIX4)
        self.ui.choix5.setText(Consts.MOTIF_CHOIX5)
        self.ui.choix6.setText(Consts.MOTIF_CHOIX6)

        self.ui.choix1.clicked.connect(lambda: self.onClickBtn(Consts.MOTIF_CHOIX1))
        self.ui.choix2.clicked.connect(lambda: self.onClickBtn(Consts.MOTIF_CHOIX2))
        self.ui.choix3.clicked.connect(lambda: self.onClickBtn(Consts.MOTIF_CHOIX3))
        self.ui.choix4.clicked.connect(lambda: self.onClickBtn(Consts.MOTIF_CHOIX4))
        self.ui.choix5.clicked.connect(lambda: self.onClickBtn(Consts.MOTIF_CHOIX5))
        self.ui.choix6.clicked.connect(lambda: self.onClickBtn(Consts.MOTIF_CHOIX6))

        self.fw.seek(0)
        first_char = self.fw.read(1)
        if not first_char:
            self.fw.write(Consts.CSV_HEADERS)
            self.fw.flush()

        self.ui.resultLabel.setText("")

    def onClickBtn(self, motif):
        now = datetime.now()
        humanTime = now.strftime('%H:%M')
        jourSemaine = now.strftime('%A')
        plageHoraire = self.getPlageHoraire(now)

        self.writeLine(now, jourSemaine, plageHoraire, motif)
        self.changeLastVisit(motif, humanTime)

    def writeLine(self, time, jourSemaine, plageHoraire, motif):
        self.fw.write(f'{time},{jourSemaine},{plageHoraire},{motif}\n')
        self.fw.flush()

    def changeLastVisit(self, motif, time):
        self.ui.resultLabel.setText(f'Dernière visite : <strong>{motif}</strong> à <strong>{time}</strong>')

    def getPlageHoraire(self, now):
        time = now.time()
        if Consts.PLAGE_1_START <= time < Consts.PLAGE_1_END:
            return Consts.PLAGE_1_LABEL
        elif Consts.PLAGE_2_START <= time < Consts.PLAGE_2_END:
            return Consts.PLAGE_2_LABEL
        elif Consts.PLAGE_3_START <= time < Consts.PLAGE_3_END:
            return Consts.PLAGE_3_LABEL
        elif Consts.PLAGE_4_START <= time < Consts.PLAGE_4_END:
            return Consts.PLAGE_4_LABEL
        elif Consts.PLAGE_5_START <= time < Consts.PLAGE_5_END:
            return Consts.PLAGE_5_LABEL
        elif Consts.PLAGE_6_START <= time < Consts.PLAGE_6_END:
            return Consts.PLAGE_6_LABEL
        else: return Consts.PLAGE_AFTER_LABEL


    def __del__(self):
        self.fw.close()

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
