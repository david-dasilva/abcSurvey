#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
class Consts:

    CSV_HEADERS = "date,jour semaine,plage horaire,motif\n"

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