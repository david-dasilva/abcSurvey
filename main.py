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

        self.ui.label_analyse1.setText(Consts.ANALYSE_1)
        self.ui.label_analyse2.setText(Consts.ANALYSE_2)
        self.ui.label_analyse3.setText(Consts.ANALYSE_3)
        self.ui.label_analyse4.setText(Consts.ANALYSE_4)
        self.ui.label_analyse5.setText(Consts.ANALYSE_5)

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
            self.populateDataView()
        if (tab_name == "tabAnalysis"):
            self.populateStatsView()

    def populateDataView(self):
        c = self.conn.cursor()

        c.execute(Consts.SQL_ALL_VISITS)
        data = c.fetchall()
        header_names = ["Date", "Jour de la semaine", "Plage horaire", "Motif"]
        self.populateTable(self.ui.allDataTableView, header_names, data)


    def populateStatsView(self):
        c = self.conn.cursor()

        c.execute(Consts.SQL_VISITS_BY_MOTIF)
        visits_by_motif = c.fetchall()
        self.populateTable(self.ui.tableView_1, ["Motif", "Visites"], visits_by_motif)

        c.execute(Consts.SQL_VISITS_BY_DAY)
        visits_by_day = c.fetchall()
        self.populateTable(self.ui.tableView_2, ["Jour", "Visites"], visits_by_day)

        c.execute(Consts.SQL_VISITS_BY_PLAGE)
        visits_by_plage = c.fetchall()
        self.populateTable(self.ui.tableView_3, ["Plage horaire", "Visites"], visits_by_plage)

        c.execute(Consts.SQL_VISITS_BY_PLAGE_AND_MOTIF)
        visits_by_plage_and_motif = c.fetchall()
        self.populateTable(self.ui.tableView_4, ["Plage horaire", "Motif", "Visites"], visits_by_plage_and_motif)

        c.execute(Consts.SQL_VISITS_BY_DAY_PLAGE_AND_MOTIF)
        visits_by_day_plage_and_motif = c.fetchall()
        self.populateTable(self.ui.tableView_5, ["Jour", "Plage horaire", "Motif", "Visites"], visits_by_day_plage_and_motif)

    def populateTable(self, tableView, header_names, data):
        model = QStandardItemModel()
        model.setColumnCount(len(header_names))
        model.setHorizontalHeaderLabels(header_names)

        for d in data:
            row = []
            for name in d:
                item = QStandardItem(f'{name}')
                item.setEditable(False)
                row.append(item)
            model.appendRow(row)

        tableView.setModel(model)
        tableView.resizeColumnsToContents()



    def __del__(self):
        self.fw.close()
        self.conn.close()

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
