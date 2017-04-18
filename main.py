import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import numpy as np
import os

plt.rcParams.update({'font.size': 18})

class Data_to_plot:
    x = 0
    y = 0
    xlabel = "x"
    ylabel = "y"
    title = ""


class Window(QtWidgets.QMainWindow, Data_to_plot):
    def __init__(self, parent=None):
        super().__init__(parent)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)

        self.button_to_plot = QtWidgets.QPushButton('Plot')
        self.button_to_plot.clicked.connect(self.plot)

        self.button_to_zoom = QtWidgets.QPushButton('Zoom')
        self.button_to_zoom.clicked.connect(self.zoom)

        self.button_to_home = QtWidgets.QPushButton('Home')
        self.button_to_home.clicked.connect(self.home)


        self.button_to_set_xlabel = QtWidgets.QPushButton('Set xlabel')
        self.button_to_set_xlabel.clicked.connect(self.set_xlabel)
        self.text_xlable = QtWidgets.QLineEdit()

        self.button_to_set_ylabel = QtWidgets.QPushButton('Set ylabel')
        self.button_to_set_ylabel.clicked.connect(self.set_ylabel)
        self.text_ylable = QtWidgets.QLineEdit()

        self.button_to_set_title = QtWidgets.QPushButton('Set title')
        self.button_to_set_title.clicked.connect(self.set_title)
        self.text_title = QtWidgets.QLineEdit()

        self.button_to_import_data = QtWidgets.QPushButton('import data x,y')
        self.button_to_import_data.clicked.connect(self.import_data)
        self.textEdit = QtWidgets.QTextEdit()

        # set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        btnlayout1 = QtWidgets.QHBoxLayout()
        btnlayout1.addWidget(self.button_to_plot)
        btnlayout1.addWidget(self.button_to_zoom)
        btnlayout1.addWidget(self.button_to_home)

        btnlayout2 = QtWidgets.QHBoxLayout()
        btnlayout2.addWidget(self.button_to_set_xlabel)
        btnlayout2.addWidget(self.button_to_set_ylabel)
        btnlayout2.addWidget(self.button_to_set_title)

        btnlayout3 = QtWidgets.QHBoxLayout()
        btnlayout3.addWidget(self.text_xlable)
        btnlayout3.addWidget(self.text_ylable)
        btnlayout3.addWidget(self.text_title)

        btnlayout4 = QtWidgets.QHBoxLayout()
        btnlayout4.addWidget(self.button_to_import_data)
        btnlayout4.addWidget(self.textEdit)

        qw = QtWidgets.QWidget(self)
        qw.setLayout(btnlayout1)

        qw2 = QtWidgets.QWidget(self)
        qw2.setLayout(btnlayout2)

        qw3 = QtWidgets.QWidget(self)
        qw3.setLayout(btnlayout3)

        qw4 = QtWidgets.QWidget(self)
        qw4.setLayout(btnlayout4)

        layout.addWidget(qw)
        layout.addWidget(qw2)
        layout.addWidget(qw3)
        layout.addWidget(qw4)

        wid.setLayout(layout)

    def home(self):
        self.toolbar.home()

    def zoom(self):
        self.toolbar.zoom()

    def import_data(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())
        if fname[0]:
            try:
                self.x, self.y = np.loadtxt(fname[0], unpack=True, skiprows=1)
                with open(fname[0], 'r') as f:
                    data = f.read()
                self.textEdit.setText(data)
            except Exception as err:
                print(err)

    def plot(self):
        self.axes.plot(self.x, self.y, 'bo')
        self.axes.set_xlabel(self.xlabel)
        self.axes.set_ylabel(self.ylabel)
        self.axes.set_title(self.title)
        self.canvas.draw()

    def set_title(self):
        self.title = self.text_title.text()

    def set_xlabel(self):
        self.xlabel = self.text_xlable.text()

    def set_ylabel(self):
        self.ylabel = self.text_ylable.text()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Window()
    main.setWindowTitle('PyPlotGui')
    main.show()

    sys.exit(app.exec_())