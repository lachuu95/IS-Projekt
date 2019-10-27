#!/usr/bin/env python3
import os
import sys
import sqlite3

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))
from src.common.dataset import Dataset
from src.common.constants import file_path_db, table_name, no_data_value, columns_headers_and_type, columns_headers

conn = sqlite3.connect(file_path_db())
cur = conn.cursor()
cur.execute(f"DROP TABLE IF EXISTS {table_name()};")
conn.commit()
column_types = ", ".join([f'"{name}" {type}' for name, type in columns_headers_and_type()])
cur.execute(
    f"""CREATE TABLE IF NOT EXISTS {table_name()} (
        Id integer PRIMARY KEY, {column_types});"""
)
conn.commit()
column_name = ", ".join(f'"{name}"' for name in columns_headers())
sql_insert = f"""INSERT INTO {table_name()} ({column_name})
    VALUES({", ".join("?"for _ in columns_headers())});"""
data = Dataset()
data.read_data()
for _, row in data.data.items():
    row_tuple = tuple(
        item if item != no_data_value() else "" for _, item in row.items()
    )
    cur.execute(sql_insert, row_tuple)
conn.commit()
