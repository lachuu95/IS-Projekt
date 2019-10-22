from src.common.read_txt import ReadTXT
from src.common.save_txt import SaveTXT
import PySimpleGUI as sg
from typing import Dict, List, Tuple


class Data:
    def __init__(self, column_name: List[str], file_path: str):
        self.column_name = column_name
        self.file_path = file_path
        self.data = {"0": {x: "" for x in column_name}}
        pass

    def read_data(self) -> Dict[str, Dict[str, str]]:
        txt_reader = ReadTXT(self.column_name)
        contents = txt_reader.read_from_file(self.file_path)
        contents_line = txt_reader.split_by_lines(contents)
        contents_line_split = [txt_reader.split_by_row(row) for row in contents_line]
        self.data = txt_reader.convert_lines_to_json(contents_line_split)
        return self.data

    def save_data(self) -> None:
        txt_saver = SaveTXT()
        contents_as_list = txt_saver.convert_json_to_lines(self.data)
        contents_line = [txt_saver.join_by_row(x) for x in contents_as_list]
        contents = txt_saver.join_by_lines(contents_line)
        txt_saver.save_to_file(self.file_path, contents)
    
    def add_row(self) -> None:
        next_index = max([int(x) for x in list(self.data.keys())]) + 1
        self.data[str(next_index)] = {x: "" for x in self.column_name}

    def calc_column_size(self) -> Tuple[int, int]:
        lp_max_len = 2
        col_max_len = {x: len(x) + 2 for x in self.column_name}
        for index, row in self.data.items():
            lp_max_len = max(len(str(index)) + 2, lp_max_len)
            for key, item in row.items():
                col_max_len[key] = max(len(str(item)) + 2, col_max_len[key])
        return (lp_max_len, col_max_len)

    def create_headers_row(self):
        lp_max_len, col_max_len = self.calc_column_size()
        columm_layout = []
        columm_layout.append(
            [
                sg.In(
                    "Lp.",
                    size=(lp_max_len, 1),
                    pad=(1, 1),
                    justification="center",
                    do_not_clear=True,
                    disabled=True,
                )
            ]
            + [
                sg.In(
                    x,
                    size=(col_max_len[x], 1),
                    pad=(1, 1),
                    justification="center",
                    do_not_clear=True,
                    disabled=True,
                )
                for x in self.column_name
            ]
        )
        return columm_layout

    def create_column_layout(self):
        lp_max_len, col_max_len = self.calc_column_size()
        columm_layout = []
        for index, row in self.data.items():
            inputs = [
                sg.In(
                    f"{index}",
                    size=(lp_max_len, 1),
                    pad=(1, 1),
                    justification="center",
                    do_not_clear=True,
                    disabled=True,
                )
            ] + [
                sg.In(
                    x,
                    size=(col_max_len[key], 1),
                    pad=(1, 1),
                    justification="center",
                    key=(index, key),
                    do_not_clear=True,
                )
                for key, x in row.items()
            ]
            columm_layout.append(inputs)
        return columm_layout

    def create_layout(self):
        index_number = len(list(self.data.keys()))
        scrol = False
        if index_number >= 10:
            scrol = True
        layout = [
            [
                sg.Button("Wczytaj dane z pliku TXT"),
                sg.Button("Zapisz dane do pliku TXT"),
                sg.Button("Dodaj wiersz"),
                sg.Button("Zamknij"),
            ],
            [sg.Column(self.create_headers_row())],
            [
                sg.Column(
                    self.create_column_layout(), scrollable=scrol
                )
            ],
        ]
        return layout
