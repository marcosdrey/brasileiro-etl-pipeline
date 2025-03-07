import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()


TRANSFORMED_DATA_PATH = "../../data/transformed.csv"
INSERT_DATA_QUERY = "INSERT INTO brasileirao_data (placement, name, points, total_games, wins, draws, loses, goals_scored, goals_conceded, goals_difference, season, winning_percentage) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"


def connect_to_postgresql():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        dbname=os.getenv("POSTGRES_DB")
    )


def get_data(file_path):
    return pd.read_csv(file_path)


def create_table(connection, cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS brasileirao_data (
        id SERIAL PRIMARY KEY,
        placement INT NOT NULL,
        name VARCHAR(255) NOT NULL,
        points INT NOT NULL,
        total_games INT NOT NULL,
        wins INT NOT NULL,
        draws INT NOT NULL,
        loses INT NOT NULL,
        goals_scored INT NOT NULL,
        goals_conceded INT NOT NULL,
        goals_difference INT NOT NULL,
        season INT NOT NULL,
        winning_percentage NUMERIC(5,2) NOT NULL
    )
    """)
    connection.commit()


def insert_data(connection, cursor, query, data):
    cursor.executemany(query, data)
    connection.commit()


def main():
    with connect_to_postgresql() as conn:
        cursor = conn.cursor()
        create_table(conn, cursor)
        df = get_data(TRANSFORMED_DATA_PATH)
        clubs_list = [tuple(row) for i, row in df.iterrows()]
        insert_data(conn, cursor, INSERT_DATA_QUERY, clubs_list)


if __name__ == '__main__':
    main()
