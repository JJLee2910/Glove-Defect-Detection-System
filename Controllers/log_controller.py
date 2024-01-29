from Controllers.main_dashboard_controller import *
from UI_Design.log import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget
from enums import Pages

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
        self.ui.ManualinspectionBox.currentIndexChanged.connect(self.switch_manual_inspection_screen)
        self.ui.SimulationButton.clicked.connect(self.switch_simulation_screen)

    def go_dashboard(self):
        self.router.setCurrentIndex(Pages.DASHBOARD.value)

    def switch_manual_inspection_screen(self):
        selected_option = self.ui.ManualinspectionBox.currentText()
        self.ui.ManualinspectionBox.setCurrentIndex(0)

        if selected_option == "Latex Glove":
            print("1")
            self.router.setCurrentIndex(Pages.MANUAL_INSPECTION.value)

    def switch_simulation_screen(self):
        if self.ui.SimulationButton.isChecked() == False:
            print("3")
