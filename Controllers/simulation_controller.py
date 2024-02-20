import cv2
from UI_Design.simulation_screen import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QFileDialog
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap

from enums import Pages

class SimulationController(QMainWindow):
    def __init__(self, router: QStackedWidget):
        super(SimulationController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        # add your event listeners here
        self.ui.DashboardButton.clicked.connect(self.go_dashboard)
        self.ui.LogReportButton.clicked.connect(self.go_logReport)
        self.ui.ManualinspectionBox.currentIndexChanged.connect(self.go_manual_inspection)

    def go_dashboard(self):
        self.router.setCurrentIndex(Pages.DASHBOARD.value)

    def go_logReport(self):
        self.router.setCurrentIndex(Pages.LOG.value)

    def go_manual_inspection(self):
        selected_option = self.ui.ManualinspectionBox.currentText()
        self.ui.ManualinspectionBox.setCurrentIndex(0)

        if selected_option == 'Latex Glove':
            print("1")
            self.router.setCurrentIndex(Pages.MANUAL_INSPECTION.value)