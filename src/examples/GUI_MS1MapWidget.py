import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QAction

import pyqtgraph as pg
from pyqtgraph import PlotWidget

import numpy as np

import time
MODULE_PATH = "/media/sachsenb/Samsung_T5/OpenMS/pyOpenMS/pyopenms/__init__.py"
MODULE_NAME = "pyopenms"
import importlib
import sys
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
print(spec)
pyopenms = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = pyopenms
spec.loader.exec_module(pyopenms)


sys.path.insert(0, '../view')
from MS1MapWidget import *

pg.setConfigOption('background', 'w') # white background
pg.setConfigOption('foreground', 'k') # black peaks

class App(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(800, 600) 
        self._initUI()

    def _initUI(self):
        self.setWindowTitle('MS1MapWidget')
        self.centerWidget = QWidget(self)
        self.setCentralWidget(self.centerWidget)
        self.layout = QVBoxLayout(self.centerWidget)
        exp = pyopenms.MSExperiment()
        pyopenms.MzMLFile().load("../data/190509_Ova_native_25ngul_R.mzML", exp)
        self.ms1mapwidget = MS1MapWidget(self)

        self.ms1mapwidget.setSpectra(exp)
        self.layout.addWidget(self.ms1mapwidget)
        self._setMainMenu()
        self._setExitButton()

    def _setMainMenu(self):
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        self.titleMenu = mainMenu.addMenu('PyOpenMS')

    def _setExitButton(self):
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        self.titleMenu.addAction(exitButton)
        
    def closeEvent(self, event):
        self.close
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
