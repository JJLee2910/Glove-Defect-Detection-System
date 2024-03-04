import cv2
from Controllers.my_main_window import MyMainWindow
from UI_Design.manual_inspection_screen import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap

from app_data import AppData
from settings import type_to_detectors
from PyQt5.QtWidgets import QMessageBox

class ManualInspectionController(MyMainWindow):
    def __init__(self, *args, **kwargs):
        ui = Ui_MainWindow()
        super(ManualInspectionController, self).__init__(ui, *args, **kwargs)
        self.image_filename = ""

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
        glove_type = AppData().manual_inspection_glove_type
        detection_type = self.ui.detectionComboBox.currentText()
        
        message_box = None
        if not glove_type:
            print("choose glove la")
            message_box = QMessageBox(QMessageBox.Icon.Critical, "Warning", "Please select a glove type", QMessageBox.Ok, self)
        elif not detection_type:
            print("choose detection la")
            message_box = QMessageBox(QMessageBox.Icon.Critical, "Warning", "Please select a detection type", QMessageBox.Ok, self)
        elif not self.image_filename:
            print("choose image la")
            message_box = QMessageBox(QMessageBox.Icon.Critical, "Warning", "Please select a image", QMessageBox.Ok, self)
        
        if message_box:
            message_box.exec()
            return
        
        img = cv2.imread(self.image_filename)

        detector_cls = type_to_detectors[glove_type][detection_type]

        detector_cls(img).detect()