#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime


class Consts:

    TAB_1 = "Visites"
    TAB_2 = "Données"
    TAB_3 = "Analyse"

    # Motifs de visite
    MOTIF_CHOIX1 = "Jeunesse"
    MOTIF_CHOIX2 = "Vie associative"
    MOTIF_CHOIX3 = "Pratiques artistiques"
    MOTIF_CHOIX4 = "Courrier"
    MOTIF_CHOIX5 = "Borne internet"
    MOTIF_CHOIX6 = "Autres renseignements"

    # Plages horaires
    PLAGE_1_LABEL = "9:00 - 10:30"
    PLAGE_1_START = datetime.time().replace(hour=9, minute=0, second=0, microsecond=0)
    PLAGE_1_END = datetime.time().replace(hour=10, minute=30, second=0, microsecond=0)

    PLAGE_2_LABEL = "10:30 - 12:00"
    PLAGE_2_START = datetime.time().replace(hour=10, minute=30, second=0, microsecond=0)
    PLAGE_2_END = datetime.time().replace(hour=12, minute=0, second=0, microsecond=0)

    PLAGE_3_LABEL = "13:30 - 15:00"
    PLAGE_3_START = datetime.time().replace(hour=13, minute=30, second=0, microsecond=0)
    PLAGE_3_END = datetime.time().replace(hour=15, minute=0, second=0, microsecond=0)

    PLAGE_4_LABEL = "15:00 - 16:30"
    PLAGE_4_START = datetime.time().replace(hour=15, minute=0, second=0, microsecond=0)
    PLAGE_4_END = datetime.time().replace(hour=16, minute=30, second=0, microsecond=0)

    PLAGE_5_LABEL = "16: 30 - 18:00"
    PLAGE_5_START = datetime.time().replace(hour=16, minute=30, second=0, microsecond=0)
    PLAGE_5_END = datetime.time().replace(hour=18, minute=0, second=0, microsecond=0)

    PLAGE_6_LABEL = "18:00 - 19:00"
    PLAGE_6_START = datetime.time().replace(hour=18, minute=0, second=0, microsecond=0)
    PLAGE_6_END = datetime.time().replace(hour=19, minute=00, second=0, microsecond=0)

    PLAGE_AFTER_LABEL = "hors ouverture"

    ANALYSE_1 = "Nombre de visites par motif"
    ANALYSE_2 = "Nombre de visites par jour de semaine"
    ANALYSE_3 = "Nombre de visites par plage horaire"
    ANALYSE_4 = "Nombre de visites par plage horaire et par motif"
    ANALYSE_5 = "Nombre de visites par jour de semaine et par plage horaire"
    ANALYSE_6 = "Nombre de visites par jour, par plage horaire et par motif"

    # Database
    CREATE_VISITES_TABLE = '''CREATE TABLE IF NOT EXISTS visites (date text, jour text, plage text, motif text)'''
    SQL_RECORD_VISIT = '''INSERT INTO visites VALUES (?, ?, ?, ?)'''
    SQL_ALL_VISITS = '''SELECT * FROM visites order by date asc'''

    SQL_TOTAL_VISITS = '''SELECT count(*) from visites'''
    SQL_VISITS_BY_PLAGE = '''SELECT plage, COUNT(*) AS total FROM visites GROUP BY plage ORDER BY total DESC;'''
    SQL_VISITS_BY_MOTIF = '''SELECT motif, COUNT(*) AS total FROM visites GROUP BY motif ORDER BY total DESC;'''
    SQL_VISITS_BY_DAY = '''SELECT jour, COUNT(*) AS total FROM visites GROUP BY jour ORDER BY total DESC;'''
    SQL_VISITS_BY_PLAGE_AND_MOTIF = '''SELECT plage, motif, COUNT(*) AS total FROM visites GROUP BY plage, motif ORDER BY total DESC;'''
    SQL_VISITS_BY_PLAGE_AND_DAY = '''SELECT jour, plage, COUNT(*) AS total FROM visites GROUP BY jour, plage ORDER BY total DESC;'''
    SQL_VISITS_BY_DAY_PLAGE_AND_MOTIF = '''SELECT jour, plage, motif, COUNT(*) AS total FROM visites GROUP BY jour, plage, motif ORDER BY total DESC;'''
