from src.common.dataset import Dataset
from typing import List
import PySimpleGUI as sg


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

    def get_gui_layout(self) -> List[List[sg.InputText]]:
        column_max_width = self.__data.calculate_column_char_width()
        header_layout = []
        for column_name in ["Lp."] + self.__data.columns_headers:
            header_layout.append(
                sg.In(
                    column_name,
                    size=(column_max_width[column_name], 1),
                    pad=(1, 1),
                    justification="center",
                    do_not_clear=True,
                    disabled=True,
                )
            )
        data_layout = [header_layout]
        for index, row in self.__data.data.items():
            row_layout = []
            row_layout.append(
                sg.In(
                    f"{index}",
                    size=(column_max_width["Lp."], 1),
                    pad=(1, 1),
                    justification="center",
                    do_not_clear=True,
                    disabled=True,
                )
            )
            for column_name in self.__data.columns_headers:
                row_layout.append(
                    sg.In(
                        row[column_name],
                        size=(column_max_width[column_name], 1),
                        pad=(1, 1),
                        justification="center",
                        key=(index, column_name),
                        do_not_clear=True,
                    )
                )
            data_layout.append(row_layout)
        return data_layout

    def create_layout(self, use_read_db: bool = False, use_write_db: bool = False) -> List[List[sg.InputText]]:
        index_number = len(self.__data.data)
        scrol = False
        if index_number >= 10:
            scrol = True
        button_label = [
            (True, "Wczytaj dane z pliku TXT"),
            (True, "Zapisz dane do pliku TXT"),
            (use_read_db, "Import z bazy danych"),
            (use_write_db, "Export do bazy danych"),
            (True, "Zamknij"),
        ]
        layout = [
            [sg.Button(x) for is_use, x in button_label if is_use]
            + [sg.Text(f"Źródło danych: {self.__data_source}")],
            [sg.Column(self.get_gui_layout(), scrollable=scrol)],
        ]
        return layout

    def show_gui(self, use_read_db: bool = False, use_write_db: bool = False) -> None:
        window = sg.Window(
            "Integracja Systemów - Błażej Łach", self.create_layout(use_read_db, use_write_db)
        )
        while True:
            event, values = window.read()
            if event is None or event == "Zamknij":
                break
            if event == "Wczytaj dane z pliku TXT":
                self.__data_source = "TXT"
                self.__data.read_data()
                window.close()
                window = sg.Window(
                    "Integracja Systemów - Błażej Łach", self.create_layout(use_read_db, use_write_db)
                )
            if event == "Zapisz dane do pliku TXT":
                self.__data.udate_data(values)
                self.__data.save_data()
                sg.Popup("Zapisano dane w plik txt.")
            if event == "Import z bazy danych" and use_read_db:
                self.__data_source = "DB"
                self.__data.read_data_db()
                window.close()
                window = sg.Window(
                    "Integracja Systemów - Błażej Łach", self.create_layout(use_read_db, use_write_db)
                )
            if event == "Export do bazy danych" and use_write_db:
                self.__data.udate_data(values)
                #self.__data.save_data()
                sg.Popup("Zapisano dane w bazie danych.")
        window.close()
