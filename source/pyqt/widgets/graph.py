from PyQt5 import QtWidgets
import pyqtgraph as pg

class GraphWidget(pg.PlotWidget):
    num_of_datapoints = 100
    def __init__(self):
        super(GraphWidget, self).__init__()

        self.datalines = []

    def add_dataline(self, d):
        self.datalines.append(d)
    

class DataLine():

    def __init__(self, name) -> None:
        self.dataline_name = name

        self.x = [0 for x in range(100)]

        self.y = [0 for x in range(100)]

    def append(self) -> None:
        pass

