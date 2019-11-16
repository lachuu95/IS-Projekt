import sqlite3
from typing import List, Dict, Tuple
from src.common.constants import no_data_value


class ReadDB:
    def __init__(self, column_name: List[str]):
        self.__column_name = column_name
        self.__conn = None

    def create_connection(self, db_file_path: str):
        self.__conn = sqlite3.connect(db_file_path)

    def select_from_db(self, sql_query: str) -> List[Tuple[str]]:
        cur = self.__conn.cursor()
        cur.execute(sql_query)
        return cur.fetchall()

    def __fill_empty_cell(self, row_contents: List[str]) -> List[str]:
        return [x if x != "" else no_data_value() for x in row_contents]

    def convert_db_to_json(
        self, contents: List[Tuple[str]]
    ) -> Dict[str, Dict[str, str]]:
        data_dict = {}
        for idx, row in enumerate(contents, start=1):
            line = self.__fill_empty_cell(list(row[1:]))
            data_dict[str(idx)] = dict(zip(self.__column_name, line))
        return data_dict
