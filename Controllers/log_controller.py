from Controllers.main_dashboard_controller import DefectDAO
from Controllers.my_main_window import MyMainWindow
from UI_Design.log import *
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QTableWidgetItem,
)
from PyQt5.QtCore import Qt
from app_data import AppData
from enums import Pages


class LogController(MyMainWindow):

    def __init__(self, *args, **kwargs):
        ui = Ui_MainWindow()
        super(LogController, self).__init__(ui, *args, **kwargs)

        self.defectDao = DefectDAO()
        self.data = self.defectDao.get_data()
        self.displayTableInfo()

    def displayTableInfo(self):
        self.ui.logTable.setRowCount(self.data.shape[0])
        self.ui.logTable.setColumnCount(self.data.shape[1])

        for row_index, row_data in enumerate(self.data.values):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setFlags(
                    item.flags() ^ Qt.ItemIsEditable
                )  # set item uneditable in table
                self.ui.logTable.setItem(row_index, col_index, item)

        self.ui.logTable.setHorizontalHeaderLabels(self.data.columns)
