from PyQt5.QtWidgets import (
    QWidget,
    QTableView,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QApplication,
    QMessageBox,
)
from PyQt5.QtCore import Qt
from src.common.dataset import Dataset
from src.common.table_model import TableModel


class Window(QWidget):
    def __init__(self, data: Dataset, *args, **kwargs):
        self.__data = data
        self.__read_db = False
        self.__write_db = False
        self.__use_xml = False
        self.__label_source_variable = QLabel()
        self.__label_source_variable.setText("Brak")
        self.__label_source_variable.setAlignment(Qt.AlignLeft)
        for key, value in kwargs.items():
            if key == "read_db" and value:
                self.__read_db = value
            if key == "write_db" and value:
                self.__write_db = value
            if key == "use_xml" and value:
                self.__use_xml = value
        QWidget.__init__(self, *args)
        self.setWindowTitle("Integracja Systemów - Błażej Łach")
        self.__table_view = QTableView()
        self.__update_table_view()
        layout = QVBoxLayout(self)
        layout.addLayout(self.__get_buttons_layout())
        layout.addWidget(self.__table_view)
        self.setLayout(layout)

    def __get_buttons_layout(self):
        btn_read = QPushButton("Wczytaj dane z pliku TXT", self)
        btn_save = QPushButton("Zapisz dane do pliku TXT", self)
        btn_exit = QPushButton("Zamknij", self)

        label_source_name = QLabel()
        label_source_name.setText("Źródło danych: ")
        label_source_name.setAlignment(Qt.AlignRight)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(btn_read)
        btn_read.clicked.connect(self.__click_read)
        buttons_layout.addWidget(btn_save)
        btn_save.clicked.connect(self.__click_save)

        if self.__read_db:
            btn_import_db = QPushButton("Import z bazy danych", self)
            buttons_layout.addWidget(btn_import_db)
            btn_import_db.clicked.connect(self.__click_import_db)
        if self.__write_db:
            btn_export_db = QPushButton("Export do bazy danych", self)
            buttons_layout.addWidget(btn_export_db)
            btn_export_db.clicked.connect(self.__click_export_db)
        if self.__use_xml:
            btn_import_xml = QPushButton("Import danych z XML", self)
            buttons_layout.addWidget(btn_import_xml)
            btn_import_xml.clicked.connect(self.__click_import_xml)
            btn_export_xml = QPushButton("Export danych do XML", self)
            buttons_layout.addWidget(btn_export_xml)
            btn_export_xml.clicked.connect(self.__click_export_xml)

        buttons_layout.addWidget(btn_exit)
        btn_exit.clicked.connect(self.close)

        buttons_layout.addWidget(label_source_name)
        buttons_layout.addWidget(self.__label_source_variable)
        return buttons_layout

    def __update_table_view(self):
        if self.__write_db and not self.__label_source_variable.text() == "Brak":
            reference_data = Dataset()
            reference_data.read_data_db()
            table_model = TableModel(self, self.__data, reference_data=reference_data)
        else:
            table_model = TableModel(self, self.__data)
        self.__table_view.setModel(table_model)
        self.__table_view.resizeColumnsToContents()

    def __click_read(self):
        self.__data.read_data()
        self.__label_source_variable.setText("TXT")
        self.__update_table_view()

    def __click_save(self):
        self.__data.save_data()
        QMessageBox().warning(
            self, "Komunikat", "Zapisano do pliku tekstowego", QMessageBox.Ok
        )
        self.__update_table_view()

    def __click_import_db(self):
        self.__data.read_data_db()
        self.__label_source_variable.setText("DB")
        self.__update_table_view()

    def __click_export_db(self):
        self.__data.save_data_db()
        QMessageBox().warning(
            self, "Komunikat", "Zapisano do bazy danych", QMessageBox.Ok
        )
        self.__update_table_view()

    def __click_import_xml(self):
        self.__data.read_data_xml()
        self.__label_source_variable.setText("XML")
        self.__update_table_view()

    def __click_export_xml(self):
        self.__data.save_data_xml()
        QMessageBox().warning(
            self, "Komunikat", "Zapisano do pliku XML", QMessageBox.Ok
        )
        self.__update_table_view()

