from pathlib import Path 
from bulk_renamer import rename_img_files

def test_renames_matching_files(tmp_path):
    image_file = tmp_path / "IMG_0042.jpg"
    image_file.write_text("contenu factice")

    rename_img_files(tmp_path, prefix="vacances", dry_run=False)

    expected_file = tmp_path / "vacances_0042.jpg"
    assert expected_file.exists()
    assert not image_file.exists()

def test_dry_run_does_not_rename(tmp_path):
    image_file = tmp_path / "IMG_0099.jpg"
    image_file.write_text("contenu factice")

    rename_img_files(tmp_path, prefix="vacances", dry_run=True)

    assert image_file.exists()
    unexpected_file = tmp_path / "vacances_0099.jpg"
    assert not unexpected_file.exists()