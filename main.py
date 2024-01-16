import os
import sys

from UI_Design.Main_Dashboard import *
from UI_Design.test import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

## Main Window Class
class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create an instance of the Ui_Form class
        self.test_ui = Ui_Form()
        # Create a QWidget to hold the Ui_Form instance
        self.test_widget = QWidget()

        self.ui.ManualinspectionBox.currentIndexChanged.connect(self.switch_manual_inspection_screen)

    def switch_manual_inspection_screen(self):
        ##to switch between widget without opening the new window
        ## when i select the option of "Latex Gloves" from the combo box, it will changed to the form from test.py
        selected_option = self.ui.ManualinspectionBox.currentText()

        if selected_option == "Latex Glove":
            # Set the central widget to the Ui_Form instance
            self.test_ui.setupUi(self.test_widget)
            self.setCentralWidget(self.test_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyMainWindow()
    window.show()

    sys.exit(app.exec_())