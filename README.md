# File Organizer

Script Python qui organise automatiquement les fichiers d'un dossier
dans des sous-dossiers selon leur extension (Images, Documents, Musique, Videos).

## Fonctionnalites
- Detection automatique du type de fichier via son extension
- Creation automatique des sous-dossiers si necessaire
- Gestion des conflits de noms : aucun fichier n'est jamais ecrase
  (renommage automatique en cas de doublon, ex: photo_1.jpg)
- Dossier cible configurable via argument en ligne de commande

## Installation

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt


## Utilisation

python file_organizer.py chemin/vers/mon/dossier

Si aucun argument n'est fourni, le script utilise `test_folder` par defaut.

## Tests

pytest


## Competences travaillees
- Manipulation de fichiers avec `pathlib` et `shutil`
- Dictionnaires pour le mapping extension -> dossier
- Gestion de cas limites (fichiers en double, casse des extensions)
- Arguments en ligne de commande avec `sys.argv`
- Tests automatises avec `pytest` (fixture `tmp_path`, tests de non-regression)

---

# Bulk Renamer

Script Python qui renomme en masse des fichiers suivant le motif `IMG_XXXX.jpg`
vers un nouveau format personnalisable (ex: `vacances_XXXX.jpg`).

## Fonctionnalites
- Detection des fichiers via expression reguliere (`IMG_(\d+)\.jpg`)
- Prefixe personnalisable
- Mode simulation (`--dry-run`) pour previsualiser les changements avant de les appliquer reellement

## Utilisation

python bulk_renamer.py chemin/vers/mon/dossier --dry-run
python bulk_renamer.py chemin/vers/mon/dossier --prefix voyage


## Competences travaillees
- Expressions regulieres (`re.match`, groupes de capture)
- Arguments en ligne de commande avec `argparse` (arguments positionnels, drapeaux, valeurs par defaut)
- Pattern "dry-run" pour securiser les actions destructives/irreversibles
- Tests automatises couvrant a la fois le comportement reel et le mode simulation