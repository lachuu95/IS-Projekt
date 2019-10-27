import sqlite3
from typing import List, Dict, Tuple
from src.common.constants import no_data_value, columns_headers_and_type, columns_headers


class SaveDB:
    def __init__(self):
        self.__conn = None

    def create_connection(self, db_file_path: str):
        self.__conn = sqlite3.connect(db_file_path)
    
    def drop_table(self, table_name:str) -> None:
        cur = self.__conn.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {table_name};")
        self.__conn.commit()

    def create_table(self, table_name:str) -> None:
        column_types = ", ".join([f'"{name}" {type}' for name, type in columns_headers_and_type()])
        cur = self.__conn.cursor()
        cur.execute(
            f"""CREATE TABLE IF NOT EXISTS {table_name} (
                Id integer PRIMARY KEY, {column_types});"""
        )
        self.__conn.commit()

    def insert_into_db(self, table_name:str, data_list: Tuple[str]) -> None:
        column_name = ", ".join(f'"{name}"' for name in columns_headers())
        row = "("+", ".join("?"for _ in columns_headers())+")"
        content = ", ".join([row for x in range(int(len(data_list)/len(columns_headers())))])
        sql_insert = f"INSERT INTO {table_name} ({column_name}) VALUES{content};"
        cur = self.__conn.cursor()
        cur.execute(sql_insert, data_list)
        self.__conn.commit()

    def __set_empty_cell(self, row_contents: List[str]) -> List[str]:
        return [x if x != no_data_value() else "" for x in row_contents]


    def convert_json_to_db(
        self, contents: Dict[str, Dict[str, str]]
    ) -> Tuple[str]:
        data_tuple = ()
        for _, row in contents.items():
            data_tuple+=(tuple(self.__set_empty_cell(row.values())))
        return data_tuple
