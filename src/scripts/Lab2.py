#!/usr/bin/env python3
import os
import sys
import PySimpleGUI as sg

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))
from src.common.dataset import Dataset

def udate_data(data: Dataset, values) -> None:
    data.data = {
        index: {key: values[(index, key)] for key, _ in row.items()}
        for index, row in data.data.items()
    }

def create_layout(data: Dataset):
    index_number = len(data.data)
    scrol = False
    if index_number >= 10:
        scrol = True
    layout = [
        [
            sg.Button("Wczytaj dane z pliku TXT"),
            sg.Button("Zapisz dane do pliku TXT"),
            sg.Button("Zamknij"),
        ],
        [sg.Column(data.get_gui_layout(), scrollable=scrol)],
    ]
    return layout

data = Dataset()
window = sg.Window("Integracja Systemów - Błażej Łach", create_layout(data))

while True:
    event, values = window.read()
    if event is None or event == "Zamknij":
        break
    if event == "Wczytaj dane z pliku TXT":
        data.read_data()
        window.close()
        window = sg.Window("Integracja Systemów - Błażej Łach", create_layout(data))
    if event == "Zapisz dane do pliku TXT":
        udate_data(data, values)
        data.save_data()
        sg.Popup('Zapisano dane.') 

window.close()
