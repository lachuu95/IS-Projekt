import sqlite3
from src.common.dataset import Dataset
from src.common.static_method import get_db_file_path, get_table_name, get_no_data_value

conn = sqlite3.connect(get_db_file_path())
cur = conn.cursor()
cur.execute(f"DROP TABLE IF EXISTS {get_table_name()};")
conn.commit()
cur.execute(
    f"""CREATE TABLE IF NOT EXISTS {get_table_name()} (
        Id integer PRIMARY KEY, "Producent" text, "Przekątna" text,
        "Rozdzielczość" text, "Rodzaj matrycy" text, "Ekran dotykowy" text,
        "CPU" text, "Rdzenie" text, "Taktowanie" text, "RAM" text,
        "Pojemność dysku" text, "Typ dysku" text, "GPU" text, "Pamieć GPU" text,
        "System operacyjny" text, "Napęd optyczny" text);"""
)
conn.commit()
sql_insert = f"""INSERT INTO {get_table_name()} (
    "Producent", "Przekątna", "Rozdzielczość", "Rodzaj matrycy",
    "Ekran dotykowy", "CPU", "Rdzenie", "Taktowanie", "RAM", "Pojemność dysku",
    "Typ dysku", "GPU", "Pamieć GPU", "System operacyjny", "Napęd optyczny")
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
data = Dataset()
data.read_data()
for _, row in data.data.items():
    row_tuple = tuple(item if item != get_no_data_value() else "" for _, item in row.items())
    cur.execute(sql_insert, row_tuple)
conn.commit()
