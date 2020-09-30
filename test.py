# from PyQt5 import QtWidgets
# from pyqtgraph import PlotWidget, plot
# import pyqtgraph as pg
# import sys  # We need sys so that we can pass argv to QApplication
# import os
#
# class MainWindow(QtWidgets.QMainWindow):
#
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#
#         self.graphWidget = pg.PlotWidget()
#         self.setCentralWidget(self.graphWidget)
#
#         hour = [1,2,3,4,5,6,7,8,9,10]
#         temperature = [30,32,34,32,33,31,29,32,35,45]
#
#         # plot data: x, y values
#         self.graphWidget.plot(hour, temperature)
#
#
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     main = MainWindow()
#     main.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()

import matplotlib.font_manager

a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

for i in a:
    print(i)
# import sys
# from MyMplCanvas import MyStaticMplCanvas, MyDynamicMplCanvas
# from PyQt5.QtWidgets import QMainWindow, QMenu, QWidget, QMessageBox,\
#     QApplication, QVBoxLayout
# from PyQt5.QtCore import Qt
#
#
# class ApplicationWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.setAttribute(Qt.WA_DeleteOnClose)
#         self.setWindowTitle("application main window")
#
#         self.file_menu = QMenu('&File', self)
#         self.file_menu.addAction('&Quit', self.fileQuit,
#                                  Qt.CTRL + Qt.Key_Q)
#         self.menuBar().addMenu(self.file_menu)
#
#         self.help_menu = QMenu('&Help', self)
#         self.menuBar().addSeparator()
#         self.menuBar().addMenu(self.help_menu)
#
#         self.help_menu.addAction('&About', self.about)
#
#         self.main_widget = QWidget(self)
#
#         l = QVBoxLayout(self.main_widget)
#         sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
#         dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
#         l.addWidget(sc)
#         l.addWidget(dc)
#
#         self.main_widget.setFocus()
#         self.setCentralWidget(self.main_widget)
#
#         self.statusBar().showMessage("All hail matplotlib!", 2000)
#
#     def fileQuit(self):
#         self.close()
#
#     def closeEvent(self, ce):
#         self.fileQuit()
#
#     def about(self):
#         QtWidgets.QMessageBox.about(self, "About",
#                                     """embedding_in_qt5.py example
# Copyright 2005 Florent Rougon, 2006 Darren Dale, 2015 Jens H Nielsen
# This program is a simple example of a Qt5 application embedding matplotlib
# canvases.
# It may be used and modified with no restriction; raw copies as well as
# modified versions may be distributed without limitation.
# This is modified from the embedding in qt4 example to show the difference
# between qt4 and qt5""")
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = ApplicationWindow()
#     win.show()
#     sys.exit(app.exec())
