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
        self.ui.startButton.clicked.connect(self.start_simulation)
        self.ui.stopButton.clicked.connect(self.stop_simulation)

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

    def start_simulation(self):
        if not (self.in_simulation):
            self.in_simulation = True
            
            input_image_list = self.get_input_image(self)

            for file in input_image_list:
                self.set_screen_image(self, file)
                
                # perform inspection based on glove type
                if (file.name.startswith('cloth')):
                    pass
                elif (file.name.startswith('latex')):
                    pass
                elif (file.name.startswith('silicone')):
                    pass

                # Add img to output
                # 

    def stop_simulation(self):
        if (self.in_simulation):
            self.in_simulation = False
    
    # return a list of file
    def get_input_image(self):
        folder_path = 'Glove-Defect-Detection-System\Simulation_IO\input'
        folder = Path(folder_path)
        files = [file for file in folder.iterdir() if file.is_file]
        return files

    def set_screen_image(self, img):
        self.ui.gloveImage.setPixelMap(QtGui.QPixmap(img))