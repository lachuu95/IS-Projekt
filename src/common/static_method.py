from typing import List
import os


def get_columns_headers() -> List[str]:
    return [
        "Producent",
        "Przekątna",
        "Rozdzielczość",
        "Rodzaj matrycy",
        "Ekran dotykowy",
        "CPU",
        "Rdzenie",
        "Taktowanie",
        "RAM",
        "Pojemność dysku",
        "Typ dysku",
        "GPU",
        "Pamieć GPU",
        "System operacyjny",
        "Napęd optyczny",
    ]


def get_no_data_value() -> str:
    return "bd."


def get_file_path() -> str:
    return os.path.join(os.getcwd(), "resource", "katalog.txt")


def get_db_file_path() -> str:
    return os.path.join(os.getcwd(), "resource", "katalog.db")


def get_table_name() -> str:
    return "katalog"
