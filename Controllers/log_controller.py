from Controllers.main_dashboard_controller import DefectDAO
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


class LogController(QMainWindow):

    def __init__(self, router):
        super(LogController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        self.defectDao = DefectDAO()
        self.data = self.defectDao.get_data()

        # print("Data in LogController:")
        # print(self.data.head())

        self.ui.DashboardButton.clicked.connect(self.go_dashboard)
        self.ui.ManualinspectionBox.currentIndexChanged.connect(
            self.switch_manual_inspection_screen
        )
        self.ui.SimulationButton.clicked.connect(self.switch_simulation_screen)

        self.displayTableInfo()

    def go_dashboard(self):
        self.router.setCurrentIndex(Pages.DASHBOARD.value)

    def switch_manual_inspection_screen(self):
        data = AppData()
        selected_option = self.ui.ManualinspectionBox.currentText()

        # setup current Screen
        self.ui.ManualinspectionBox.setCurrentIndex(0)

        # setup Manual Inspection Screen
        data._instance.manual_inspection_page.ui.title_label_6.setText(
            f"Manual Inspection for {selected_option}"
        )

        # setup router
        self.router.setCurrentIndex(Pages.MANUAL_INSPECTION.value)

        # setup app data
        data.manual_inspection_glove_type = selected_option

    def switch_simulation_screen(self):
        if self.ui.SimulationButton.isChecked() == False:
            print("3")
            self.router.setCurrentIndex(Pages.SIMULATION_INSPECTION.value)

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
