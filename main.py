import os
import sys

from UI_Design.Main_Dashboard import *

from PyQt5.QtWidgets import QApplication, QMainWindow

## Main Window Class
class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyMainWindow()
    window.show()

    sys.exit(app.exec_())