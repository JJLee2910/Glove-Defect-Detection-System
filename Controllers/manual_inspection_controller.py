import cv2
from Detectors.silicone.dirt_detector import DirtDetector
# from Detectors.latex.latex_dirt_detector import DirtDetector
from UI_Design.manual_inspection_screen import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QFileDialog
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap

from enums import Pages

class ManualInspectionController(QMainWindow):
    def __init__(self, router: QStackedWidget):
        super(ManualInspectionController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        # add your event listeners here
        self.ui.DashboardButton.clicked.connect(self.go_dashboard)
        self.ui.AddImageBtn.clicked.connect(self.add_image)
        self.ui.StartDetectionBtn.clicked.connect(self.start_detection)

    def go_dashboard(self):
        self.router.setCurrentIndex(Pages.DASHBOARD.value)
        
    def add_image(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg *.jpeg)')
            if not filename:
                return
            
        self.image_filename = filename
        self.ui.PictureLabel.setPixmap(QPixmap(filename))

    def start_detection(self):
        img = cv2.imread(self.image_filename)
        DirtDetector(img).detect()
        