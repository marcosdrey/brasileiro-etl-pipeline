CREATE_TABLE_QUERY = """
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
"""

INSERT_DATA_QUERY = "INSERT INTO brasileirao_data (placement, name, points, total_games, wins, draws, loses, goals_scored, goals_conceded, goals_difference, season, winning_percentage) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
