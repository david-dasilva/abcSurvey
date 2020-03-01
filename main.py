#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import gui  # import du fichier gui.py généré par pyuic5
from consts import Consts
from PyQt5 import QtWidgets
import sqlite3


class MyWindow(QtWidgets.QMainWindow):
    fw = open("data.csv", "a+")
    conn = sqlite3.connect("abcsurvey.db")

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

        self.initDb()

        self.ui.tabWidget.currentChanged.connect(lambda: self.onTabChange())
        self.ui.resultLabel.setText(self.getTotalVisites())

    def onClickBtn(self, motif):
        now = datetime.now()
        humanTime = now.strftime('%H:%M')
        jourSemaine = now.strftime('%A')
        plageHoraire = self.getPlageHoraire(now)

        self.recordVisit(now, jourSemaine, plageHoraire, motif)
        self.changeLastVisit(motif, humanTime)
        self.getVisitsByPlageAndMotif()

    def recordVisit(self, time, jourSemaine, plageHoraire, motif):
        c = self.conn.cursor()
        c.execute(Consts.SQL_RECORD_VISIT, (time, jourSemaine, plageHoraire, motif))
        self.conn.commit()

    def changeLastVisit(self, motif, time):
        self.ui.resultLabel.setText(f'Dernière visite : <strong>{motif}</strong> à <strong>{time}</strong> {self.getTotalVisites()}')

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

    def initDb(self):
        c = self.conn.cursor()
        c.execute(Consts.CREATE_VISITES_TABLE)
        self.conn.commit()

    def getTotalVisites(self):
        c = self.conn.cursor()
        c.execute(Consts.SQL_TOTAL_VISITS)
        return f'Visites enregistrées : <strong>{c.fetchone()[0]}</strong>'

    def getVisitsByPlageAndMotif(self):
        c = self.conn.cursor()
        c.execute(Consts.SQL_VISITS_BY_PLAGE_AND_MOTIF)
        self.conn.commit()

    def onTabChange(self):
        tab_name = self.ui.tabWidget.currentWidget().objectName()
        if (tab_name == "tabData"):
            self.populateDataTab()

    def populateDataTab(self):
        print("populateDataTab")
        c = self.conn.cursor()

        c.execute(Consts.SQL_ALL_VISITS)
        data = c.fetchall()
        model = QStandardItemModel()
        model.setColumnCount(4)
        header_names = ["Date", "Jour de la semaine", "Plage horaire", "Motif"]
        model.setHorizontalHeaderLabels(header_names)

        for d in data:
            row = []
            for name in d:
                item = QStandardItem(name)
                item.setEditable(False)
                row.append(item)
            model.appendRow(row)
        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()



    def __del__(self):
        self.fw.close()
        self.conn.close()

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
