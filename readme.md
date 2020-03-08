# Sondage des visites de l'Abc de Blanquefort

Le but de l'application est d'enregistrer l'heure et le motif des visites à l'ABC de Blanquefort sur plusieurs mois, afin d'analyser les données et d'optimiser les horaires de présence.

## Installation

1. Télécharger le zip de l'application et le dézipper sur le PC de l'accueil (par ex: dans `C:\abcSurvey`)
2. Créer un raccourci sur le bureau, pointant sur `C:\abcSurvey\dist\abcSurvey-windows.exe`
3. Executer une première fois l'application, pour que la base de données soit générée : un fichier `abcsurvey.db` va être créé dans `C:\abcSurvey\dist\`. **Il est impératif de ne pas supprimer ce fichier, sinon toutes les données sont perdues!**

## Utilisation

Lors d'une visite, cliquer sur le motif le plus approprié.

L'application va alors enregistrer l'heure de la visite et le motif dans la base de données.

Un message confirmant l'enregistrement s'affiche brièvement en bas de la fenêtre.

Les données enregistrées peuvent être consultées dans les onglets *Données* et *Analyse*.

## Analyse des données

Une série de requêtes sur les données enregistrées est disponible n'importe quand durant la periode de l'étude, via l'onglet Analyse.

Une fois l'étude jugée terminée, il est possible de créer de nouvelles requêtes plus fines sur les données obtenues, **à condition de bien conserver le fichier `abcSurvey.db`**

## Contact

Pour toute question sur le logiciel, merci de s'adresser à Julien, ou à moi-même par e-mail : contact@daviddasilva.net

## Développement

La base de donnée repose sur SQLite.

L'interface graphique est créé via QT Creator.

Pour générer le mapping python de la maquette : `pyuic5 mainwindow.ui -x -o gui.py`

Pour générer l'éxecutable contenant toutes les librairies nécéssaire à l'éxecution, il faut utiliser **PyInstaller** depuis l'OS cible. PyInstaller ne peut pas générer un executable Windows depuis Linux, et inversement.

Depuis l'OS cible : 
```pyinstaller --onefile main.pyw --name abcSurvey-OS```
