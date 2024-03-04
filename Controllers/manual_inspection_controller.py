import cv2
from Controllers.my_main_window import MyMainWindow
from Detectors.silicone.dirt_detector import DirtDetector
from Detectors.latex.latex_dirt_detector import DirtDetectors
from Detectors.cloth.nitrile_missing_finger import MissingFingerDetector
from UI_Design.manual_inspection_screen import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QFileDialog
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap

from enums import Pages

class ManualInspectionController(MyMainWindow):
    def __init__(self, *args, **kwargs):
        ui = Ui_MainWindow()
        super(ManualInspectionController, self).__init__(ui, *args, **kwargs)

        # add your event listeners here
        self.ui.AddImageBtn.clicked.connect(self.add_image)
        self.ui.StartDetectionBtn.clicked.connect(self.start_detection)
        
    def add_image(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg *.jpeg)')
            if not filename:
                return
            
        self.image_filename = filename
        self.ui.PictureLabel.setPixmap(QPixmap(filename))

    def start_detection(self):
        img = cv2.imread(self.image_filename)
        # DirtDetector(img).detect()
        # StainDetector(img).detect()
        DirtDetectors(img).detect()
        # MissingFingerDetector(img).detect()
        