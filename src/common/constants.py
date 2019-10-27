from typing import List, Tuple
import os

COLUMNS_HEADERS = [
    ("Producent", "text"),
    ("Przekątna", "text"),
    ("Rozdzielczość", "text"),
    ("Rodzaj matrycy", "text"),
    ("Ekran dotykowy", "text"),
    ("CPU", "text"),
    ("Rdzenie", "text"),
    ("Taktowanie", "text"),
    ("RAM", "text"),
    ("Pojemność dysku", "text"),
    ("Typ dysku", "text"),
    ("GPU", "text"),
    ("Pamieć GPU", "text"),
    ("System operacyjny", "text"),
    ("Napęd optyczny", "text"),
]

RESOURCE_DIR = "resource"

FILE_PATH_TXT = "katalog.txt"

FILE_PATH_DB = "katalog.db"


def columns_headers() -> List[str]:
    columns_headers = [name for name, _ in COLUMNS_HEADERS]
    return columns_headers


def columns_headers_and_type() -> List[Tuple[str]]:
    return COLUMNS_HEADERS


def no_data_value() -> str:
    return "bd."


def file_path_txt() -> str:
    return os.path.join(os.getcwd(), RESOURCE_DIR, FILE_PATH_TXT)


def file_path_db() -> str:
    return os.path.join(os.getcwd(), RESOURCE_DIR, FILE_PATH_DB)


def table_name() -> str:
    return "katalog"
