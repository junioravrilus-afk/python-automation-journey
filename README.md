# File Organizer

Script Python qui organise automatiquement les fichiers d'un dossier
dans des sous-dossiers selon leur extension (Images, Documents, Musique, Videos).

## Fonctionnalités
- Détection automatique du type de fichier via son extension
- Création automatique des sous-dossiers si nécessaire
- Gestion des conflits de noms : aucun fichier n'est jamais écrasé
  (renommage automatique en cas de doublon, ex: photo_1.jpg)

## Utilisation 

Par défaut, organise le contenu du dossier `test_folder`.

## Compétences travaillées
- Manipulation de fichiers avec `pathlib` et `shutil`
- Dictionnaires pour le mapping extension → dossier
- Gestion de cas limites (fichiers en double, casse des extensions) 

## Utilisation avancee 

 si aucun argument n'est fourni, le scriptsutilise 'test_folder' par defaut. 

 ## test 

 ## Installation