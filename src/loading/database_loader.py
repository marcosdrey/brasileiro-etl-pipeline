import psycopg2
import os
import logging
from dotenv import load_dotenv


load_dotenv()
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DatabaseLoader:

    def __enter__(self):
        logging.info("Conectando ao banco de dados...")
        self.__conn = self.__connect_to_database()
        self.__cur = self.__conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        logging.info("Encerrando conexão ao banco de dados...")
        self.__cur.close()
        self.__conn.close()

    def create_table(self, query):
        logging.info("Criando tabela (ou apenas pegá-la caso já exista)...")
        self.__cur.execute(query)
        self.__conn.commit()

    def insert_data(self, query, data):
        logging.info("Inserindo dados...")
        self.__cur.executemany(query, data)
        self.__conn.commit()
        logging.info(f"{self.__cur.rowcount} dados inseridos na tabela.")

    def __connect_to_database(self):
        return psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            dbname=os.getenv("POSTGRES_DB"),
        )
