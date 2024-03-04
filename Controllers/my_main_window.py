from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QTableWidgetItem,
)
from PyQt5.QtCore import Qt
from Detectors.base import Detector
from app_data import AppData
from enums import Pages
from Detectors import silicone
from settings import type_to_detectors

class MyMainWindow(QMainWindow):
    def __init__(self, ui, router):
        super(MyMainWindow, self).__init__()
        self.ui = ui
        self.ui.setupUi(self)
        self.router = router

        # setup glove types
        self.ui.ManualinspectionBox.clear()
        items = ["Manual Inspection", *list(type_to_detectors.keys())]
        self.ui.ManualinspectionBox.addItems(items)

        # setup event listeners
        self.ui.DashboardButton.clicked.connect(self.go_dashboard)
        self.ui.LogReportButton.clicked.connect(self.switch_log_screen)
        self.ui.ManualinspectionBox.currentIndexChanged.connect(
            self.switch_manual_inspection_screen
        )
        self.ui.SimulationButton.clicked.connect(self.switch_simulation_screen)

    def go_dashboard(self):
        self.router.setCurrentIndex(Pages.DASHBOARD.value)


    def switch_log_screen(self):
        if self.ui.LogReportButton.isChecked() == False:
            print("2")
            self.router.setCurrentIndex(Pages.LOG.value)


    def switch_manual_inspection_screen(self):
        data = AppData()
        selected_option = self.ui.ManualinspectionBox.currentText()
        data.manual_inspection_glove_type = selected_option

        # setup Manual Inspection Screen
        data._instance.manual_inspection_page.ui.title_label_6.setText(
            f"Manual Inspection for {selected_option}"
        )
        detection_combo_box = data._instance.manual_inspection_page.ui.detectionComboBox
        detection_combo_box.clear()
        items = list(type_to_detectors[selected_option].keys())
        detection_combo_box.addItems(items)  # Add the "items" to the detection_combo_box

        # setup router
        self.router.setCurrentIndex(Pages.MANUAL_INSPECTION.value)

        # setup current Screen
        self.ui.ManualinspectionBox.blockSignals(True)
        self.ui.ManualinspectionBox.setCurrentIndex(0)
        self.ui.ManualinspectionBox.blockSignals(False)


    def switch_simulation_screen(self):
        if self.ui.SimulationButton.isChecked() == False:
            print("3")
            self.router.setCurrentIndex(Pages.SIMULATION_INSPECTION.value)