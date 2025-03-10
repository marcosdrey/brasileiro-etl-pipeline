from src.transformation.data_transformer import DataTransformer
from src.config import get_data_file


RAW_CSV_PATH = get_data_file("raw.csv")
SAVE_CSV_PATH = get_data_file("transformed.csv")
HASH_NAMES = {
    "Atlético Paranaense": "Athletico Paranaense",
    "Grêmio Prudente": "Grêmio Barueri",
}


def main():
    transformer = DataTransformer(RAW_CSV_PATH, SAVE_CSV_PATH)
    transformer.run(HASH_NAMES)


if __name__ == "__main__":
    main()
