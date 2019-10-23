#!/usr/bin/env python3
import os
import sys
import argparse
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))
from src.common.static_method import get_columns_headers, get_no_data_value


def read_and_print_data(file_path: str) -> None:
    data = pd.read_csv(file_path, sep=";", header=None)
    columns_headers = get_columns_headers()
    columns_headers.append("none")
    data.columns = columns_headers
    data = data.drop(columns=["none"])
    data = data.fillna(get_no_data_value())
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read from txt file and print data.")
    parser.add_argument(
        "txt_file_path", type=str, help="Path to the text file with data."
    )
    args = parser.parse_args()
    if os.path.isfile(args.txt_file_path):
        read_and_print_data(args.txt_file_path)
    else:
        print(f"File {args.txt_file_path} doesn't exist.")
