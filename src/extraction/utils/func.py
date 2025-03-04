import re


def extract_infos_from_table_cell(cell):
    if cell.find("b"):
        value = cell.find('b').text.strip()
    else:
        value = cell.text.strip()
    value = re.sub(r'[\u2212\u2012\u2013\u2014\u2015]', "-", value)
    value = re.sub(r'[^\d-]', '', value)
    return int(value)
