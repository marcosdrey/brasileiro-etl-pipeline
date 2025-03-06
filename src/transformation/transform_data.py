import pandas as pd


RAW_CSV_PATH = "../../data/raw.csv"
SAVE_CSV_PATH = "../../data/transformed.csv"
HASH_NAMES = {
    "Atlético Paranaense": "Athletico Paranaense",
    "Grêmio Prudente": "Grêmio Barueri"
}


def load_data(file_path: str):
    return pd.read_csv(file_path)


def fix_goals_difference(df: pd.DataFrame):
    df['goals_difference'] = df.goals_scored - df.goals_conceded


def change_names(hash_names: dict, df: pd.DataFrame):
    for key in hash_names.keys():
        df.loc[df['name'] == key, 'name'] = hash_names[key]


def create_winning_percentage_column(df: pd.DataFrame):
    winning_percentage_series = ((df['points'] / (df['total_games'] * 3)) * 100).round(2)
    df['winning_percentage'] = winning_percentage_series


def save_data(file_path: str, df: pd.DataFrame):
    df.to_csv(file_path, index=False)


def main():
    df = load_data(RAW_CSV_PATH)

    fix_goals_difference(df)

    change_names(HASH_NAMES, df)

    create_winning_percentage_column(df)

    save_data(SAVE_CSV_PATH, df)


if __name__ == '__main__':
    main()
