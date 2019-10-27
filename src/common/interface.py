from src.common.dataset import Dataset
from typing import List
import PySimpleGUI as sg

class Interface:
    def __init__(self, data: Dataset) -> None:
        self.__data = data
        
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
        console_layout = "{:-^{}}".format("", tab_size)+"\n"+header_layout+"\n"+"{:-^{}}".format("", tab_size)+"\n"+data_layout+"{:-^{}}".format("", tab_size)
        return console_layout

    def get_gui_layout(self) -> List[List[sg.InputText]]:
        column_max_width = self.__data.calculate_column_char_width()
        header_layout = []
        for column_name in ["Lp."] + self.__data.columns_headers:
            header_layout.append(
                sg.In(column_name, size=(column_max_width[column_name], 1), pad=(1, 1), justification="center", do_not_clear=True, disabled=True)
            )
        data_layout = [header_layout]
        for index, row in self.__data.data.items():
            row_layout = []
            row_layout.append(sg.In(f"{index}", size=(column_max_width["Lp."], 1), pad=(1, 1), justification="center", do_not_clear=True, disabled=True))
            for column_name in self.__data.columns_headers:
                row_layout.append(sg.In(row[column_name], size=(column_max_width[column_name], 1), pad=(1, 1), justification="center", key=(index, column_name), do_not_clear=True))
            data_layout.append(row_layout)
        return data_layout

    def create_layout(self, **kwargs) -> List[List[sg.InputText]]:
        index_number = len(self.__data.data)
        scrol = False
        if index_number >= 10:
            scrol = True
        layout = [
            [
                sg.Button("Wczytaj dane z pliku TXT"),
                sg.Button("Zapisz dane do pliku TXT"),
                sg.Button("Zamknij"),
            ],
            [sg.Column(self.get_gui_layout(), scrollable=scrol)],
        ]
        return layout

    def show_gui(self, **kwargs) -> None:
        for key, value in kwargs.items(): 
            print("%s == %s" %(key, value))
        window = sg.Window("Integracja Systemów - Błażej Łach", self.create_layout())
        while True:
            event, values = window.read()
            if event is None or event == "Zamknij":
                break
            if event == "Wczytaj dane z pliku TXT":
                self.__data.read_data()
                window.close()
                window = sg.Window("Integracja Systemów - Błażej Łach", self.create_layout())
            if event == "Zapisz dane do pliku TXT":
                self.__data.udate_data(values)
                self.__data.save_data()
                sg.Popup('Zapisano dane.') 

        window.close()