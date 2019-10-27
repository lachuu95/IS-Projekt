import sqlite3
from typing import List, Dict, Tuple
from src.common.static_method import get_no_data_value


class ReadDB:
    def __init__(self, column_name: List[str]):
        self.__column_name = column_name
        self.__conn = None

    def create_connection(self, db_file_path: str):
        self.__conn = sqlite3.connect(db_file_path)

    def select_from_db(self, table_name: str) -> List[Tuple[str]]:
        cur = self.__conn.cursor()
        cur.execute(f"SELECT * FROM {table_name}")
        return cur.fetchall()

    def __fill_empty_cell(self, row_contents: List[str]) -> List[str]:
        return [x if x != "" else get_no_data_value() for x in row_contents]

    def convert_db_to_json(
        self, contents: List[Tuple[str]]
    ) -> Dict[str, Dict[str, str]]:
        data_dict = {}
        for row in contents:
            line = self.__fill_empty_cell(list(row[1:]))
            data_dict[row[0]] = dict(zip(self.__column_name, line))
        return data_dict
