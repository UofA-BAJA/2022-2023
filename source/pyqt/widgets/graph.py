from PyQt5 import QtWidgets
import pyqtgraph as pg

class GraphWidget(pg.PlotWidget):

    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent)