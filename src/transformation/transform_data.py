from data_transformer import DataTransformer


RAW_CSV_PATH = "../../data/raw.csv"
SAVE_CSV_PATH = "../../data/transformed.csv"
HASH_NAMES = {
    "Atlético Paranaense": "Athletico Paranaense",
    "Grêmio Prudente": "Grêmio Barueri",
}


def main():
    transformer = DataTransformer(RAW_CSV_PATH, SAVE_CSV_PATH)
    transformer.run(HASH_NAMES)


if __name__ == "__main__":
    main()
