#!/usr/bin/env python3
import os
import argparse
import pandas as pd
from typing import List

def data_name_list() -> List[str]:
    return [
        "Producent",
        "Przekątna",
        "Rozdzielczość",
        "Rodzaj matrycy",
        "Parametr tak vs nie",
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
        "none"
    ]
def read_n_print(file_path:str)->None:
    data = pd.read_csv(file_path, sep=";", header=None)
    data.columns = data_name_list()
    data = data.drop(columns=["none"])
    data = data.fillna("brak danych")
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read from txt file and print it.")
    parser.add_argument("path_to_file", type=str, help="Path to read file")
    args = parser.parse_args()
    if os.path.isfile(args.path_to_file):
        read_n_print(args.path_to_file)
    else:
        print(f"file {args.path_to_file} doesn't exist.")
