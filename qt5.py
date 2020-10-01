# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt5.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 770)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_project_item_name = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_project_item_name.setFont(font)
        self.label_project_item_name.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_project_item_name.setObjectName("label_project_item_name")
        self.verticalLayout_2.addWidget(self.label_project_item_name)
        self.splitter_3 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_item_image = QtWidgets.QLabel(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_item_image.sizePolicy().hasHeightForWidth())
        self.label_item_image.setSizePolicy(sizePolicy)
        self.label_item_image.setText("")
        # self.label_item_image.setPixmap(QtGui.QPixmap(BASE_DIR + "\\messageImage_1600330717366.jpg"))
        # self.label_item_image.setScaledContents(True)
        self.label_item_image.setObjectName("label_item_image")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.tableWidget_project_item = QtWidgets.QTableWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_project_item.sizePolicy().hasHeightForWidth())
        self.tableWidget_project_item.setSizePolicy(sizePolicy)
        self.tableWidget_project_item.setObjectName("tableWidget_project_item")
        self.tableWidget_project_item.setColumnCount(0)
        self.tableWidget_project_item.setRowCount(0)
        self.label_gonogo = QtWidgets.QLabel(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_gonogo.sizePolicy().hasHeightForWidth())
        self.label_gonogo.setSizePolicy(sizePolicy)
        self.label_gonogo.setObjectName("label_gonogo")
        self.label_gonogo.setScaledContents(True)
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_project_name = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_project_name.setFont(font)
        self.label_project_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_project_name.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_project_name.setObjectName("label_project_name")
        self.verticalLayout.addWidget(self.label_project_name)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableWidget_measure = QtWidgets.QTableWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_measure.sizePolicy().hasHeightForWidth())
        self.tableWidget_measure.setSizePolicy(sizePolicy)
        self.tableWidget_measure.setObjectName("tableWidget_measure")
        self.tableWidget_measure.setColumnCount(0)
        self.tableWidget_measure.setRowCount(0)
        # -------------------------------------------------------
        # self.label_5 = QtWidgets.QLabel(self.splitter)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.splitter.addWidget(self.canvas)  # 更改處
        # -------------------------------------------------------
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.hasHeightForWidth())
        # self.label_5.setSizePolicy(sizePolicy)
        # self.label_5.setText("")
        # self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/螢幕擷取畫面 2020-09-17 163652.png"))
        # self.label_5.setScaledContents(True)
        # self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.splitter)
        self.gridLayout.addWidget(self.splitter_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_project_item_name.setText(_translate("MainWindow", "量測項目："))
        self.label_gonogo.setText(_translate("MainWindow", "GONOGO"))
        self.label_project_name.setText(_translate("MainWindow", "量測專案："))




class Ui_widget_projectcheck(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(678, 607)
        self.gridLayout_2 = QtWidgets.QGridLayout(widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(17, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 5, 1, 1)
        self.lineEdit_now_project_name = QtWidgets.QLineEdit(widget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.lineEdit_now_project_name.setFont(font)
        self.lineEdit_now_project_name.setObjectName("lineEdit_now_project_name")
        self.gridLayout.addWidget(self.lineEdit_now_project_name, 7, 2, 1, 3)
        self.pushButton_cinfirm_project = QtWidgets.QPushButton(widget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.pushButton_cinfirm_project.setFont(font)
        self.pushButton_cinfirm_project.setObjectName("pushButton_cinfirm_project")
        self.gridLayout.addWidget(self.pushButton_cinfirm_project, 7, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 7, 7, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 10, 1, 1)
        self.tableWidget_project = QtWidgets.QTableWidget(widget)
        self.tableWidget_project.setObjectName("tableWidget_project")
        self.tableWidget_project.setColumnCount(0)
        self.tableWidget_project.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_project, 1, 0, 1, 11)
        self.label = QtWidgets.QLabel(widget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.tableWidget_measureitem = QtWidgets.QTableWidget(widget)
        self.tableWidget_measureitem.setObjectName("tableWidget_measureitem")
        self.tableWidget_measureitem.setColumnCount(0)
        self.tableWidget_measureitem.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_measureitem, 6, 0, 1, 11)
        self.label_2 = QtWidgets.QLabel(widget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 4)
        self.pushButton_close = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 7, 9, 1, 2)
        self.pushButton_rest_project = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rest_project.sizePolicy().hasHeightForWidth())
        self.pushButton_rest_project.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.pushButton_rest_project.setFont(font)
        self.pushButton_rest_project.setObjectName("pushButton_rest_project")
        self.gridLayout.addWidget(self.pushButton_rest_project, 0, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(widget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 2)
        self.tableWidget_work_order = QtWidgets.QTableWidget(widget)
        self.tableWidget_work_order.setObjectName("tableWidget_work_order")
        self.tableWidget_work_order.setColumnCount(0)
        self.tableWidget_work_order.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_work_order, 3, 0, 1, 11)
        self.label_4 = QtWidgets.QLabel(widget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "無線量具測試"))
        self.pushButton_cinfirm_project.setText(_translate("widget", "選擇量測專案 \n"
                                                                     " Confirm project"))
        self.label.setText(_translate("widget", "1. 量測專案 \n"
                                                " Measurement project"))
        self.label_2.setText(_translate("widget", "3. 量測項目 \n"
                                                  " Measurement items"))
        self.pushButton_close.setText(_translate("widget", "離開 \n"
                                                           " Exit"))
        self.pushButton_rest_project.setText(_translate("widget", "重新整理專案 \n"
                                                                  " Reimport the project"))
        self.label_3.setText(_translate("widget", "已選擇量測專案名稱  \n"
                                                  " Selected  project name"))
        self.label_4.setText(_translate("widget", "2. 專案工單 \n"
                                                  " work order"))

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(682, 643)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 571, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(BASE_DIR + "\\mp_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 140, 641, 116))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(200, 270, 281, 343))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tool_test = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_test.sizePolicy().hasHeightForWidth())
        self.tool_test.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.tool_test.setFont(font)
        self.tool_test.setObjectName("tool_test")
        self.verticalLayout_2.addWidget(self.tool_test)
        self.start_measure = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_measure.sizePolicy().hasHeightForWidth())
        self.start_measure.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.start_measure.setFont(font)
        self.start_measure.setObjectName("start_measure")
        self.verticalLayout_2.addWidget(self.start_measure)
        self.syste_setting = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.syste_setting.sizePolicy().hasHeightForWidth())
        self.syste_setting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.syste_setting.setFont(font)
        self.syste_setting.setObjectName("syste_setting")
        self.verticalLayout_2.addWidget(self.syste_setting)
        self.excit = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excit.sizePolicy().hasHeightForWidth())
        self.excit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.excit.setFont(font)
        self.excit.setObjectName("excit")
        self.verticalLayout_2.addWidget(self.excit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "生產線上雲端管理系統 - 無線量測系統"))
        self.label_2.setText(_translate("Form", "無線量測品管暨雲端可視化系統 - 品管量測端"))
        self.label_3.setText(_translate("Form", "Wireless Measure and quality Control System"))
        self.label_4.setText(_translate("Form", " with Cloud Visualization Integration-Client"))
        self.tool_test.setText(_translate("Form", "無線量具測試\n"
"Wireless measuring tool test"))
        self.start_measure.setText(_translate("Form", "開始量測\n"
"Start measurement"))
        self.syste_setting.setText(_translate("Form", "系統設定\n"
"system setting"))
        self.excit.setText(_translate("Form", "離開系統\n"
"Exit System"))

