from typing import List, Tuple, Dict
import os

# List[Tuple[name, DB_type, XML_name]]
COLUMNS_HEADERS = [
    ("Producent", "text", "manufacturer"),
    ("Przekątna", "text", "screen size"),
    ("Rozdzielczość", "text", "screen resolution"),
    ("Rodzaj matrycy", "text", "screen type"),
    ("Ekran dotykowy", "text", "screen touchscreen"),
    ("CPU", "text", "processor name"),
    ("Rdzenie", "text", "processor physical_cores"),
    ("Taktowanie", "text", "processor clock_speed"),
    ("RAM", "text", "ram"),
    ("Pojemność dysku", "text", "disc storage"),
    ("Typ dysku", "text", "disc type"),
    ("GPU", "text", "graphic_card name"),
    ("Pamieć GPU", "text", "graphic_card memory"),
    ("System operacyjny", "text", "os"),
    ("Napęd optyczny", "text", "disc_reader"),
]

RESOURCE_DIR = "resource"

FILE_PATH_TXT = "katalog.txt"

FILE_PATH_DB = "katalog.db"

FILE_PATH_XML = "katalog.xml"


def columns_headers() -> List[str]:
    return [name for name, _, _ in COLUMNS_HEADERS]


def translate_headers_xls_to_name() -> Dict[str, str]:
    return {xml_name: name for name, _, xml_name in COLUMNS_HEADERS}


def translate_headers_name_to_xls() -> Dict[str, str]:
    return {name: xml_name for name, _, xml_name in COLUMNS_HEADERS}


def columns_headers_and_type() -> List[Tuple[str]]:
    return [(name, typ) for name, typ, _ in COLUMNS_HEADERS]


def no_data_value() -> str:
    return "bd."


def file_path_txt() -> str:
    return os.path.join(os.getcwd(), RESOURCE_DIR, FILE_PATH_TXT)


def file_path_db() -> str:
    return os.path.join(os.getcwd(), RESOURCE_DIR, FILE_PATH_DB)


def file_path_xml() -> str:
    return os.path.join(os.getcwd(), RESOURCE_DIR, FILE_PATH_XML)


def file_path_log() -> str:
    return os.path.join(os.getcwd(), RESOURCE_DIR, "logs", "examples.log")


def table_name() -> str:
    return "katalog"
