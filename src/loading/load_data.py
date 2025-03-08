import pandas as pd
import queries as q
from database_loader import DatabaseLoader


TRANSFORMED_DATA_PATH = "../../data/transformed.csv"


def get_data(file_path):
    return pd.read_csv(file_path)


def main():
    with DatabaseLoader() as db_loader:
        db_loader.create_table(q.CREATE_TABLE_QUERY)
        df = get_data(TRANSFORMED_DATA_PATH)
        clubs_list = [tuple(row) for _, row in df.iterrows()]
        db_loader.insert_data(q.INSERT_DATA_QUERY, clubs_list)


if __name__ == "__main__":
    main()
