#!/usr/bin/env python3
import os
import argparse
from typing import List, Dict
import sys
sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))
from src.common.read_txt import ReadTXT


def print_file(data_dict: Dict[int, Dict[str, str]]) -> None:
    for key, value in data_dict.items():
        print(f"index: {key}")
        for key, value in value.items():
            print(f"{key}: {value}")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read from txt file and print it.")
    parser.add_argument("path_to_file", type=str, help="Path to read file")
    args = parser.parse_args()
    if os.path.isfile(args.path_to_file):
        column_name = [
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
        txt_reader = ReadTXT(column_name)
        contents = txt_reader.read_from_file(args.path_to_file)
        contents_line = txt_reader.split_by_lines(contents)
        contents_line_split = [txt_reader.split_by_row(row) for row in contents_line]
        data = txt_reader.convert_lines_to_json(contents_line_split)
        print_file(data)
    else:
        print(f"file {args.path_to_file} doesn't exist.")
