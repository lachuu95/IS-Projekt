from src.common.read_txt import ReadTXT
from src.common.save_txt import SaveTXT
from src.common.read_db import ReadDB
from src.common.save_db import SaveDB
from typing import Dict, List, Tuple
from src.common.constants import (
    columns_headers,
    file_path_txt,
    file_path_db,
    table_name,
)
import os


class Dataset:
    def __init__(self) -> None:
        self.__file_path = self.__is_file(file_path_txt())
        self.__columns_headers = columns_headers()
        self.__data = {"1": {x: "" for x in self.__columns_headers}}

    @property
    def data(self) -> Dict[str, Dict[str, str]]:
        return self.__data

    @data.setter
    def data(self, data: Dict[str, Dict[str, str]]) -> None:
        self.__data = data

    @property
    def columns_headers(self) -> List[str]:
        return self.__columns_headers

    def read_data(self) -> None:
        txt_reader = ReadTXT(self.__columns_headers)
        contents = txt_reader.read_from_file(self.__is_file(self.__file_path))
        contents_line = txt_reader.split_by_lines(contents)
        contents_line_split = [txt_reader.split_by_row(row) for row in contents_line]
        self.__data = txt_reader.convert_lines_to_json(contents_line_split)

    def save_data(self) -> None:
        txt_saver = SaveTXT()
        contents_line_split = txt_saver.convert_json_to_lines(self.__data)
        contents_line = [txt_saver.join_by_row(x) for x in contents_line_split]
        contents = txt_saver.join_by_lines(contents_line)
        txt_saver.save_to_file(self.__file_path, contents)

    def read_data_db(self) -> None:
        db_reader = ReadDB(self.__columns_headers)
        db_reader.create_connection(self.__is_file(file_path_db()))
        contents = db_reader.select_from_db(table_name())
        self.__data = db_reader.convert_db_to_json(contents)

    def save_data_db(self) -> None:
        db_saver = SaveDB()
        db_saver.create_connection(file_path_db())
        db_saver.drop_table(table_name())
        db_saver.create_table(table_name())
        contents = db_saver.convert_json_to_db(self.__data)
        db_saver.insert_into_db(table_name(),contents)

    def calculate_column_char_width(self) -> Dict[str, int]:
        column_max_width = {x: len(x) + 2 for x in ["Lp."] + self.__columns_headers}
        for index, row in self.__data.items():
            column_max_width["Lp."] = max(len(str(index)) + 2, column_max_width["Lp."])
            for key, item in row.items():
                column_max_width[key] = max(len(str(item)) + 2, column_max_width[key])
        return column_max_width

    def __is_file(self, file_path: str) -> str:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File {file_path} doesn't exist.")
        else:
            return file_path

    def udate_data(self, values: Dict[Tuple[str, str], str]) -> None:
        self.__data = {
            index: {key: values[(index, key)] for key, _ in row.items()}
            for index, row in self.__data.items()
        }
