# File Organizer

Script Python qui organise automatiquement les fichiers d'un dossier
dans des sous-dossiers selon leur extension (Images, Documents, Musique, Videos).

## Fonctionnalités
- Détection automatique du type de fichier via son extension
- Création automatique des sous-dossiers si nécessaire
- Gestion des conflits de noms : aucun fichier n'est jamais écrasé
  (renommage automatique en cas de doublon, ex: photo_1.jpg)
- Dossier cible configurable via argument en ligne de commande

## Installation 

## Utilisation 

Si aucun argument n'est fourni, le script utilise `test_folder` par défaut.

## Tests

## Compétences travaillées
- Manipulation de fichiers avec `pathlib` et `shutil`
- Dictionnaires pour le mapping extension → dossier
- Gestion de cas limites (fichiers en double, casse des extensions)
- Arguments en ligne de commande avec `sys.argv`
- Tests automatisés avec `pytest` (fixture `tmp_path`, tests de non-régression)