import re
import argparse
from pathlib import Path


def rename_img_files(folder_path, prefix="vacances", dry_run=False):
    folder = Path(folder_path)
    pattern = r"IMG_(\d+)\.jpg"

    for item in folder.iterdir():
        if item.is_file():
            match = re.match(pattern, item.name)

            if match:
                numbers = match.group(1)
                new_name = f"{prefix}_{numbers}.jpg"
                new_path = folder / new_name

                if dry_run:
                    print(f"[SIMULATION] Renommerait : {item.name} -> {new_name}")
                else:
                    item.rename(new_path)
                    print(f"Renomme : {item.name} -> {new_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Renomme en masse des fichiers IMG_XXXX.jpg")
    parser.add_argument("folder", help="Dossier contenant les fichiers a renommer")
    parser.add_argument("--dry-run", action="store_true", help="Simule sans renommer reellement")
    parser.add_argument("--prefix", default="vacances", help="Prefixe pour les nouveaux noms")

    args = parser.parse_args()

    rename_img_files(args.folder, prefix=args.prefix, dry_run=args.dry_run)