class Ui_toolcheck(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(686, 587)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(9, 9, 661, 561))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Button_tool_connect = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_tool_connect.sizePolicy().hasHeightForWidth())
        self.Button_tool_connect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Button_tool_connect.setFont(font)
        self.Button_tool_connect.setObjectName("Button_tool_connect")
        self.gridLayout.addWidget(self.Button_tool_connect, 1, 2, 1, 1)
        self.Button_tool_connect_rest = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_tool_connect_rest.sizePolicy().hasHeightForWidth())
        self.Button_tool_connect_rest.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Button_tool_connect_rest.setFont(font)
        self.Button_tool_connect_rest.setObjectName("Button_tool_connect_rest")
        self.gridLayout.addWidget(self.Button_tool_connect_rest, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_comname = QtWidgets.QComboBox(self.widget)
        self.comboBox_comname.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_comname.sizePolicy().hasHeightForWidth())
        self.comboBox_comname.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_comname.setFont(font)
        self.comboBox_comname.setObjectName("comboBox_comname")
        self.gridLayout.addWidget(self.comboBox_comname, 0, 1, 1, 1)
        self.comboBox_tool_mount = QtWidgets.QComboBox(self.widget)
        self.comboBox_tool_mount.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_tool_mount.sizePolicy().hasHeightForWidth())
        self.comboBox_tool_mount.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_tool_mount.setFont(font)
        self.comboBox_tool_mount.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.comboBox_tool_mount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_tool_mount.setAutoFillBackground(False)
        self.comboBox_tool_mount.setPlaceholderText("")
        self.comboBox_tool_mount.setObjectName("comboBox_tool_mount")
        self.comboBox_tool_mount.addItem("")
        self.comboBox_tool_mount.addItem("")
        self.comboBox_tool_mount.addItem("")
        self.comboBox_tool_mount.addItem("")
        self.gridLayout.addWidget(self.comboBox_tool_mount, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(30, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_5.addWidget(self.pushButton_9, 1, 5, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_5.addWidget(self.pushButton_10, 0, 5, 1, 1)
        self.lineEdit_toolname = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.lineEdit_toolname.setFont(font)
        self.lineEdit_toolname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_toolname.setReadOnly(False)
        self.lineEdit_toolname.setObjectName("lineEdit_toolname")
        self.gridLayout_5.addWidget(self.lineEdit_toolname, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 4, 1, 1)
        self.lineEdit_toolvalue = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.lineEdit_toolvalue.setFont(font)
        self.lineEdit_toolvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_toolvalue.setReadOnly(False)
        self.lineEdit_toolvalue.setObjectName("lineEdit_toolvalue")
        self.gridLayout_5.addWidget(self.lineEdit_toolvalue, 1, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Button_tool_connect.setText(_translate("Form", "量具連結\n"
                                                            "Measuring Tool Confirmation"))
        self.Button_tool_connect_rest.setText(_translate("Form", "量具重新連結\n"
                                                                 "Measuring Tool Relink"))
        self.label_2.setText(_translate("Form", "連接量具數量\n"
                                                "Measuretool "))
        self.label.setText(_translate("Form", "連接埠&裝置名稱\n"
                                              "COM&Device name"))
        self.comboBox_tool_mount.setItemText(0, _translate("Form", "1"))
        self.comboBox_tool_mount.setItemText(1, _translate("Form", "2"))
        self.comboBox_tool_mount.setItemText(2, _translate("Form", "3"))
        self.comboBox_tool_mount.setItemText(3, _translate("Form", "4"))
        self.pushButton_9.setText(_translate("Form", "離開重設量具\n"
                                                     "Exit reconnect "))
        self.pushButton_10.setText(_translate("Form", "量具設定確認\n"
                                                      "Gage setting confirmation"))
        self.label_12.setText(_translate("Form", "裝置名稱\n"
                                                 "Device name"))
        self.label_11.setText(_translate("Form", "量測數值\n"
                                                 "Measurement Value"))
        self.label_10.setText(_translate("Form", "2. 量具測試\n"
                                                 "     Measuring Tool Connection"))
        self.label_5.setText(_translate("Form", "1. 量測設定檢查\n"
                                                "     Measurement setting check"))


class Ui_check(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(309, 209)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 1, 1, 3)
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 4, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.pushButton_setup = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_setup.sizePolicy().hasHeightForWidth())
        self.pushButton_setup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        self.pushButton_setup.setFont(font)
        self.pushButton_setup.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_setup.setObjectName("pushButton_setup")
        self.gridLayout.addWidget(self.pushButton_setup, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        self.pushButton_exit = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout.addWidget(self.pushButton_exit, 6, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(8, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(8, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(8, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 5, 1, 1, 3)
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "量測方式選擇"))
        self.radioButton.setText(_translate("Form", "依照零件部位"))
        self.radioButton_2.setText(_translate("Form", "依照件數"))
        self.pushButton_setup.setText(_translate("Form", "設定完成 \n"
                                                         " Set up"))
        self.pushButton_exit.setText(_translate("Form", "離開 \n"
                                                        " exit"))
        self.label.setText(_translate("Form", "選擇量測方式"))
