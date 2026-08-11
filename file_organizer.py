import shutil
from pathlib import Path

EXTENSIONS_MAP = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".mp3": "Musique",
    ".mp4": "Videos",
}


def get_unique_destination(destination_folder, filename):
    destination = destination_folder / filename

    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix
    counter = 1

    while destination.exists():
        new_filename = f"{stem}_{counter}{suffix}"
        destination = destination_folder / new_filename
        counter += 1

    return destination


def organize_folder(folder_path):
    folder = Path(folder_path)

    for item in folder.iterdir():
        if item.is_file():
            extension = item.suffix.lower()

            if extension in EXTENSIONS_MAP:
                destination_folder = folder / EXTENSIONS_MAP[extension]
                destination_folder.mkdir(exist_ok=True)

                destination = get_unique_destination(destination_folder, item.name)
                shutil.move(str(item), str(destination))
                print(f"Deplace : {item.name} -> {destination.name}")


if __name__ == "__main__":
    organize_folder("test_folder")