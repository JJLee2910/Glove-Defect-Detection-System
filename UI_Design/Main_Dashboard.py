# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 701)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(996, 701))
        MainWindow.setMaximumSize(QtCore.QSize(996, 701))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(996, 701))
        self.centralwidget.setMaximumSize(QtCore.QSize(996, 701))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu_frame = QtWidgets.QFrame(self.centralwidget)
        self.side_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_frame.setObjectName("side_menu_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.side_menu_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo_label_frame = QtWidgets.QFrame(self.side_menu_frame)
        self.logo_label_frame.setMinimumSize(QtCore.QSize(100, 100))
        self.logo_label_frame.setMaximumSize(QtCore.QSize(500, 100))
        self.logo_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_label_frame.setObjectName("logo_label_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.logo_label_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label = QtWidgets.QLabel(self.logo_label_frame)
        self.logo_label.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap(":/Images/icons/Logo-APU-200.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.horizontalLayout_2.addWidget(self.logo_label)
        self.APU_Glove_Detection_System_label = QtWidgets.QLabel(self.logo_label_frame)
        self.APU_Glove_Detection_System_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.APU_Glove_Detection_System_label.sizePolicy().hasHeightForWidth())
        self.APU_Glove_Detection_System_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.APU_Glove_Detection_System_label.setFont(font)
        self.APU_Glove_Detection_System_label.setObjectName("APU_Glove_Detection_System_label")
        self.horizontalLayout_2.addWidget(self.APU_Glove_Detection_System_label)
        self.verticalLayout.addWidget(self.logo_label_frame)
        self.menu_frame = QtWidgets.QFrame(self.side_menu_frame)
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DashboardButton = QtWidgets.QPushButton(self.menu_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DashboardButton.setFont(font)
        self.DashboardButton.setObjectName("DashboardButton")
        self.verticalLayout_2.addWidget(self.DashboardButton)
        self.LogReportButton = QtWidgets.QPushButton(self.menu_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LogReportButton.setFont(font)
        self.LogReportButton.setObjectName("LogReportButton")
        self.verticalLayout_2.addWidget(self.LogReportButton)
        self.ManualinspectionBox = QtWidgets.QComboBox(self.menu_frame)
        self.ManualinspectionBox.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ManualinspectionBox.setFont(font)
        self.ManualinspectionBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ManualinspectionBox.setEditable(False)
        self.ManualinspectionBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.ManualinspectionBox.setObjectName("ManualinspectionBox")
        self.ManualinspectionBox.addItem("")
        self.ManualinspectionBox.addItem("")
        self.ManualinspectionBox.addItem("")
        self.ManualinspectionBox.addItem("")
        self.ManualinspectionBox.addItem("")
        self.verticalLayout_2.addWidget(self.ManualinspectionBox)
        self.SimulationButton = QtWidgets.QPushButton(self.menu_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SimulationButton.setFont(font)
        self.SimulationButton.setObjectName("SimulationButton")
        self.verticalLayout_2.addWidget(self.SimulationButton)
        self.verticalLayout.addWidget(self.menu_frame)
        self.horizontalLayout.addWidget(self.side_menu_frame)
        self.dashbord_main_frame = QtWidgets.QFrame(self.centralwidget)
        self.dashbord_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashbord_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashbord_main_frame.setObjectName("dashbord_main_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dashbord_main_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chart_frame = QtWidgets.QFrame(self.dashbord_main_frame)
        self.chart_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chart_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chart_frame.setObjectName("chart_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.chart_frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.chart_widget = QtWidgets.QStackedWidget(self.chart_frame)
        self.chart_widget.setObjectName("chart_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.defect_chart_frame = QtWidgets.QFrame(self.page)
        self.defect_chart_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.defect_chart_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.defect_chart_frame.setObjectName("defect_chart_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.defect_chart_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.defect_chart_labe = QtWidgets.QLabel(self.defect_chart_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.defect_chart_labe.setFont(font)
        self.defect_chart_labe.setAlignment(QtCore.Qt.AlignCenter)
        self.defect_chart_labe.setObjectName("defect_chart_labe")
        self.verticalLayout_7.addWidget(self.defect_chart_labe, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_6.addWidget(self.defect_chart_frame, 0, QtCore.Qt.AlignTop)
        self.chart = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart.sizePolicy().hasHeightForWidth())
        self.chart.setSizePolicy(sizePolicy)
        self.chart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chart.setObjectName("chart")
        self.gridLayout = QtWidgets.QGridLayout(self.chart)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6.addWidget(self.chart)
        self.chart_widget.addWidget(self.page)
        self.horizontalLayout_7.addWidget(self.chart_widget)
        self.verticalLayout_3.addWidget(self.chart_frame)
        self.label_info_frame = QtWidgets.QFrame(self.dashbord_main_frame)
        self.label_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_info_frame.setObjectName("label_info_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.label_info_frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.info_frame = QtWidgets.QFrame(self.label_info_frame)
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.info_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.info_label = QtWidgets.QLabel(self.info_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.info_label.setFont(font)
        self.info_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")
        self.verticalLayout_5.addWidget(self.info_label)
        self.horizontalLayout_6.addWidget(self.info_frame)
        self.verticalLayout_3.addWidget(self.label_info_frame)
        self.horizontalLayout.addWidget(self.dashbord_main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.chart_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.APU_Glove_Detection_System_label.setText(_translate("MainWindow", "APU Glove Detection System"))
        self.DashboardButton.setText(_translate("MainWindow", "Dashboard"))
        self.LogReportButton.setText(_translate("MainWindow", "Log Report"))
        self.ManualinspectionBox.setItemText(0, _translate("MainWindow", "Manual Inspection"))
        self.ManualinspectionBox.setItemText(1, _translate("MainWindow", "Latex Glove"))
        self.ManualinspectionBox.setItemText(2, _translate("MainWindow", "Plastic Glove"))
        self.ManualinspectionBox.setItemText(3, _translate("MainWindow", "Silicone Glove"))
        self.ManualinspectionBox.setItemText(4, _translate("MainWindow", "Nitrile Glove"))
        self.SimulationButton.setText(_translate("MainWindow", "Simulation"))
        self.defect_chart_labe.setText(_translate("MainWindow", "Glove Defect Bar Chart"))
        self.info_label.setText(_translate("MainWindow", "Asia Pacific University IPPR Assignment"))
from UI_Design import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
