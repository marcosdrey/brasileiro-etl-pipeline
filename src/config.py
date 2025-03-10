from pathlib import Path


project_root = Path(__file__).resolve().parent.parent


DATA_FOLDER = project_root / "data"


def get_data_file(filename: str):
    return DATA_FOLDER / filename
