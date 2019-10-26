from src.common.read_txt import ReadTXT
from src.common.save_txt import SaveTXT
import PySimpleGUI as sg
from typing import Dict, List, Tuple
from src.common.static_method import get_columns_headers, get_file_path
import os


class Dataset:
    def __init__(self) -> None:
        self.__file_path = self.__is_file(get_file_path())
        self.__columns_headers = get_columns_headers()
        self.__data = {"0": {x: "" for x in self.__columns_headers}}

    @property
    def data(self) -> Dict[str, Dict[str, str]]:
        return self.__data

    @data.setter
    def data(self, data:Dict[str, Dict[str, str]]) -> None:
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

    def calculate_column_char_width(self) -> Dict[str, int]:
        column_max_width = {x: len(x) + 2 for x in ["Lp."] + self.__columns_headers}
        for index, row in self.__data.items():
            column_max_width["Lp."] = max(len(str(index)) + 2, column_max_width["Lp."])
            for key, item in row.items():
                column_max_width[key] = max(len(str(item)) + 2, column_max_width[key])
        return column_max_width

    def __is_file(self, file_path: str) -> str:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File {get_file_path()} doesn't exist.")
        else:
            return file_path

    def get_console_layout(self) -> str:
        column_max_width = self.calculate_column_char_width()
        header_layout = "|"
        for column_name in ["Lp."] + self.__columns_headers:
            header_layout += "{:^{}}|".format(
                column_name, column_max_width[column_name]
            )
        data_layout = ""
        for index, row in self.__data.items():
            data_layout += "|{:^{}}|".format(str(index), column_max_width["Lp."])
            for column_name in self.__columns_headers:
                data_layout += "{:^{}}|".format(
                    row[column_name], column_max_width[column_name]
                )
            data_layout += "\n"
        tab_size = len(header_layout)
        console_layout = "{:-^{}}".format("", tab_size)+"\n"+header_layout+"\n"+"{:-^{}}".format("", tab_size)+"\n"+data_layout+"{:-^{}}".format("", tab_size)
        return console_layout

    def get_gui_layout(self):
        column_max_width = self.calculate_column_char_width()
        header_layout = []
        for column_name in ["Lp."] + self.__columns_headers:
            header_layout.append(
                sg.In(column_name, size=(column_max_width[column_name], 1), pad=(1, 1), justification="center", do_not_clear=True, disabled=True)
            )
        data_layout = [header_layout]
        for index, row in self.__data.items():
            row_layout = []
            row_layout.append(sg.In(f"{index}", size=(column_max_width["Lp."], 1), pad=(1, 1), justification="center", do_not_clear=True, disabled=True))
            for column_name in self.__columns_headers:
                row_layout.append(sg.In(row[column_name], size=(column_max_width[column_name], 1), pad=(1, 1), justification="center", key=(index, column_name), do_not_clear=True))
            data_layout.append(row_layout)
        return data_layout
