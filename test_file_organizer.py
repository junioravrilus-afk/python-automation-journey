from pathlib import Path 
from file_organizer import organize_folder

def test_organizer_single_image(tmp_path):
    image_file = tmp_path / "photo.jpg"
    image_file.write_text("contenu factice")

    organize_folder(tmp_path)

    expected_folder = tmp_path / "Images" / "photo.jpg"
    assert expected_folder.exists()


def test_no_overwrite_on_confilct(tmp_path):
    original_file = tmp_path / "photo.jpg"
    original_file.write_text("contenu original")

    images_folder = tmp_path / "Images"
    images_folder.mkdir()
    existing_file = images_folder / "photo.jpg"
    existing_file.write_text("contenu deja present")

    organize_folder(tmp_path)

    assert existing_file.read_text() == "contenu deja present"
    assert (images_folder / "photo_1.jpg").exists()