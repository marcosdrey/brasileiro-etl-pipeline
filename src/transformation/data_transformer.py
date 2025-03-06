import pandas as pd
import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DataTransformer:
    def __init__(self, raw_data_path: str, save_data_path: str):
        self.raw_data_path = raw_data_path
        self.save_data_path = save_data_path
        self.df = self.__load_data()

    def __load_data(self):
        logging.info("Carregando dados do CSV...")
        return pd.read_csv(self.raw_data_path)

    def __fix_goals_difference(self):
        logging.info("Corrigindo saldo de gols...")
        self.df["goals_difference"] = self.df.goals_scored - self.df.goals_conceded

    def __change_names(self, hash_names: dict | None):
        if isinstance(hash_names, dict):
            logging.info("Padronizando nomes dos times...")
            self.df["name"] = self.df["name"].replace(hash_names)

    def __create_winning_percentage_column(self):
        logging.info("Calculando percentual de vitórias...")
        winning_percentage_series = (
            (self.df["points"] / (self.df["total_games"] * 3)) * 100
        ).round(2)
        self.df["winning_percentage"] = winning_percentage_series

    def __save_data(self):
        logging.info("Salvando dados transformados...")
        self.df.to_csv(self.save_data_path, index=False)

    def run(self, hash_names: dict | None):
        self.__fix_goals_difference()
        self.__change_names(hash_names)
        self.__create_winning_percentage_column()
        self.__save_data()
