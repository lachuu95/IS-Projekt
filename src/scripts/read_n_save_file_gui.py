#coding=<iso-8859-1>
#!/usr/bin/env python

import PySimpleGUI as sg
import os
import sys
from typing import Dict, List, Tuple

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))
from src.common.data import Data


def udate_data(dataset: Data, values) -> None:
    dataset.data = {
        index: {key: values[(index, key)] for key, _ in row.items()}
        for index, row in dataset.data.items()
    }


file_path = "resource/katalog.txt"
column_name = [
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
]
dataset = Data(column_name, file_path)

window = sg.Window("Integracja Systemów - Błażej Łach", dataset.create_layout())

while True:
    event, values = window.read()
    if event is None or event == "Zamknij":
        break
    if event == "Wczytaj dane z pliku TXT":
        dataset.read_data()
        window.close()
        window = sg.Window("Integracja Systemów - Błażej Łach", dataset.create_layout())
    if event == "Zapisz dane do pliku TXT":
        udate_data(dataset, values)
        dataset.save_data()
    if event == "Dodaj wiersz":
        udate_data(dataset, values)
        dataset.add_row()
        window.close()
        window = sg.Window("Integracja Systemów - Błażej Łach", dataset.create_layout())

window.close()
