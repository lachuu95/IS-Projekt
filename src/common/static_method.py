from typing import List
import os

def get_columns_headers() -> List[str]:
    columns_headers = [
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
    return columns_headers


def get_no_data_value() -> str:
    return "bd."

def get_file_path() -> str:
    return os.path.join(os.getcwd(), "resource", "katalog.txt")
