import re


def get_infos_from_club(row, current_year):
    th_placement_row = row.find("th", scope="row")
    values = row.find_all('td')

    if th_placement_row:
        values.insert(0, th_placement_row)
    club_placement = int(values[0].text.strip())

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

    return {
        "placement": club_placement,
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


def extract_infos_from_table_cell(cell):
    if cell.find("b"):
        value = cell.find('b').text.strip()
    else:
        value = cell.text.strip()
    value = re.sub(r'[\u2212\u2012\u2013\u2014\u2015]', "-", value)
    value = re.sub(r'[^\d-]', '', value)
    return int(value)
