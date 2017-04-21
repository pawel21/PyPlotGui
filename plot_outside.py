from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QComboBox

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import sys

from fit import Fit

matplotlib.use('qt5Agg')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Palatino'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams.update({'font.size': 28})
plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{polski}'


class Data_to_plot:
    x = 0
    y = 0
    z = 0
    xlabel = "x"
    ylabel = "y"
    title = ""


class Window(QtWidgets.QMainWindow, Data_to_plot):
    def __init__(self, parent=None):
        super().__init__(parent)
        wid = QWidget(self)
        self.setCentralWidget(wid)

        self.button_to_plot = QtWidgets.QPushButton('Plot')
        self.button_to_plot.clicked.connect(self.plot)

        self.button_to_plot_twinx = QtWidgets.QPushButton('Plot twinx')
        self.button_to_plot_twinx.clicked.connect(self.plot_twinx)

        self.button_to_reset = QtWidgets.QPushButton('Reset')
        self.button_to_reset.clicked.connect(self.reset)

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
        self.button_to_import_data_xyz.clicked.connect(self.import_data_xyz)

        self.label_fit = QtWidgets.QLabel('Fit')

        self.combo_to_chose_poly = QComboBox(self)
        self.combo_to_chose_poly.addItem("poly1")
        self.combo_to_chose_poly.addItem("poly2")
        self.fit_info = QtWidgets.QLineEdit()
        self.fit_info.setEnabled(True)
        self.combo_to_chose_poly.activated[str].connect(self.fit)
        #set the layout
        layout = QtWidgets.QVBoxLayout()

        btnlayout1 = QtWidgets.QHBoxLayout()
        btnlayout1.addWidget(self.button_to_plot)
        btnlayout1.addWidget(self.button_to_plot_twinx)
        btnlayout1.addWidget(self.button_to_reset)
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

        btnlayout5 = QtWidgets.QHBoxLayout()
        btnlayout5.addWidget(self.label_fit)
        btnlayout5.addWidget(self.combo_to_chose_poly)
        btnlayout5.addWidget(self.fit_info)

        qw = QtWidgets.QWidget(self)
        qw.setLayout(btnlayout1)

        qw2 = QtWidgets.QWidget(self)
        qw2.setLayout(btnlayout2)

        qw3 = QtWidgets.QWidget(self)
        qw3.setLayout(btnlayout3)

        qw4 = QtWidgets.QWidget(self)
        qw4.setLayout(btnlayout4)

        qw5 = QtWidgets.QWidget(self)
        qw5.setLayout(btnlayout5)

        layout.addWidget(qw)
        layout.addWidget(qw2)
        layout.addWidget(qw3)
        layout.addWidget(qw5)
        layout.addWidget(qw4)

        wid.setLayout(layout)
        self.setGeometry(800, 900, 600, 700)

    def home(self):
        pass

    def reset(self):
        plt.close("all")

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
        self.fig, self.axes = plt.subplots()
        self.axes.plot(self.x, self.y, 'bo', markersize=10)
        plt.grid(True)
        plt.show()

    def plot_twinx(self):
        self.fig, self.axes = plt.subplots()
        self.axes.plot(self.x, self.y, 'bo', label="prąd [A]", markersize=14)
        self.axes2 = self.axes.twinx()
        self.axes2.plot(self.x, self.z, 'r<', label="moc [W]", markersize=14)
        self.axes2.set_ylabel("moc [W]")
        box = self.axes.get_position()
        self.axes.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        self.axes2.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        self.axes.legend(loc='center left', bbox_to_anchor=(1.05, 0.8), frameon=False)
        self.axes2.legend(loc='upper left', bbox_to_anchor=(1.05, 0.8), frameon=False)
        plt.grid(True)
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

    def fit(self, text):
        f = Fit(self.x, self.y)
        if text=="poly1":
            a, b, da, db = f.do_fit_by_poly1()
            self.fit_info.setText("a={}; b={}".format(a, b))
            x = np.linspace(min(self.x), max(self.x), 1000)
            y = a*x + b
            self.axes.plot(x, y, 'r-', lw=2)
            self.fig.canvas.draw()
        if text == "poly2":
            a, b, c, da, db, dc = f.do_fit_by_poly2()
            self.fit_info.setText("a={}; b={}; c={}".format(a, b, c))
            x = np.linspace(min(self.x), max(self.x), 1000)
            y = a*x*x + b*x + c
            self.axes.plot(x, y, 'g-', lw=2)
            self.fig.canvas.draw()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Window()
    main.setWindowTitle('PyPlotGui')
    main.show()

    sys.exit(app.exec_())
