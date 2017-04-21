import numpy as np
from scipy.optimize import curve_fit


class Fit:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @staticmethod
    def poly1(x, a, b):
        return a * x + b

    @staticmethod
    def poly2(x, a, b, c):
        return a*x*x + b*x + c

    def do_fit_by_poly1(self):
        popt, pcov = curve_fit(self.poly1, self.x, self.y)
        a = popt[0]
        b = popt[1]
        error = np.abs(np.diag(pcov) ** 0.5)
        da = error[0]
        db = error[1]
        return a, b, da, db

    def do_fit_by_poly2(self):
        popt, pcov = curve_fit(self.poly2, self.x, self.y)
        a = popt[0]
        b = popt[1]
        c = popt[2]
        error = np.abs(np.diag(pcov) ** 0.5)
        da = error[0]
        db = error[1]
        dc = error[2]
        return a, b, c, da, db, dc

