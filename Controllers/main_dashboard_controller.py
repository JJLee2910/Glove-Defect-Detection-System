from UI_Design.Main_Dashboard import *
from UI_Design.test import *
from Controllers.manual_inspection_controller import ManualInspectionController
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QGraphicsView, QGraphicsScene, QVBoxLayout
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import QLineSeries, QDateTimeAxis, QValueAxis, QChart, QChartView, QBarSet, QBarSeries


class MainDashboardController(QMainWindow):
    def __init__(self, router: QStackedWidget):
        super(MainDashboardController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router

        self.chart = QChart()
        series = QBarSeries()
        set0 = QBarSet("Series 1")
        set0.append([1, 2, 3, 4, 5])  # Sample data for the chart
        series.append(set0)
        self.chart.addSeries(series)

        chart_view = QChartView(self.chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.ui.gridLayout.addWidget(chart_view)

        # Add your event listeners here
        self.ui.ManualinspectionBox.currentIndexChanged.connect(self.switch_manual_inspection_screen)

        # add your event listeners here
        self.ui.ManualinspectionBox.currentIndexChanged.connect(self.switch_manual_inspection_screen)


    def switch_manual_inspection_screen(self):
        selected_option = self.ui.ManualinspectionBox.currentText()
        self.ui.ManualinspectionBox.setCurrentIndex(0)

        if selected_option == "Latex Glove":
            print("1")
            self.router.setCurrentIndex(1)
    

    # def create_time_series_chart(self):
    #     csv_path = "Database\\data.csv"

    #     try:
    #         # Load data from CSV using pandas
    #         df = pd.read_csv(csv_path)

    #         # Convert the 'date' column to datetime format
    #         df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

    #         grouped_df = df.groupby(['Date', 'Type of Defect']).size().reset_index(name='Count').rename(columns={0: 'Count'})

    #         # Get unique types of defects
    #         unique_defects = df['Type of Defect'].unique()

    #         # Create a chart
    #         unique_defects = grouped_df['Type of Defect'].unique()

    #         # Create a chart
    #         chart = QChart()
    #         # chart.setTitle("Time Series Chart")

    #         # Create and add line series for each type of defect
    #         for defect_type in unique_defects:
    #             series = QLineSeries()
    #             series.setName(defect_type)

    #             # Filter dataframe for the current defect type
    #             filtered_df = grouped_df[grouped_df['Type of Defect'] == defect_type]

    #             # Add data points to the series
    #             for index, row in filtered_df.iterrows():
    #                 series.append(row['Date'].timestamp() * 1000, row['Count'])

    #             chart.addSeries(series)

    #         # Configure axes
    #         axis_x = QDateTimeAxis()
    #         axis_x.setFormat("yyyy-MM-dd")  # Set the date format as needed
    #         chart.addAxis(axis_x, Qt.AlignBottom)

    #         axis_y = QValueAxis()
    #         chart.addAxis(axis_y, Qt.AlignLeft)

    #         # Attach axes to series
    #         for series in chart.series():
    #             series.attachAxis(axis_x)
    #             series.attachAxis(axis_y)

    #         # Create chart view
    #         chart_view = QChartView(chart)
    #         chart_view.setRenderHint(QPainter.Antialiasing)

    #         # Clear existing layout if any
    #         # Check if layout is already set
    #         if self.chart.layout() is None:
    #             # Set the chart view as the central widget
    #             layout = QVBoxLayout(self.chart)
    #             layout.addWidget(chart_view)

    #     except FileNotFoundError:
    #         print(f"Error: File '{csv_path}' not found.")
    #     except pd.errors.EmptyDataError:
    #         print(f"Error: File '{csv_path}' is empty.")
    #     except Exception as e:
    #         print(f"An error occurred: {e}")