from PyQt5.QtWidgets import (
    QWidget,
    QTableView,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QApplication,
    QMessageBox,
    QComboBox,
)
from PyQt5.QtCore import Qt
from src.common.dataset import Dataset
from src.common.table_model import TableModel
from zeep import Client
from src.common.constants import no_data_value
import json


class ClientWindow(QWidget):
    def __init__(self, data: Dataset, *args, **kwargs):
        QWidget.__init__(self, *args)
        self.__data = data
        self.__client = Client("http://localhost:58585/SelectFromDB/soap/description?WSDL")
        self.__label_count_manufacturer = QLabel()
        self.__label_count_manufacturer.setText("Wybór producenta")
        self.__label_count_manufacturer.setAlignment(Qt.AlignLeft)
        self.__combo_box_count_manufacturer = QComboBox()
        self.__combo_box_count_manufacturer.addItems(self.__client.service.get_manufacturer())
        self.__button_count_manufacturer = QPushButton("Liczba laptopów producenta", self)
        self.__button_count_manufacturer.clicked.connect(self.__click_count)
        self.__label_value_count_manufacturer = QLabel()
        self.__label_value_count_manufacturer.setText("")
        self.__label_value_count_manufacturer.setAlignment(Qt.AlignLeft)
        self.__label_select_screen_type = QLabel()
        self.__label_select_screen_type.setText("Wybór typu matrycy")
        self.__label_select_screen_type.setAlignment(Qt.AlignLeft)
        self.__combo_box_select_screen_type = QComboBox()
        self.__combo_box_select_screen_type.addItems(self.__client.service.get_screen_type())
        self.__button_select_screen_type = QPushButton("Lista laptopów z określonym typem matrycy", self)
        self.__button_select_screen_type.clicked.connect(self.__click_list)
        self.__label_source_variable = QLabel()
        self.__label_source_variable.setText("Brak")
        self.__label_source_variable.setAlignment(Qt.AlignLeft)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.__label_count_manufacturer)
        buttons_layout.addWidget(self.__combo_box_count_manufacturer)
        buttons_layout.addWidget(self.__button_count_manufacturer)
        buttons_layout.addWidget(self.__label_value_count_manufacturer)
        buttons_layout.addWidget(self.__label_select_screen_type)
        buttons_layout.addWidget(self.__combo_box_select_screen_type)
        buttons_layout.addWidget(self.__button_select_screen_type)
        buttons_layout.addWidget(self.__label_source_variable)
        self.setWindowTitle("Integracja Systemów - Aplikacja klienta - Błażej Łach")
        self.__table_view = QTableView()
        self.__update_table_view()
        layout = QVBoxLayout(self)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.__table_view)
        self.setLayout(layout)

    def __click_count(self):
        self.__label_value_count_manufacturer.setText(str(self.__client.service.count_manufacturer(self.__combo_box_count_manufacturer.currentText())))

    def __click_list(self):
        select_item = self.__combo_box_select_screen_type.currentText()
        if select_item == no_data_value():
            select_item = ""
        result = self.__client.service.get_screen_type_data(select_item)
        self.__data.data = json.loads(result)
        self.__label_source_variable.setText("DB")
        self.__update_table_view()

    def __update_table_view(self):
        table_model = TableModel(self, self.__data)
        self.__table_view.setModel(table_model)
        self.__table_view.resizeColumnsToContents()
