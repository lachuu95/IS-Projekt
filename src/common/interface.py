import sys
from src.common.dataset import Dataset
from src.common.window import Window
from PyQt5.QtWidgets import QApplication
from typing import List


class Interface:
    def __init__(self, data: Dataset) -> None:
        self.__data = data
        self.__data_source = "Brak"

    def get_console_layout(self) -> str:
        column_max_width = self.__data.calculate_column_char_width()
        header_layout = "|"
        for column_name in ["Lp."] + self.__data.columns_headers:
            header_layout += "{:^{}}|".format(
                column_name, column_max_width[column_name]
            )
        data_layout = ""
        for index, row in self.__data.data.items():
            data_layout += "|{:^{}}|".format(str(index), column_max_width["Lp."])
            for column_name in self.__data.columns_headers:
                data_layout += "{:^{}}|".format(
                    row[column_name], column_max_width[column_name]
                )
            data_layout += "\n"
        tab_size = len(header_layout)
        console_layout = (
            "{:-^{}}".format("", tab_size)
            + "\n"
            + header_layout
            + "\n"
            + "{:-^{}}".format("", tab_size)
            + "\n"
            + data_layout
            + "{:-^{}}".format("", tab_size)
        )
        return console_layout

    def show_gui(self, **kwargs) -> None:
        app = QApplication([])
        window = Window(self.__data, **kwargs)
        window.show()
        sys.exit(app.exec_())
        