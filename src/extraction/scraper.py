import sys
import requests
import csv
from bs4 import BeautifulSoup
from utils.func import extract_infos_from_table_cell


DEFAULT_START_YEAR = "2003"
DEFAULT_END_YEAR = "2024"

start_year = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_START_YEAR

try:
    start_year = int(start_year)

except ValueError:
    raise ValueError(f"'year' argument needs to be an integer.")

if start_year < 2003 or start_year > 2024:
    raise ValueError("'year' argument needs to be between 2003 and 2024 (years available atm)")

current_year = start_year
list_clubs = []

while current_year < 2025:
    url_path = f"https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_{current_year}_-_Série_A"
    response = requests.get(url_path)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        h2_title = soup.find('h2', id="Classificação")
        tbody = h2_title.find_next("tbody")
        table_value_rows = tbody.find_all('tr')[1:]

        for row in table_value_rows:
            th_position_row = row.find("th", scope="row")
            values = row.find_all('td')

            if th_position_row:
                values.insert(0, th_position_row)
            club_position = int(values[0].text.strip())

            if values[1].find("b"):
                club_name = values[1].find('b').find_all('a')[1].text.strip()
            else:
                club_name = values[1].find_all('a')[1].text.strip()

            club_points = extract_infos_from_table_cell(values[2])
            club_total_games = extract_infos_from_table_cell(values[3])
            club_wins = extract_infos_from_table_cell(values[4])
            club_draws = extract_infos_from_table_cell(values[5])
            club_loses = extract_infos_from_table_cell(values[6])
            club_goals_scored = extract_infos_from_table_cell(values[7])
            club_goals_conceded = extract_infos_from_table_cell(values[8])
            club_goals_difference = extract_infos_from_table_cell(values[9])

            club = {
                "position": club_position,
                "name": club_name,
                "points": club_points,
                "total_games": club_total_games,
                "wins": club_wins,
                "draws": club_draws,
                "loses": club_loses,
                "goals_scored": club_goals_scored,
                "goals_conceded": club_goals_conceded,
                "goals_difference": club_goals_difference,
                "season": current_year
            }
            list_clubs.append(club)

        current_year += 1

    else:
        raise Exception(f"Request error. URL likely is wrong or has restrict access. Status code: {response.status_code}")

with open('../../data/raw.csv', mode='w') as file:
    dict_writer = csv.DictWriter(file, fieldnames=list_clubs[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(list_clubs)