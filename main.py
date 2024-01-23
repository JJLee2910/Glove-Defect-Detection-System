import os
import sys

from Controllers import main_dashboard_controller, manual_inspection_controller, log_controller
from UI_Design.Main_Dashboard import *
from UI_Design.test import *
from Controllers.manual_inspection_controller import ManualInspectionController
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


# Add ur pages here and access by index.
def add_pages(router):
    dashboard_page = main_dashboard_controller.MainDashboardController(router)
    router.addWidget(dashboard_page)

    log_page = log_controller.LogController(router)
    router.addWidget(log_page)

    manual_inspection_page = manual_inspection_controller.ManualInspectionController(router)
    router.addWidget(manual_inspection_page)

    # logReportPage = False # Replace false with log report page connection
    # router.addWidget(logReportPage)

    # simulation_page = False # Replace False with simulation page connection
    # router.addWidget(simulation_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    router = QtWidgets.QStackedWidget()

    add_pages(router)

    router.setGeometry(100, 100, 996, 700)
    router.setCurrentIndex(0)
    router.show()
    sys.exit(app.exec_())