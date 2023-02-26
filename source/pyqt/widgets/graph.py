from PyQt5 import QtWidgets
import pyqtgraph as pg

class GraphWidget(pg.PlotWidget):
    all_graph_instances = []
    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent)

        self.__class__.all_graph_instances.append(self)

        self.updated = False