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

    def go_dashboard(self):
        self.router.setCurrentIndex(Pages.DASHBOARD.value)