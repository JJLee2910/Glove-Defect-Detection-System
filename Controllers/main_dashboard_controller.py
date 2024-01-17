from UI_Design.Main_Dashboard import *
from UI_Design.test import *
from Controllers.manual_inspection_controller import ManualInspectionController
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QGraphicsView, QGraphicsScene, QVBoxLayout
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import QBarSet, QBarSeries, QChart, QBarCategoryAxis, QChartView, QValueAxis

class MainDashboardController(QMainWindow):
    def __init__(self, router):
        super(MainDashboardController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        # Load your data from the CSV file (adjust the path accordingly)
        csv_path = 'Database\\data.csv'
        self.data = pd.read_csv(csv_path, parse_dates=['Date'], dayfirst=True)

        # Create a chart and add it to the layout
        self.chart = self.create_defect_count_chart()
        chart_view = QChartView(self.chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.ui.gridLayout.addWidget(chart_view)

        # add your event listeners here
        self.ui.ManualinspectionBox.currentIndexChanged.connect(self.switch_manual_inspection_screen)

    def switch_manual_inspection_screen(self):
        selected_option = self.ui.ManualinspectionBox.currentText()
        self.ui.ManualinspectionBox.setCurrentIndex(0)

        if selected_option == "Latex Glove":
            print("1")
            self.router.setCurrentIndex(1)

    def create_defect_count_chart(self):
        chart = QChart()

        # Get unique defect types
        defect_types = self.data['Type of Defect'].unique()

        # Create a bar set for each type of defect
        bar_set = QBarSet("Defect Count")

        # Count occurrences of each defect type
        defect_counts = self.data['Type of Defect'].value_counts()

        # Add data to the bar set
        for defect_type in defect_types:
            count = defect_counts.get(defect_type, 0)
            bar_set.append(count)

        # Create a bar series and add the bar set to it
        bar_series = QBarSeries()
        bar_series.append(bar_set)
        chart.addSeries(bar_series)

        # Configure the x-axis with QBarCategoryAxis
        x_axis = QBarCategoryAxis()
        x_axis.append(defect_types)
        chart.addAxis(x_axis, Qt.AlignBottom)

        # Configure the y-axis with QValueAxis
        y_axis = QValueAxis()
        y_axis.setTitleText("Count")
        chart.addAxis(y_axis, Qt.AlignLeft)

        # Attach the axes to the series
        bar_series.attachAxis(x_axis)
        bar_series.attachAxis(y_axis)

        return chart