from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtGui import QColor


class TableModel(QAbstractTableModel):
    def __init__(self, parent, data, *args, **kwargs):
        QAbstractTableModel.__init__(self, parent, *args)
        self.__data = data
        self.__reference_data = None
        for key, value in kwargs.items():
            if key == "reference_data":
                self.__reference_data = value

    def rowCount(self, parent):
        return len(self.__data.data)

    def columnCount(self, parent):
        return len(self.__data.columns_headers)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def data(self, index, role):
        row = str(index.row() + 1)
        column = self.__data.columns_headers[index.column()]
        if not index.isValid():
            return None
        elif role == Qt.DisplayRole or role == Qt.EditRole:
            return self.__data.data[row][column]
        elif role == Qt.BackgroundColorRole and self.__reference_data is not None:
            if (
                not self.__data.data[row][column]
                == self.__reference_data.data[row][column]
            ):
                return QVariant(QColor(Qt.red))
            else:
                return QVariant(QColor(Qt.white))
        else:
            return None

    def headerData(self, col, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.__data.columns_headers[col]
            if orientation == Qt.Vertical:
                return str(col + 1)
        return None

    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if role != Qt.EditRole:
            return False
        row = index.row()
        if row < 0 or row >= len(self.__data.data):
            return False
        column = index.column()
        if column < 0 or column >= len(self.__data.columns_headers):
            return False
        row = str(index.row() + 1)
        column = self.__data.columns_headers[index.column()]
        self.__data.data[row][column] = value
        self.dataChanged.emit(index, index)
        return True
