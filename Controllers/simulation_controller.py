import cv2
from Controllers.my_main_window import MyMainWindow
from UI_Design.simulation_screen import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QFileDialog
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap

from enums import Pages

class SimulationController(MyMainWindow):
    def __init__(self, *args, **kwargs):
        ui = Ui_MainWindow()
        super(SimulationController, self).__init__(ui, *args, **kwargs)

        # add your event listeners here
        self.ui.startButton.clicked.connect(self.start_simulation)
        self.ui.stopButton.clicked.connect(self.stop_simulation)

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