import sys
import requests
import csv
from bs4 import BeautifulSoup
from src.extraction.utils.func import get_infos_from_club
from src.config import get_data_file


# First year of the current format of Brasileirão. Data collection may not work below this year.
BASE_START_YEAR = 2003

# Currently, the Brasileirão 2025 hasn't started yet, so it doesn't make sense to include it.
BASE_END_YEAR = 2024

DEFAULT_SCRAPING_START_YEAR = 2003
DEFAULT_SCRAPING_END_YEAR = 2024


def main():
    start_year = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SCRAPING_START_YEAR

    try:
        start_year = int(start_year)

    except ValueError:
        raise ValueError("'start_year' argument needs to be an integer.")

    if start_year < BASE_START_YEAR or start_year > BASE_END_YEAR:
        raise ValueError(
            f"'year' argument needs to be between {BASE_START_YEAR} and {BASE_END_YEAR} (years available atm)"
        )

    current_year = start_year
    list_clubs = []

    while current_year <= DEFAULT_SCRAPING_END_YEAR:
        url_path = f"https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_{current_year}_-_Série_A"
        response = requests.get(url_path)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            h2_title = soup.find("h2", id="Classificação")
            tbody = h2_title.find_next("tbody")
            table_value_rows = tbody.find_all("tr")[1:]

            for row in table_value_rows:
                club = get_infos_from_club(row, current_year)
                list_clubs.append(club)

            current_year += 1

        else:
            raise Exception(
                f"Request error. URL is likely wrong or has restricted access. Status code: {response.status_code}"
            )

    with open(get_data_file('raw.csv'), mode="w") as file:
        dict_writer = csv.DictWriter(file, fieldnames=list_clubs[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(list_clubs)


if __name__ == "__main__":
    main()
