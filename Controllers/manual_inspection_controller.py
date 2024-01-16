from UI_Design.manual_inspection_screen import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget

class ManualInspectionController(QMainWindow):
    def __init__(self, router: QStackedWidget):
        super(ManualInspectionController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        # add your event listeners here
        self.ui.DashboardButton.clicked.connect(self.go_dashboard)

    def go_dashboard(self):
        print("0")
        self.router.setCurrentIndex(0)