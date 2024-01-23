from Controllers.main_dashboard_controller import *
from UI_Design.log import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget
class LogController(QMainWindow):

    def __init__(self, router):
        super(LogController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        self.defectDao = DefectDAO()
        self.data = self.defectDao.get_data()

        #
        self.ui.DashboardButton.clicked.connect(self.go_dashboard)

    def go_dashboard(self):
        print("0")
        self.router.setCurrentIndex(0)
