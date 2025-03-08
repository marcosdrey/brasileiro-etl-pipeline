import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()


class DatabaseLoader:

    def __enter__(self):
        self.__conn = self.__connect_to_database()
        self.__cur = self.__conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__cur.close()
        self.__conn.close()

    def create_table(self, query):
        self.__cur.execute(query)
        self.__conn.commit()

    def insert_data(self, query, data):
        self.__cur.executemany(query, data)
        self.__conn.commit()

    def __connect_to_database(self):
        return psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            dbname=os.getenv("POSTGRES_DB"),
        )
