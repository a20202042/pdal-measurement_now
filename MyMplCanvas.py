from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from numpy import arange, sin, pi, linspace
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    # 这既是一个wiget类也是一个FigureCanva

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        # self.compute_initial_figure()

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        self.compute_initial_figure()

    def compute_initial_figure(self):
        print("hello world")
        x = linspace(0, 2 * pi, 500)
        y = sin(x)
        self.axes.cla()
        self.axes.plot(x, y)
        self.draw()


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)

        timer.timeout.connect(self.update_figure)
        timer.start(100)
        x = linspace(0, 2 * pi, 500)
        y = sin(x)
        self.myaxes, = self.axes.plot(x, y)
        self.__i = 0

    def update_figure(self):
        self.__i += 1
        self.__i %= 50
        begain = self.__i / 50 * 2 * pi
        y = sin(linspace(begain, 2 * pi + begain, 500))
        self.myaxes.set_ydata(y)
        self.draw()