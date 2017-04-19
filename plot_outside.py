import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('qt5Agg')
import numpy as np
import os

plt.rcParams.update({'font.size': 18})

class Data_to_plot:
    x = 0
    y = 0
    x = 0
    xlabel = "x"
    ylabel = "y"
    title = ""


class Window(QtWidgets.QMainWindow, Data_to_plot):
    def __init__(self, parent=None):
        super().__init__(parent)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        self.fig, self.axes = plt.subplots()

        self.button_to_plot = QtWidgets.QPushButton('Plot')
        self.button_to_plot.clicked.connect(self.plot)

        self.button_to_plot_twinx = QtWidgets.QPushButton('Plot twinx')
        self.button_to_plot_twinx.clicked.connect(self.plot_twinx)

        self.button_to_zoom = QtWidgets.QPushButton('Zoom')
        self.button_to_zoom.clicked.connect(self.zoom)

        self.button_to_home = QtWidgets.QPushButton('Home')
        self.button_to_home.clicked.connect(self.home)

        self.button_to_save_fig = QtWidgets.QPushButton('Save')
        self.button_to_save_fig.clicked.connect(self.save_fig)


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

        self.button_to_import_data_xyz = QtWidgets.QPushButton('import data x,y,z')

        #set the layout
        layout = QtWidgets.QVBoxLayout()

        btnlayout1 = QtWidgets.QHBoxLayout()
        btnlayout1.addWidget(self.button_to_plot)
        btnlayout1.addWidget(self.button_to_plot_twinx)
        btnlayout1.addWidget(self.button_to_zoom)
        btnlayout1.addWidget(self.button_to_home)
        btnlayout1.addWidget(self.button_to_save_fig)

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
        btnlayout4.addWidget(self.button_to_import_data_xyz)

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
        pass

    def zoom(self):
        pass

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

    def import_data_xyz(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())
        if fname[0]:
            try:
                self.x, self.y, self.z = np.loadtxt(fname[0], unpack=True, skiprows=1)
                with open(fname[0], 'r') as f:
                    data = f.read()
                self.textEdit.setText(data)
            except Exception as err:
                print(err)

    def plot(self):
        self.axes.plot(self.x, self.y, 'bo')
        plt.show()

    def plot_twinx(self):
        self.axes.plot(self.x, self.y, 'bo')
        self.axes2 = self.axes.twinx()
        self.axes2.plot(self.x, self.z, 'r<')
        plt.show()

    def set_title(self):
        self.title = self.text_title.text()
        self.axes.set_title(self.title)
        self.fig.canvas.draw()

    def set_xlabel(self):
        self.xlabel = self.text_xlable.text()
        self.axes.set_xlabel(self.xlabel)
        self.fig.canvas.draw()

    def set_ylabel(self):
        self.ylabel = self.text_ylable.text()
        self.axes.set_ylabel(self.ylabel)
        self.fig.canvas.draw()

    def save_fig(self):
        path_to_save_fig = os.path.join(os.getcwd(), "wykres.jpg")
        plt.savefig(path_to_save_fig)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Window()
    main.setWindowTitle('PyPlotGui')
    main.show()

    sys.exit(app.exec_())
