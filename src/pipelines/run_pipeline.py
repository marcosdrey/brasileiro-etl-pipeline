from src.extraction import scraper
from src.transformation import transform_data
from src.loading import load_data


def main():
    scraper.main()
    transform_data.main()
    load_data.main()


if __name__ == '__main__':
    main()
