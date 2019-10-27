#!/usr/bin/env python3
import os
import sys
import argparse
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))
from src.common.constants import columns_headers, no_data_value, file_path_txt


def read_and_print_data(file_path: str) -> None:
    data = pd.read_csv(file_path, sep=";", header=None)
    columns_names = columns_headers()
    columns_names.append("none")
    data.columns = columns_names
    data = data.drop(columns=["none"])
    data = data.fillna(no_data_value())
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print(data)


if __name__ == "__main__":
    read_and_print_data(file_path_txt())
